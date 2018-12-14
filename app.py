import time
import datetime
from plexapi.server import PlexServer

notification_period = 7  # days
base_url = 'http://<SERVER_ADDRESS>:32400'
token = '<PLEX TOKEN>'


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
    "–": "&ndash;"
}

today = datetime.date.today()
notification_date = today - datetime.timedelta(days=notification_period)
notification_epoch = date_to_epoch("%s 00:00:00" % notification_date)

plex = PlexServer(base_url, token)
recent = plex.library.recentlyAdded()

recent_items = []
for video in recent:
    if video.type == "movie" and date_to_epoch(video.addedAt) > notification_epoch:
        recent_item = {}
        recent_item['title'] = video.title
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



