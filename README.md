# Plex Notifications

Plex Notifications is a tool to send regular updates to the people you share your Plex server with about what has been 
recently added. 

The tool will find all the new items in a single library section and format their data into an email that can also be 
automatically distributed 

![Email Sample](docs/images/email_covershot.png?raw=true "Email Sample")

## Setup

#### GMail account

First, a Gmail account will be needed for this to work - it is recommended to set up a new account specifically or this, or
for all system related messaging, due to security requirements.

[Go ahead and create one here](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp)

#### Environment Variables

Now that the Gmail account is sorted, the credentials for that and the Plex server itself need to be added to the environment

Set two environment variables

## To Do

- [x] Get Plex server credentials from environment variables
- [ ] Fully document tool
- [ ] Pull the user list from the server API
- [ ] User white/black lists
- [ ] Convert tool to a full plugin
- [ ] Make all the options (inc. library name) configurable
- [ ] Allow multiple libraries
- [ ] Link to item in Plex (?)
