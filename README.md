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

For this to work, the Plex server needs to be available externally. This can be done by following the instructions on the 
[Plex Website](https://support.plex.tv/articles/200289506-remote-access/)

#### Environment Variables

**There is an example script called `run.sh` which will speed up the set up of the env vars, sourcing the virtualenv and running the tool**

First, we need to know about the server that this tool will run against

```bash
# Plex credentials
export PLEX_URL=""  # External Plex server address and port (eg. http://my.plex.server:32400)
export PLEX_USER="" # Plex admin user username
export PLEX_PASS="" # Plex admin user password
```

Now that the Gmail account is sorted, the credentials for that and the Plex server itself need to be added to the environment

Set two environment variables

```bash
# Gmail credentials
export GMAIL_USERNAME="" # Gmail address
export GMAIL_PASSWORD="" # Gmail password
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
- [ ] Only send emails if new items have been added
- [x] Fully document tool
- [x] Pull the user list from the server API
- [ ] User white/black lists
- [ ] Convert tool to a full plugin
- [ ] Make all the options (inc. library name) configurable
- [ ] Allow multiple libraries
- [ ] Link to item in Plex (?)
