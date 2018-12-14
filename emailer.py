import random
from subprocess import Popen, PIPE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

header_messages = [
    "Now Showing:",
    "Looking for Inspiration?",
    "Hot from the theatre!",
]

msg = MIMEMultipart('alternative')
msg["From"] = "<SENDER_EMAIL>"
msg["To"] = "<RECIPIENT_EMAIL>"
msg["Subject"] = random.choice(header_messages)
msg.preamble = "See what's been added to Plex this week"

html_msg = MIMEText(open('plex_email.html', 'r').read(), 'html')
msg.attach(html_msg)

p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
p.communicate(msg.as_bytes())