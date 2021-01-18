import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
#while True:
with sr.Microphone() as source:
    print('Speak Anything:')
    audio = r.listen(source)
                    
    try:
        text = r.recognize_google(audio)
        r.adjust_for_ambient_noise(source, duration = 1)
        print("You said:{}".format(text))
                       
    except:
        print("Sorry!")

    finally:
        print("Kudos!")
            
        
