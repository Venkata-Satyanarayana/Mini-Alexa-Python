# 🎙️ Python Voice Assistant
A simple voice-controlled assistant using Python libraries like speech_recognition, pyttsx3, wikipedia, pyautogui, and more. It can play YouTube videos, tell jokes, fetch information from Wikipedia, announce the current time, and open applications via voice commands.

## 🚀 Features
Voice-activated commands with a wake word ("Alexa")

Play songs on YouTube

Tell the current time

Fetch brief summaries from Wikipedia

Tell jokes using pyjokes

Open applications on your system

Text-to-speech feedback

## 🛠️ Requirements
Install the required Python libraries using pip:

bash
Copy
Edit
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes pyautogui pyaudio
### ⚠️ Note: pyaudio may require additional setup depending on your OS. On Windows, you can install it via:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
## 📁 Files
main.py – The main script containing the voice assistant logic.

## 📌 Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Run the script:

bash
Copy
Edit
python main.py
Say a command starting with the wake word "Alexa", such as:

“Alexa play despacito”

“Alexa what time is it”

“Alexa who is Albert Einstein”

“Alexa tell me a joke”

“Alexa open notepad”

## ❗ Known Issues
Background noise can affect voice recognition.

pyautogui opening apps via keystrokes may not work consistently across systems.

The assistant runs indefinitely until a manual interruption (Ctrl+C) or using the voice command: "Alexa stop"
