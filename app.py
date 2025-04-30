import whisper
import gradio as gr
from pydub import AudioSegment
from pyAudioAnalysis import MidTermFeatures as mF
import numpy as np
import os

model = whisper.load_model("tiny")

def convert_to_wav(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path

def detect_emotion(audio_path):
    [features, _, _] = mF.mid_feature_extraction(audio_path, 1.0, 1.0, 0.050, 0.050)
    energy = np.mean(features[1])
    pitch = np.mean(features[2])
    if energy > 0.2 and pitch > 0.1:
        return "(गुस्से में)"
    elif energy < 0.05 and pitch < 0.04:
        return "(उदासी में)"
    elif energy > 0.15 and pitch < 0.05:
        return "(खुशी में)"
    else:
        return "(सामान्य भाव में)"

def transcribe_with_emotion(audio):
    if audio is None:
        return "Please provide audio input."
    if audio.endswith(".mp3"):
        audio = convert_to_wav(audio)
    emotion = detect_emotion(audio)
    result = model.transcribe(audio)
    return f"{emotion} {result['text']}"

gr.Interface(
    fn=transcribe_with_emotion,
    inputs=[gr.Audio(sources=["microphone", "upload"], label="🎙️ Speak or Upload Audio")],
    outputs=[gr.Textbox(label="📝 Transcription with Emotion")],
    title="🎧 Emotion-Aware Audio Transcription",
    description="Transcribe speech to text and detect voice emotion using Whisper + pyAudioAnalysis.",
    allow_flagging="never"
).launch()
