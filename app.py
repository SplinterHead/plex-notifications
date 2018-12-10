import os
import time
import base64
import shutil
import random
import string
import urllib.request
import datetime
from plexapi.server import PlexServer

notification_period = 7 # days
base_url = 'http://<IP ADDRESS>:32400'
token = 'API_TOKEN'
image_path = 'images'


def date_to_epoch(timestamp):
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(str(timestamp), pattern)))
    return epoch


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    "’": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
}

# def randomword(length):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(length))


today = datetime.date.today()
notification_date = today - datetime.timedelta(days=notification_period)
notification_epoch = date_to_epoch("%s 00:00:00" % notification_date)


if os.path.exists(image_path):
    shutil.rmtree(image_path, ignore_errors=True)

if not os.path.exists(image_path):
    os.makedirs(image_path)

plex = PlexServer(base_url, token)
recent = plex.library.recentlyAdded()

recent_items = []
for video in recent:
    if video.type == "movie" and date_to_epoch(video.addedAt) > notification_epoch:
        recent_item = {}
        urllib.request.urlretrieve(video.thumbUrl, "%s/poster.jpeg" % image_path)
        #movie_data = plex.library.section('Movies').get(video.title)
        with open("%s/poster.jpeg" % image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        recent_item['title'] = video.title
        #recent_item['year'] = movie_data.year
        recent_item['poster_base64'] = encoded_string.decode('utf-8')
        recent_items.append(recent_item)

f = open("plex_email.html", "w+")
f.write("<html><body style=\"font-family:sans-serif;\"><table>")
for item in recent_items:
    f.write("<tr><td><img src=\"data:image/png;base64,%s\" height=\"450px\" width=\"300px\"/></td>" % item['poster_base64'])
    f.write("<td valign=\"top\"><h2>%s</h2></td></tr>\n" % item['title'])
f.write("</table></body></html>")
