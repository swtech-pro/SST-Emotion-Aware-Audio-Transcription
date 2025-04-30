# 🎧 Emotion-Aware Audio Transcription App (Version 2)

This prototype adds emotion detection from audio alongside Whisper-based transcription. It tags the transcribed text with emotions like (गुस्से में), (उदासी में), (खुशी में), etc.

## 🚀 Features

- 🎙️ Mic or Audio File Input
- 🧠 Whisper for speech-to-text
- 😄 pyAudioAnalysis for emotion detection (based on pitch/energy)
- 📋 Combined output: text + emotion tag
- 🌐 Gradio Interface

## 🛠️ Setup Instructions

```bash
git clone https://github.com/yourusername/audio_transcription_v2.git
cd audio_transcription_v2
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ How to Run

```bash
python app.py
```

Open http://127.0.0.1:7860/ in your browser.

## 📁 File Structure

```
audio_transcription_v2/
├── app.py
├── requirements.txt
├── README.md
├── license.txt
├── .gitignore
└── .gitattributes
```

## 📜 License

MIT License – see `license.txt`.
