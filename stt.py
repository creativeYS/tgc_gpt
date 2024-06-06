# pip install SpeechRecognition
# pip install librosa
import speech_recognition as sr

def stt():
    r = sr.Recognizer()

    # recognize_google() : Google Web Speech API
    # recognize_google_cloud() : Google Cloud Speech API
    # recognize_bing() : Microsoft Bing Speech API
    # recognize_houndify() : SoundHound Houndify API
    # recognize_ibm() : IBM Speech to Text API
    # recognize_wit() : Wit.ai API
    # recognize_sphinx() : CMU Sphinx (오프라인에서 동작 가능)

    import librosa
    sample_wav, rate = librosa.core.load('C:\\Temp\\test.wav')

    korean_audio = sr.AudioFile('C:\\Temp\\test.wav')

    with korean_audio as source:
        audio = r.record(source)
    result = r.recognize_google(audio_data=audio, language='ko-KR')
    print(result)
    return result