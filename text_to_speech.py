import json
from gtts import gTTS
import os

# Path to the JSON file containing the LLM response
input_file_path = "output_from_llm.json"

# Load the assistant's response from the JSON file
def load_response_from_json(json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            response = data.get("response", "").strip()
            if not response:
                raise ValueError("The 'response' field in the JSON file is empty or missing.")
            return response
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{json_file}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file '{json_file}'.")

# Load the response
response_text = load_response_from_json(input_file_path)

# Convert text to speech
output_audio_file = "output.mp3"
tts = gTTS(text=response_text, lang="en")
tts.save(output_audio_file)

# Play the generated speech
print(f"Playing the generated speech from {output_audio_file}...")
os.system(f"start {output_audio_file}")  # Use 'start' for Windows, 'xdg-open' for Linux, or 'open' for macOS





"""
import json
from gtts import gTTS
import os
import pygame

# Load the response from `output_from_llm.json`
input_file_path = "output_from_llm.json"
with open(input_file_path, "r") as file:
    data = json.load(file)
    response_text = data.get("response", "")

    if not response_text:
        raise ValueError("The response text is missing in the input file.")

# Convert the text to speech and save it as `output.mp3`
output_audio_path = "output.mp3"
tts = gTTS(text=response_text, lang="en")
tts.save(output_audio_path)
print(f"Audio saved as {output_audio_path}")

# Play the audio using pygame
pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load(output_audio_path)
    pygame.mixer.music.play()

    print("Playing audio...")
    while pygame.mixer.music.get_busy():  # Wait until playback finishes
        pygame.time.Clock().tick(10)

finally:
    pygame.mixer.quit()
    pygame.quit()
"""
