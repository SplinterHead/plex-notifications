import random
import smtplib
# from subprocess import Popen, PIPE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

header_messages = [
    "Now Showing",
    "Looking for inspiration?",
    "Hot from the theatre!",
    "Don't know what to watch?"
]

# Use this list to block sending emails to certain users
user_blacklist = []


def send_email(defaults, server_name, recipients):
    for person in recipients:
        print("Evaluating %s" % person)

        if person in user_blacklist:
            print("- User in blacklist, not sending")
        else:
            print("- User not in blacklist, continuing")
            smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(defaults['gmail_addr'], defaults['gmail_pass'])

            msg = MIMEMultipart('alternative')
            msg["From"] = 'Plex %s <%s>' % (server_name, defaults['gmail_addr'])
            msg["To"] = person
            msg["Subject"] = random.choice(header_messages)
            msg.preamble = "See what's been added to Plex this week"
            msg.add_header('Content-Type', 'text/html')

            text_msg = MIMEText("See what's been added to Plex this week", 'plain', 'utf-8')
            html_msg = MIMEText(open('plex_email.html', 'r').read(), 'html', 'utf-8')

            msg.attach(text_msg)
            msg.attach(html_msg)

            smtp.send_message(msg)
            smtp.quit()
