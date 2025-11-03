import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "Taguette Team <no-reply@taguete.com>"
recipient_email = "john@gmail.com"
subject = "Password Expired"

body = """\
Hello,

Your password will expire soon!
We require you to update it to maintain access to your account. 
Please update your password as soon as possible — otherwise, your account may be deactivated.

We’ll send you a link shortly to complete the password update process.

Best regards,
The Taguette Team
"""

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

# Connect to MailHog SMTP server
with smtplib.SMTP("localhost", 1025) as server:
    server.send_message(msg)

print("Email sent!")
