import cv2
import mediapipe as mp
import pyautogui
import collections

def initialize_hand_detection():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils
    return mp_hands, hands, mp_drawing

def initialize_video_capture():
    cap = cv2.VideoCapture(0)
    return cap

def get_screen_size():
    return pyautogui.size()

def gesture_detection(stop_event):
    mp_hands, hands, mp_drawing = initialize_hand_detection()
    cap = initialize_video_capture()
    screen_width, screen_height = get_screen_size()

    # Historial de coordenadas para suavizar el movimiento
    history_length = 5
    x_history = collections.deque(maxlen=history_length)
    y_history = collections.deque(maxlen=history_length)

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir la imagen a RGB para Mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dibujar las marcas de la mano
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Obtener las coordenadas de la punta del dedo índice y pulgar
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Convertir las coordenadas a píxeles
                height, width, _ = frame.shape
                index_finger_x, index_finger_y = int(index_finger_tip.x * width), int(index_finger_tip.y * height)
                thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)

                # Mapear las coordenadas de la cámara a la resolución de la pantalla
                # Invertir el eje X para corregir el movimiento invertido
                mapped_x = screen_width - int((index_finger_x / width) * screen_width)
                mapped_y = int((index_finger_y / height) * screen_height)

                # Agregar las coordenadas al historial
                x_history.append(mapped_x)
                y_history.append(mapped_y)

                # Calcular la media de las coordenadas para suavizar el movimiento
                smoothed_x = sum(x_history) // len(x_history)
                smoothed_y = sum(y_history) // len(y_history)

                # Mover el cursor del mouse a la posición mapeada
                pyautogui.moveTo(smoothed_x, smoothed_y)

                # Calcular la distancia entre la punta del dedo índice y el pulgar
                distance = ((thumb_x - index_finger_x) ** 2 + (thumb_y - index_finger_y) ** 2) ** 0.5

                # Si la distancia es pequeña (Umbral de 30 píxeles), hacer clic
                if distance < 30:
                    pyautogui.click()

                # Mostrar la imagen con las marcas de la mano
                cv2.imshow('Hand Tracking', frame)

                # Salir del bucle si se presiona la tecla 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    stop_event.set()
                    break

    # Liberar la captura de video y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()
    print("Recursos de video liberados correctamente.")