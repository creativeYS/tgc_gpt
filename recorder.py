# pip install pyaudio
import pyaudio, wave, threading

# 녹음 설정
FORMAT = pyaudio.paInt16  # 16비트 형식
CHANNELS = 2  # 스테레오
RATE = 44100  # 샘플링 레이트 (44.1kHz)
CHUNK = 1024  # 버퍼 크기
OUTPUT_FILENAME = "c:\\temp\\test.wav"  # 출력 파일 이름

recorder = False
recording = True

# pyaudio 객체 생성
audio = pyaudio.PyAudio()

def start_recording():
    # 스트림 열기
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    frames = []

    print("Recording... Press 's' to stop.")

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    # 스트림 정지 및 종료
    stream.stop_stream()
    stream.close()

    # WAV 파일로 저장
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Recording saved as {OUTPUT_FILENAME}")

def start():
    global recorder
    global recording
    recording = True
    recorder = threading.Thread(target=start_recording)
    print('start recording')
    recorder.start()

def stop():
    global recorder
    global recording
    recording = False
    recorder.join()
    print('stop recording')