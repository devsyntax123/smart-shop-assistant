import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import logger

def send_email(recipient_email, subject, body):
    """Send an email dynamically using SMTP."""
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "keshtya.kesh@gmail.com"
    sender_password = "bhzj gbmj pwul ijap"

    try:
        # Create email content
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add the email body
        message.attach(MIMEText(body, 'html'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Login to the server
            server.send_message(message)  # Send the email
            logger.info(f"Email sent successfully to {recipient_email}.")

    except Exception as e:
        logger.info(f"Failed to send email: {e}")
