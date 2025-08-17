from pywhispercpp.model import Model
from dotenv import load_dotenv
import glob
import os
import re
import warnings

load_dotenv()
AUDIO_IN_DIR = os.getenv("AUDIO_IN_DIR")
TEXT_OUT_DIR = os.getenv("TEXT_OUT_DIR")
warnings.filterwarnings("ignore")
model = Model("large-v3-turbo")

audio_paths = glob.glob(f"{AUDIO_IN_DIR}/*.MP3") + glob.glob(f"{AUDIO_IN_DIR}/*.mp3")
text_paths = glob.glob(f"{TEXT_OUT_DIR}/*.md")
for audio_path in audio_paths:
    audio_filename = re.match(r"[a-zA-Z0-9-_\/\\]*[\/\\]([a-zA-Z0-9-_\/\\]*)\.(mp3|MP3)", audio_path).group(1)
    text_file_exists = False
    for text_path in text_paths:
        if audio_filename in text_path:
            text_file_exists = True
    if not text_file_exists:
        print(f"Generating transcript for: {audio_filename}.MP3")

        text_segments = []
        segments = model.transcribe(audio_path)
        for segment in segments:
            text_segments.append(segment.text)
        text = "".join(text_segments)

        with open(f"{TEXT_OUT_DIR}/{audio_filename}.md", "w") as file:
            file.write(text)
print("\nDone!")
