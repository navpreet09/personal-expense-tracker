# Sends summary email using SendGrid API
# External service may fail, so exceptions are handled to prevent app crash. Email content is simple text for compatibility.
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

class EmailService:

    def send_summary(self, email, summary_text):

        message = Mail(
            from_email='gillnavpreetkaur8@gmail.com',
            to_emails=email,
            subject='Expense Summary',
            plain_text_content=summary_text
        )

        try:
            sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            response = sg.send(message)
            print("Email sent. Status code:", response.status_code)

        except Exception as e:
            print(e)