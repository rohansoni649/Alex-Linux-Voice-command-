import speech_recognition as sr
import webbrowser
import pyttsx3
pyttsx3.speak("Welcome to my tools")
#ch = input()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("start saying!!")
    audio=r.listen(source)
    print("speech done!!")

ch1 = r.recognize_google(audio)
print(ch1)
if "alex" in ch1 or "Alex" in ch1:
	print("tell me ur requirements : ",end='')
	s = sr.Recognizer()
	with sr.Microphone() as source:
    		print("start saying!!")
    		audio=s.listen(source)
    		print("speech done!!")

	ch2 = s.recognize_google(audio)
	if "date" in  ch2:
    		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=date")
	elif "cal" in ch2:
    		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=cal")
	elif ("list" and "contents") in ch2 or ("show" and "contents") in ch2:
    		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=ls")
	elif ("current" or  "directory") in ch2:
		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=pwd")
	elif ("running" or  "docker" or "containers") in ch2:
		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=sudo+docker+ps")
	elif ("run" or  "docker" or "container") in ch2:
		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=sudo+docker+run+-dit+centos")
	elif ("show" and  "images") in ch2 or ("container" or "docker") in ch2:
		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=sudo+docker+images")
	elif "show" and ("IP" or "address") in ch2:
		webbrowser.open("http://192.168.43.65/cgi-bin/command.py?q=ifconfig+enp0s3")
	else:
    		print("Coudn't undertand")
else:
	print("please speak the name correctly....")
