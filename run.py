import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol

def ret_email(dbfile):

    import sqlite3
    connection = sqlite3.connect(dbfile)
    cursor = connection.cursor()
    cursor.execute(f"SELECT student_email FROM student WHERE student_rollno='{data}'")
    records = cursor.fetchall()
    db_email = str(records[0]).strip("(,)").strip("'").strip("''")
    connection.close()
    return db_email

def process_notification():

    import time
    from plyer import notification
    notification.notify(
        title=f"{data} Attended",
        message= f"Time : {time.ctime()}",
        app_icon="notify.ico",
        timeout=2)

def process_entry():

    import time
    with open("entrys.txt", "a") as f:
        f.write(f"{data} - {time.ctime()}\n")
        f.close()

def process_mail():

    import time
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg["Subject"] = "Attendance Registered Successfully"
    msg["From"] = "goosezenv@gmail.com"
    msg["To"] = "{0}".format(ret_email("bennett.db"))
    msg.set_content(f"I'm Authsys,\nData:\nRollno - {data}\nTime - {time.ctime()}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("goosezenv@gmail.com", "test1234test")
        smtp.send_message(msg)
        smtp.close()

def process_auth():

    from playsound import playsound
    print(f"Authorized - {data}")
    process_notification()
    playsound("auth.mp3")
    process_entry()
    process_mail()

def process_unauth():

    from playsound import playsound
    print(f"Unauthorized - {data}")
    playsound("unauth.mp3")

def process_restart():

    import os
    import sys
    print("Restarting...")
    os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == '__main__':

    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    capture.set(3,640)
    capture.set(4,480)

    with open('allowlist.txt') as f:
        lock = f.read()

    while (True):
        ret, frame = capture.read()
        for qrcode in decode(frame, symbols=[ZBarSymbol.QRCODE]):
            data = qrcode.data.decode("utf-8")
            if data in lock:
                cv2.destroyAllWindows()
                process_auth()
                process_restart()
            else:
                cv2.destroyAllWindows()
                process_unauth()
                process_restart()

        cv2.imshow('AuthSys Scanning', frame)
        if cv2.waitKey(1) == ord('q'):
            break