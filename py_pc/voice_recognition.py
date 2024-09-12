import pyautogui
import speech_recognition as recognition

# Constantes para los comandos de voz
COMMAND_JARVIS = "escribir"
COMMAND_ENTER = "enter"
COMMAND_OPEN = "abrir"
COMMAND_CLOSE = "cerrar"
COMMAND_STOP = "finalizar"

def recognize_command(recognizer, microphone):
    """Reconoce un comando de voz y lo devuelve como texto."""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Escuchando comandos de voz...")
        audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio, language='es-ES').lower()
        print("Comando recibido:", command)
        return command

def execute_command(command, stop_event):
    """Ejecuta el comando de voz dado."""
    if COMMAND_JARVIS in command:
        text_to_write = command.split(COMMAND_JARVIS, 1)[1].strip().split("gracias", 1)[0].strip()
        pyautogui.write(text_to_write, interval=0.1)
    elif COMMAND_ENTER in command:
        pyautogui.press('enter')
    elif COMMAND_OPEN in command:
        text_to_search = command.split(COMMAND_OPEN, 1)[1].strip()
        pyautogui.hotkey('ctrl', 'esc')
        pyautogui.write(text_to_search, interval=0.1)
        pyautogui.press('enter')
    elif COMMAND_CLOSE in command:
        pyautogui.hotkey('alt', 'f4')
    elif COMMAND_STOP in command:
        stop_event.set()

def voice_commands(stop_event):
    """Maneja el reconocimiento de voz y la ejecución de comandos."""
    recognizer = recognition.Recognizer()
    microphone = recognition.Microphone()

    while not stop_event.is_set():
        try:
            command = recognize_command(recognizer, microphone)
            execute_command(command, stop_event)
        except recognition.UnknownValueError:
            print("No se pudo entender el audio")
        except recognition.RequestError as e:
            print(f"Error al solicitar resultados; {e}")
    
    print("Recursos de audio liberados correctamente.")