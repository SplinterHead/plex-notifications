import random
import smtplib
# from subprocess import Popen, PIPE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

header_messages = [
    "Now Showing:",
    "Looking for Inspiration?",
    "Hot from the theatre!",
]


def send_email(defaults, server_name):
    smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(defaults['gmail_addr'], defaults['gmail_pass'])

    msg = MIMEMultipart('alternative')
    # msg["From"] = 'Plex %s <%s>' % (server_name, defaults['gmail_addr'])
    msg["From"] = defaults['gmail_addr']
    msg["To"] = 'lewis2004@hotmail.com'
    msg["Subject"] = random.choice(header_messages)
    # msg["Preamble"] = "See what's been added to Plex this week"
    msg.preamble = "See what's been added to Plex this week"
    msg.add_header('Content-Type', 'text/html')

    text_msg = MIMEText("See what's been added to Plex this week", 'plain')
    html_msg = MIMEText(open('plex_email.html', 'r').read(), 'html')

    msg.attach(text_msg)
    msg.attach(html_msg)

    smtp.send_message(msg)
    smtp.quit()
