import cv2
from pyzbar.pyzbar import decode

def notify():

    import time
    from plyer import notification
    notification.notify(
        title=f"{data} Attended",
        message= f"Time : {time.ctime()}",
        app_icon="notify.ico",
        timeout=2)

def mail():

    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg["Subject"] = "Attendance Registered Successfully"
    msg["From"] = "goosezenv@gmail.com"
    msg["To"] = "zenvindia@gmail.com"

    import time
    msg.set_content(f"I'm Authsys,\nData:\nRollno - {data}\nTime - {time.ctime()}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("goosezenv@gmail.com", "test1234test")
        smtp.send_message(msg)
        smtp.close()

def writeentry():

    import time
    with open("entrys.txt", "a") as f:
        f.write(f"{data} - {time.ctime()}\n")
        f.close()

def restart():

    import sys
    print("Argv was",sys.argv)
    print("Executable was", sys.executable)
    print("Restarting...")

    import os
    os.execv(sys.executable, ['python'] + sys.argv) 

def auth():

    from playsound import playsound
    print(f"Authorized - {data}")
    notify()
    playsound("auth.mp3")
    writeentry()
    mail()

def unauth():

    from playsound import playsound
    print(f"Unauthorized - {data}")
    playsound("unauth.mp3")

if __name__ == '__main__':

    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    capture.set(3,640)
    capture.set(4,480)

    with open('allowlist.txt') as f:
        lock = f.read()

    while (True):
        ret, frame = capture.read()
        for qrcode in decode(frame):
            data = qrcode.data.decode("utf-8")
            if data == lock:
                cv2.destroyAllWindows()
                auth()
                restart()
            else:
                cv2.destroyAllWindows()
                unauth()
                restart()

        cv2.imshow('window', frame)
        if cv2.waitKey(30) == ord('q'):
            break