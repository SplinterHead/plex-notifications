# Plex Notifications

Plex Notifications is a tool to send regular updates to the people you share your Plex server with about what has been 
recently added. 

This has been built on pkkid's awesome work on the [python-plexapi](https://github.com/pkkid/python-plexapi)

The tool will find all the new items in a single library section and format their data into an email that can also be 
automatically distributed 

![Email Sample](docs/images/email_covershot.png?raw=true "Email Sample")

## Setup

#### GMail account

First, a Gmail account will be needed for this to work - it is recommended to set up a new account specifically or this, or
for all system related messaging, due to security requirements.

[Go ahead and create one here](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp)

#### Plex server Remote Access

For these emails to work, the Plex server needs to be available externally. This can be done by following the instructions on the
[Plex Website](https://support.plex.tv/articles/200289506-remote-access/)

#### Configuration File

Inputs to this tool are set up in the `plex-notifications.ini` configuration file. Fill in the fields in the supplied file

```
[general]
NOTIFICATION_PERIOD     # Number of days to look back into library history
EMAIL_BLACKLIST         # List of users' emails that do not want to get emails

[plex]
PLEX_URL                # External URL (with port) to the Plex Server
PLEX_USER               # Admin Plex username
PLEX_PASS               # Admin Plex user password

[gmail]
GMAIL_USERNAME          # Email address of the GMail account
GMAIL_PASSWORD          # Password for the GMail account
```


#### Dependencies

It is recommended to install all the required libraries in a virtualenv to keep your system clean. 

```bash
virtualenv venv -p $(which python3)
source venv/bin/activate
```

From there, install the libraries

`pip install plexapi`

#### Crontab

In it's current state, the tool will need to be run as part of a crontab timer to get regular updates. Future improvements 
could move this to a Plex plugin and use a better scheduling system. Please add the tool or it's `run.sh` to the crontab 
for a user with access to Plex

```bash
crontab -e

# Then add something like this
0 19 * * 5 /path/to/run.sh # Fires every Friday night at 7pm
```

## To Do

- [x] Get Plex server credentials from environment variables
- [x] Only send emails if new items have been added
- [x] Fully document tool
- [x] Pull the user list from the server API
- [x] User white/black lists
- [ ] Make all the options (inc. library name) configurable
- [ ] Allow multiple libraries
- [ ] Convert tool to a full plugin
- [ ] Link to item in Plex (?)
