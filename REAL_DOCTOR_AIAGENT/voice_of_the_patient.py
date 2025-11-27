import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
from groq import Groq

# Ensure FFmpeg path is set correctly

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def record_audio(file_path, timeout=10, phrase_time_limit=None, mic_index=None):
    """
    Records audio from the microphone and saves it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Max time to wait for speech to start (seconds).
    phrase_time_limit (int): Max time for a phrase to be recorded (seconds).
    mic_index (int): Specific microphone index (default: None, auto-detect).
    """
    recognizer = sr.Recognizer()
    
    try:
        # List available microphones
        if mic_index is None:
            mic_list = sr.Microphone.list_microphone_names()
            logging.info(f"Available microphones: {mic_list}")

        # Use specific microphone if provided
        with sr.Microphone(device_index=mic_index) as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=3)  # Increased duration for better noise adjustment
            logging.info("Start speaking now...")
            
            # Record the audio
            try:
                audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                logging.info("Recording complete.")
            except sr.WaitTimeoutError:
                logging.error("No speech detected within the timeout period. Please try again.")
                return
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run the function
audio_filepath = "patient_voice_test_for_patient.mp3"
#record_audio(file_path=audio_filepath, timeout=10)


GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    return transcription.text
