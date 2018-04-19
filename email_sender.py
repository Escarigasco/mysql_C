# import the smtplib module. It should be included in Python by default
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import configparser
# set up the SMTP server


class email_sender(object):
    def send(self, target):
        # target = 'federico.zarelli@aol.com'
        config = configparser.ConfigParser()
        config.read("path/to/file")
        sender = config.get("configuration", "sender")
        password = config.get("configuration", "password")
        user_name = config.get("configuration", "user_name")
        server = config.get("configuration", "server")
        port = config.get("configuration", "port")

        msg = MIMEMultipart()
        msg['Subject'] = 'I have a picture'
        msg['From'] = sender
        msg['To'] = target

        txt = MIMEText('I just bought a new camera.')
        msg.attach(txt)

        filepath = 'path/to/file'
        with open(filepath, 'rb') as f:
            img = MIMEImage(f.read(), 'file_extension')

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
    target = "recipiens_address"
    test.send(target)
