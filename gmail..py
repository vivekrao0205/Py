import smtplib
from email.message import EmailMessage

sender_email = input("Enter your email: ")
receiver_email = input("Enter receiver's email: ")

subject = input("Enter subject: ")
message = input("Enter message: ")

msg = EmailMessage()
msg.set_content(message)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 25)
    server.starttls()
    # Replace the placeholders with your actual email and password
    server.login(sender_email, input("Enter your password: "))
    server.send_message(msg)
    print("Email has been sent to " + receiver_email)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()
