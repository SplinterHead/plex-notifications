import os
import time
import datetime
import emailer
from plexapi.server import PlexServer

defaults = {
    'base_url':   os.environ['PLEX_URL'],
    'token':      os.environ['PLEX_TOKEN'],
    'gmail_addr': os.environ['GMAIL_USERNAME'],
    'gmail_pass': os.environ['GMAIL_PASSWORD']
}
notification_period = 7  # days


def date_to_epoch(timestamp):
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(str(timestamp), pattern)))
    return epoch


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    '“': "&quot;",
    '”': "&quot;",
    "'": "&apos;",
    "’": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    "-": "&ndash;",
    "–": "&ndash;",
    "½": "&frac12;",
    "⅓": "&frac13;"
}

today = datetime.date.today()
notification_date = today - datetime.timedelta(days=notification_period)
notification_epoch = date_to_epoch("%s 00:00:00" % notification_date)

plex = PlexServer(defaults['base_url'], defaults['token'])
recent = plex.library.recentlyAdded()

recent_items = []
for video in recent:
    if video.type == "movie" and date_to_epoch(video.addedAt) > notification_epoch:
        recent_item = {}
        recent_item['title'] = "".join(html_escape_table.get(c, c) for c in video.title)
        #  This allows movie posters to be loaded
        recent_item['poster_url'] = video.thumbUrl.replace('https://', 'http://')
        recent_item['description'] = "".join(html_escape_table.get(c, c) for c in video.summary)
        recent_items.append(recent_item)

f = open("plex_email.html", "w+")
f.write('<html>\n  <head>\n    <style>\n%s\n    </style>\n  </head>' % open('email.css', 'r').read())
f.write('  <body>\n    <div class="content">\n      <h1>Now Streaming:</h1>')
for item in recent_items:
    #  Create a card for the movie
    f.write('        <div class="card">\n')
    # Start with the movie poster
    f.write('          <img class="poster" src="%s"  alt="%s movie poster"/>\n' % (item['poster_url'], item['title']))
    #  Add a <div> to hold the text-based data
    f.write('          <div class="info-cell">\n')
    #  Add the Title as a <h2>, and the movie summary
    f.write('            <h2>%s</h2>\n            %s\n' % (item['title'], item['description']))
    #  Wrap it up like a fajita
    f.write('          </div>\n')
    f.write('        </div>\n')
f.write('    </div>\n  </body>\n</html>')

print("Sending email")
# TODO: Get the server name from the API
emailer.send_email(defaults, 'plex-server')
print("Complete")
