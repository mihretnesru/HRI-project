import pyaudio
import wave
import whisper
import json
import os

def record_audio(record_seconds=20, output_file="user_input.wav"):
    """
    Records audio for a specified duration and saves it to a WAV file.
    """
    print(f"Recording for {record_seconds} seconds...")
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    # Initialize PyAudio
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    # Record audio
    frames = []
    for _ in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(output_file, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))
    print("Recording finished.")
    return output_file

def transcribe_audio(file_path):
    """
    Transcribes audio using Whisper and returns the transcribed text.
    """
    print("Transcribing audio...")
    whisper_model = whisper.load_model("base")
    result = whisper_model.transcribe(file_path)
    return result["text"]

def main():
    audio_file = record_audio()
    text = transcribe_audio(audio_file)
    print(f"Transcribed Text: {text}")

    # Save the transcribed text to a JSON file
    with open("input_to_llm.json", "w") as json_file:
        json.dump({"question": text}, json_file)

    print("Transcribed text saved to input_to_llm.json.")

if __name__ == "__main__":
    main()
