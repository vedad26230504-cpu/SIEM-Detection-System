import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body):
    sender_email = "senders_emailid"
    receiver_email = "receivers_emailid"
    password = "Google_2FA_16digit_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")

    except Exception as e:
        print("Error:", e)
