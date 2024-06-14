import os
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

if __name__ == "__main__":
    print("welcome")
    while True:
        x = input("enter the text: ")
        if x == 'q':
            speak.Speak("bye bye friend")
            break
    
        speak.Speak(f"{x}")
