# 🎙️ Jarvis Assistant

A **voice-controlled personal assistant built with Python** that helps automate everyday tasks through speech recognition, text-to-speech, browser automation, media controls, and system utilities.

Jarvis listens to voice commands, understands supported requests, and performs actions to make everyday computer interactions faster and more convenient.

## ✨ Features

### 🎤 Voice Interaction
- Recognizes spoken commands using Google's Speech Recognition API.
- Records audio using `sounddevice` and `SpeechRecognition`.
- Responds with speech using the offline `pyttsx3` text-to-speech engine.
- Supports a conversational command loop.

### 🌐 Web Search & Information
- Search Google using voice commands.
- Search YouTube for videos and topics.
- Open websites through voice commands.
- Retrieve short summaries from Wikipedia.
- Open Google Maps.

### 🎵 Music & YouTube Controls
- Play songs using local audio files or YouTube.
- Control YouTube playback using keyboard shortcuts.
- Pause, mute, rewind, skip, and toggle fullscreen.
- Access additional playback controls through voice commands.

### 💬 WhatsApp Automation
- Compose WhatsApp messages through voice input.
- Schedule messages using `pywhatkit`.
- Support predefined contacts configured in the script.

*Note: WhatsApp Web, an appropriate browser session, and valid contact details may be required.*

### 🖥️ System Automation
- Capture screenshots and save them with custom filenames.
- Open and close supported applications.
- Control browser tabs and windows.
- Trigger keyboard shortcuts using voice commands.

### 🌍 Translation & Utilities
- Recognize Hindi speech and translate it into English.
- Set a time-based alarm.
- Tell programming-related jokes.
- Repeat recognized speech on request.
- Respond to basic greetings and conversational commands.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `SpeechRecognition` | Speech recognition |
| `sounddevice` | Audio recording |
| `pyttsx3` | Text-to-speech |
| `googletrans` | Language translation |
| `pywhatkit` | YouTube playback and WhatsApp automation |
| `pyautogui` | Screenshots and GUI automation |
| `keyboard` | Keyboard shortcuts |
| `wikipedia` | Wikipedia summaries |
| `webbrowser` | Opening websites |
| `pyjokes` | Programming jokes |
| `playsound` | Alarm audio playback |
| `AppOpener` | Application launching |

## 🚀 Getting Started

### Prerequisites

- Windows operating system
- Python 3.8 or later (a compatible version for all dependencies is required)
- A working microphone
- Internet connection for online speech recognition, searches, translation, and other online features

### 1. Clone the Repository

```bash
git clone https://github.com/madhavr432/Jarvis-Assistant.git
cd Jarvis-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it in Windows Command Prompt:

```bat
.venv\Scripts\activate
```

For PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install pyttsx3 pywhatkit pyautogui keyboard pyjokes AppOpener googletrans==3.1.0a0 wikipedia playsound sounddevice SpeechRecognition
```

If installation fails, check the Python version and the compatibility requirements of the specific package reporting the error.

### 4. Run Jarvis

```bash
python "jarvis 2.0.py"
```

Make sure the filename matches the Python script in your local repository.

## 🎙️ Sample Voice Commands

| Category | Voice Command | Action |
|---|---|---|
| Greeting | `hello` | Greets the user |
| Conversation | `how are you` | Gives a conversational response |
| Search | `google search Python` | Searches Google |
| Search | `youtube search Python tutorials` | Searches YouTube |
| Information | `wikipedia artificial intelligence` | Reads a short Wikipedia summary |
| Websites | `open youtube` | Opens YouTube |
| Music | `music` | Asks for a song name |
| Media | `pause` | Toggles YouTube playback using a keyboard shortcut |
| Media | `mute` | Toggles mute |
| Media | `full screen` | Toggles fullscreen |
| System | `screenshot` | Captures and saves a screenshot |
| System | `close chrome` | Terminates Chrome |
| System | `close code` | Terminates VS Code |
| Messaging | `whatsapp munna` | Prompts for a message and scheduling time |
| Translation | `translate` | Listens for Hindi speech and translates it |
| Utility | `jokes` | Tells a programming joke |
| Utility | `alarm` | Sets a time-based alarm |
| Exit | `bye` | Exits the assistant |

*Available commands depend on the conditions and branches implemented in the script.*

## ⚙️ Configuration & Notes

- **Voice recognition:** Online recognition requires internet access and may not recognize every command correctly.
- **Text-to-speech:** The assistant uses the Windows SAPI5 speech engine through `pyttsx3`.
- **Audio files:** Update the local music and alarm file paths in the script to match your computer.
- **Screenshots:** Configure the screenshot directory to a folder that exists and is writable.
- **WhatsApp:** Configure the intended contact numbers and use the required WhatsApp Web session.
- **Keyboard controls:** Media shortcuts depend on the active application and window focus.
- **Application termination:** Commands that close applications may cause unsaved work to be lost.

## 🔮 Future Improvements

- [ ] Add a configurable wake word.
- [ ] Improve speech recognition error handling.
- [ ] Add a configuration file for contacts, audio files, and application paths.
- [ ] Implement more reliable application detection and control.
- [ ] Add an AI-powered conversational interface.
- [ ] Introduce a plugin-based architecture for new commands.
- [ ] Add logging and automated tests.
- [ ] Provide a requirements file for reproducible installation.

## 🔒 Privacy & Safety

Jarvis uses a combination of local computer automation and online services. Speech sent to Google's recognition service and requests made to external services may be processed outside your computer.

Use messaging and system-control features carefully. Review commands before sending messages, avoid hardcoding sensitive information, and never commit personal credentials or private contact details to a public repository.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them.
4. Submit a pull request describing your improvements.


---

**Built with Python 🐍 and a little voice-controlled automation.**
