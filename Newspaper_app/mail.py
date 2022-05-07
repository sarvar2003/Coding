import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email="from__email",
    to_emails="to__email__",
    subject="Cambridge Computer Science Admissions Updated",
    html_content="The admissions test information for cambridge has been updated"
)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    sg.send(message)
except Exception as e:
    print(e)