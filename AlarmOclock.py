import datetime
from playsound import playsound

alarmHour = int(input("Hour: "))
alarmMinute = int(input("Minute: "))
amPm = str.upper((input("AM or PM: ")))

if amPm == "PM" and alarmHour <= 12 :
    alarmHour = alarmHour + 12

while True :
    if  alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute :
        print("Събуди се!")
        playsound('C:\\Users\\Ivona\\Pictures\\Downloads\\alarm.mp3')
        break
