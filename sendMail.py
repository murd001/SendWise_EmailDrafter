import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, smtp_password, subject, html_body, recipients_filename):
    # Gmail SMTP configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Read recipient emails from CSV file
    recipients = []
    with open(recipients_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if exists
        recipients = [row[0] for row in reader if row]  # Extract email addresses from CSV rows

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, smtp_password)

        for recipient in recipients:
            # Create a new message for each recipient
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(html_body, 'html'))

            # Send the email to the current recipient
            server.sendmail(sender_email, recipient, message.as_string())