import speech_recognition as sr
IBM_USERNAME = "6f8206c1-cb24-4408-a7e0-d57331c2d4c0"
IBM_PASSWORD = "5wzbTWGJk6yF"

def getresult(path):
    r = sr.Recognizer()
    with sr.WavFile(path) as source:
        audio = r.record(source)
        text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='zh-CN')
        return text

if __name__ == '__main__':
    path = r'C:\Users\heyon\Desktop\2.wav'
    text = getresult(path)
    print(text)