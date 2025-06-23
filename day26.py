

# ------------------------> amazing feature of python <--------------------------------------


# multiline printing statement:  use ''' '''

print(''' 
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch localhost",
            "type": "firefox",
            "request": "launch",
            "reAttach": true,
            "url": "http://localhost/index.html", 
            "webRoot": "${workspaceFolder}"
        }
    ]
}
''') # print random script


# text to speech by : pyttxs3 module
import pyttsx3
engine=pyttsx3.init()              # type: ignore
engine.say("jarvis activated, how can i assist you") # type: ignore
engine.runAndWait()                # type: ignore
             


