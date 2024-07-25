import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Email details
smtp_server = 'ms.dolmengroup.com'
smtp_port = 587
smtp_username = 'riaz.haq@dolmengroup.com'
smtp_password = 'SeaKing99'

# Sender and CC email addresses
from_email = 'riaz.haq@dolmengroup.com'
cc_emails = ['riaz.haq@dolmengroup.com', 'amjad.ali@dolmengroup.com']

# List of recipients
to_emails = [
    'amjad.ali@dolmengroup.com',
    'rahat.ali@dolmengroup.com'
]

# Email subject and body
subject = 'Request for Email Domain Information to Enhance Security'
body = '''Dear DREM Team,

We hope this message finds you well.

To better protect your email experience and enhance our security measures against spam, we are increasing our email security protocols. As part of this process, we need your assistance to identify the domains from which you frequently receive emails.

Could you please provide us with a list of the email domains you often receive emails from? This information will allow us to whitelist these domains, ensuring that you continue to receive important emails without interruption.

Your cooperation in this matter is highly appreciated and will help us provide you with a more secure and efficient email service.

Thank you for your support.

Shaikh Riaz | Assistant Manager | Infrastructure Specialist
DOLMEN Real Estate Management (Pvt.) Ltd.
5th Floor, Dolman City, Clifton, Karachi.
Tel - +92 307-3869042, Ext. 131 | Fax - +92 3529-7680
Email: riaz.haq@dolmengroup.com
'''

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Secure the connection
server.login(smtp_username, smtp_password)

# Loop through each recipient and send the email
for to_email in to_emails:
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = ', '.join(cc_emails)
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Convert the message to a string and send it
    server.sendmail(from_email, [to_email] + cc_emails, msg.as_string())
    print(f'Email sent to {to_email}')

# Terminate the SMTP session and close the connection
server.quit()