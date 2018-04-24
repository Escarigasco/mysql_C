import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# from backports import configparser
import configparser


class email_sender(object):
    def send(self, target, info):
        subject = 'Your requested Data'
        config = configparser.ConfigParser()

        config.read("path/to/file")
        # target = config.get("configuration", target)
        sender = config.get("configuration", "sender")
        password = config.get("configuration", "password")
        user_name = config.get("configuration", "user_name")
        server = config.get("configuration", "server")
        port = config.get("configuration", "port")
        print(target)
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = str(target)

        txt = MIMEText(info)
        msg.attach(txt)

        filepath = 'path/to/file'
        with open(filepath, 'rb') as f:
            img = MIMEImage(f.read(), 'csv')

        img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filepath))
        msg.attach(img)

        server = smtplib.SMTP(server, port)
        print("connection established")
        server.starttls()
        server.login(user_name, password)
        server.sendmail(sender, target, msg.as_string())
        print("email sent")
        server.quit()


if __name__ == "__main__":
    test = email_sender()
    target = "email@address.com"
    info = "test content"
    test.send(target, info)
