import threading
import voice_recognition as vr
import gesture_detector as gd

# Variable global para controlar la ejecución
stop_event = threading.Event()

if __name__ == "__main__":

    while not stop_event.is_set():
        # Iniciar el hilo de reconocimiento de voz
        voice_thread = threading.Thread(target=vr.voice_commands, args=(stop_event,))
        voice_thread.start()

        # Iniciar el hilo de detección de gestos
        gesture_thread = threading.Thread(target=gd.gesture_detection, args=(stop_event,))
        gesture_thread.start()

        # Esperar a que ambos hilos terminen
        voice_thread.join()
        gesture_thread.join()