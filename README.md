# 🎤 Speech Recognition Web App using Python & Streamlit

A complete Speech Recognition application built with **Python** that converts real-time microphone input into text.  
The project includes both **core speech recognition logic** and an **interactive Streamlit web interface**, making it practical, user-friendly, and resume-ready.

---


## 🚀 Features

- 🎙️ Real-time speech input using microphone
- 🧠 Speech-to-text conversion using Google Speech Recognition API
- 🌐 Interactive web interface built with Streamlit
- 🔊 Automatic background noise adjustment
- ⏱️ Timeout handling to avoid infinite listening
- ❌ Robust error handling for unclear speech and network issues
- 🇮🇳 Optimized for Indian English (`en-IN`)
- 🧩 Clean and modular project structure


---

## 🛠️ Tech Stack

- **Python**
- **SpeechRecognition**
- **PyAudio**
- **Streamlit**
- **VS Code**
- **Git & GitHub**

---

## 📁 Project Structure <br>
speech-recognition-python/ <br>
│  <br>
├── app.py # Streamlit web application  <br>
├── speech_utils.py # Speech recognition logic  <br>
├── requirements.txt # Project dependencies  <br>
├── README.md # Project documentation  <br>
├── .gitignore # Ignored files and folders  <br>
└── venv/ # Virtual environment (not pushed to GitHub)  <br>


## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
bash

- git clone https://github.com/rushikeshghonse/Speech-Recognition-Using-Python.git
- cd Speech-Recognition-Using-Python

### 2️⃣ Create and activate a virtual environment
- python -m venv venv

### Windows
- venv\Scripts\activate

### macOS / Linux
- source venv/bin/activate

### 3️⃣ Install dependencies
- pip install -r requirements.txt

### ▶️ Run the Application
- streamlit run app.py

The application will open automatically in your browser at: http://localhost:8501
Click “Start Listening”, speak into your microphone, and the recognized text will be displayed on the screen.


## 🧠 How the Application Works

Streamlit provides a button-based web interface
1.On button click: 
    -Microphone is activated 
    -Ambient noise is calibrated
    -Speech is recorded with time limits
2.Recorded audio is sent to Google Speech Recognition
3.Converted text is displayed on the web UI
4.Errors such as silence, unclear speech, or network issues are handled gracefully

## ⚠️ Requirements & Notes

- Active internet connection is required (Google Speech API)

- Microphone access must be enabled

- Best results in a quiet environment

- Python 3.10+ recommended (Python 3.11 preferred)


## 🔮 Future Enhancements

- 🔁 Voice command execution (open apps, browser, etc.)

- 💾 Save recognized speech to a text file

- 🌍 Multiple language support

- ☁️ Cloud deployment (Streamlit Cloud / Hugging Face Spaces)

- 📴 Offline speech recognition support

## 💼 Resume Highlight
- Built a Speech Recognition Web Application using Python and Streamlit to convert real-time microphone input into text with background noise handling, timeout management, and robust exception handling.

## 📜 License

- This project is open-source and available under the MIT License.

## 🙌 Acknowledgements

- Python SpeechRecognition library

- Google Speech Recognition API

- Streamlit community
