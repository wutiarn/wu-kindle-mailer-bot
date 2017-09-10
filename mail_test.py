import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Привет мир")
msg["Subject"] = "Testing python"
msg["From"] = "me@wutiarn.com"
msg['To'] = "wutiarn@gmail.com"

s = smtplib.SMTP_SSL("smtp.yandex.ru")
s.login("me@wutiarn.com", "")
s.sendmail("me@wutiarn.com", "wutiarn@gmail.com", msg.as_string())
s.close()
