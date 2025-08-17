# Transcript Tool
A quick python script I made for bulk transcripts right off of my audio recorder.
# Getting Started
## Mac
* Install Python
* Add environment variables
```sh
brew install ffmpeg
python3 -m pip install dotenv git+https://github.com/absadiki/pywhispercpp --break-system-packages
python3 src/main.py
```

To get coreml model
```sh
git clone https://github.com/ggml-org/whisper.cpp.git
pip install ane_transformers
pip install openai-whisper
pip install coremltools
./whisper.cpp/models/generate-coreml-model.sh large-v3-turbo
mv ./whisper.cpp/models/coreml-encoder-large-v3-turbo.mlpackage ~/Library/Application Support/pywhispercpp/models
```
TODO get coreml model actually working