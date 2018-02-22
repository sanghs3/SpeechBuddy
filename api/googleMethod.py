import io
import os
import googleMethod


#Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import wave

def googleApiCall(path):

# Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = path #'/home/sanghs3/Capstone/umm.flac'


    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=48000,
        language_code='en-US',
        enable_word_time_offsets=True)

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    return response

# for result in response.results:
    #         alternative = result.alternatives[0]
    #         print('Transcript: {}'.format(alternative.transcript))
    #         print('Confidence: {}'.format(alternative.confidence))
    #
    #         for word_info in alternative.words:
    #             word = word_info.word
    #             start_time = word_info.start_time
    #             end_time = word_info.end_time
    #             print('Word: {}, start_time: {}, end_time: {}'.format(
    #                 word,
    #                 start_time.seconds + start_time.nanos * 1e-9,
    #                 end_time.seconds + end_time.nanos * 1e-9))