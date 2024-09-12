# Controla tu computadora a través de gestos

## Descripción

Este proyecto es un prototipo de un sistema de control de la computadora a través de gestos. El sistema se basa en la detección de gestos a través de una cámara web y la ejecución de acciones en la computadora en función de los gestos detectados.

## Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

- **Recibir comandos de voz**: El sistema recibe comandos de voz para escribir texto en la computadora:
    
      - "escribir": Comenzará a escribir el texto que se le dicte.
      - "enter": Presiona un salto de línea.
      - "abrir": Buscará en el menú de inicio la aplicación que se le dicte y la abrirá.
      - "cerrar": Cerrará la aplicación actualmente activa.
      - "finalizar": Finalizará la ejecución del programa.

- **Control del mouse**: El sistema detecta la posición de la mano y los dedos a través de la cámara web y mueve el cursor del mouse en función de la posición de la mano.


## Requisitos

Las siguientes librerías se encuentran listadas en el archivo `requirements.txt` y son necesarias para ejecutar el proyecto:

- opencv-python
- mediapipe
- SpeechRecognition
- pyautogui
- pyaudio
- setuptools

## Primeros Pasos

Para ejecutar el proyecto, sigue los siguientes pasos:

Si estás usando Visual Studio Code, puedes ejecutar la tarea `win-init` o `linux-init` para instalar las librerías necesarias:

1. Presiona `Ctrl + Shift + P` para abrir el menú de comandos.

2. Escribe `Tasks: Run Task` y selecciona la opción `Tasks: Run Task`.

3. Selecciona la tarea `win-init` o `linux-init` para instalar las librerías necesarias.

Esta tarea va a crear un entorno virtual, activarlo e instalar las librerías necesarias en el entorno virtual.

Si no estás usando Visual Studio Code, sigue los siguientes pasos:

1. Inicializa un entorno virtual (opcional)

2. Ejecuta el siguiente comando para instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

### Ejecución

Ejecuta el siguiente comando para iniciar el sistema:

```bash
python main.py
```