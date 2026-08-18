# Jarvis Assistant 🎙️🤖

A voice-controlled Python AI assistant designed to automate daily tasks using speech recognition, text-to-speech, web scraping, system controls, and messaging capabilities.

---

## 🌟 Features

* **Voice Interaction & Speech Recognition**: Listens to user voice commands using `sounddevice` and `speech_recognition` via Google Speech API.
* **Multilingual Support**: Supports both English and Hindi speech recognition along with translation functionality (`googletrans`).
* **Text-to-Speech Output**: Speaks back responses naturally using offline `pyttsx3` text-to-speech engine.
* **Web & Search Automation**: Performs quick Google and YouTube searches, opens specific websites, and retrieves Wikipedia summaries.
* **Media & YouTube Controls**: Controls playback actions via hotkeys (Play, Pause, Mute, Skip, Rewind, Fullscreen, Film Mode).
* **Automated Messaging**: Sends scheduled WhatsApp messages automatically using `pywhatkit`.
* **System Utilities**: Takes custom screenshots, sets custom alarms, tells jokes, and executes system process controls (closes applications like Chrome, Edge, Notepad, VS Code, etc.).

---

## 🛠️ Built With

* **Language**: Python 3.x
* **Core Libraries**:
  * `pyttsx3` - Offline Text-to-Speech Engine
  * `speech_recognition` & `sounddevice` - Voice Input & Audio Recording
  * `pywhatkit` - YouTube Search & WhatsApp Automation
  * `pyautogui` & `keyboard` - GUI Automation & Keyboard Hotkeys
  * `googletrans` - Language Translation
  * `wikipedia` - Quick Information Fetching
  * `pyjokes` - Programmer Jokes

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/madhavr432/Jarvis-Assistant.git](https://github.com/madhavr432/Jarvis-Assistant.git)
   cd Jarvis-Assistant
2. **Install required dependencies
    ```bash
   pip install pyttsx3 pywhatkit pyautogui keyboard pyjokes AppOpener googletrans==3.1.0a0 wikipedia playsound sounddevice SpeechRecognition
3. **Run the Assistant
   ```bash
   python "jarvis 2.0.py"
🎙️ Sample Commands
    ## 🎙️ Sample Commands

| Category | Voice Command | Description / Action |
| :--- | :--- | :--- |
| **Greeting** | `"hello"` | Greets the user |
| **Search** | `"google search [topic]"` | Searches Google for the given topic |
| **Search** | `"youtube search [topic]"` | Searches YouTube for the given topic |
| **Search** | `"wikipedia [topic]"` | Speaks a brief summary of the topic from Wikipedia |
| **System** | `"screenshot"` | Prompts for a file name and saves the screenshot |
| **System** | `"close chrome"` | Closes Google Chrome |
| **System** | `"close code"` | Closes VS Code |
| **Media** | `"play music"` | Prompts for a song name and starts playing it |
| **Media** | `"pause"` / `"mute"` / `"full screen"` | Controls YouTube playback using hotkeys |
| **Messaging** | `"whatsapp munna"` | Schedules and sends a WhatsApp message |
| **Utilities** | `"translate"` | Listens in Hindi and translates the speech to English |
| **Utilities** | `"alarm"` | Sets a voice-activated alarm |
