# Importing Moudles
import random
import pyttsx3
import speech_recognition as sr

# Setuping the pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 130)
# Creating a Function for speak
def Say(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    
# Inputing data through voice
r = sr.Recognizer()
def TakeCommand():
    with sr.Microphone() as source:
        print("Your Turn:\nSay: stone, paper, scissor")
        
        # Capture the audio from Microphone
        audio = r.listen(source)
        
        try:
            # Convert audio to text by google's speech recognition service
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            Say("Sorry, say that again.")

# Starting a game loop
while (True):
    # Inputing information
    Human = TakeCommand()
    Computer = random.randint(1,3)
    # Reconizing Computer Input
    if(Computer == 1):
        Com_Input = "stone"
    elif(Computer == 2):
        Com_Input = "paper"
    elif(Computer == 3):
        Com_Input = "scissor"

    # Creating a desiding function - game
    def Game(Com, You):
        if You == "stone":
            if(Com == "stone"):
                return None
            elif(Com == "paper"):
                return False
            elif(Com == "scissor"):
                return True
        elif (You == "paper"):
            if(Com == "stone"):
                return True
            elif(Com == "paper"):
                return None
            elif(Com == "scissor"):
                return False
        elif(You == "scissor"):
            if(Com == "stone"):
                return False
            elif(Com == "paper"):
                return True
            elif(Com == "scissor"):
                return None

    a = Game(Com_Input, Human)
    if (a == True):
        result = "You are the Winner"
    elif(a == False):
        result = "You Loose"
    else:
        result = "The match is draw"

    # Printing result
    print("--------------------")
    Say(f"You Chose: {Human}")
    Say(f"Computer Choose: {Com_Input}")
    Say(result)
    print("--------------------")
    print("********************")
