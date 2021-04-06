# upvotes

Create live Reddit submissions that update in response to comments, upvotes, score, etc.

## Tools

* PRAW (Python Reddit API Wrapper) - [PRAW](https://praw.readthedocs.io/en/latest/)

## Installation

Easiest way to install is using Git via the command line. 

You can install git here: [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Once installed, run via your terminal:

```
$> git clone https://github.com/MaciejKrzysiak/upvotes.git
$> cd upvotes
```

Once downloaded and inside the upvotes directory, update super_secret.json to use your credentials. 

A personal client_id and client_secret can be created here: [Reddit Dev](https://www.reddit.com/prefs/apps). 

The username and password fields correspond to your Reddit account information. 

The user_agent field is a way to name your program. Give it an informative name. 

Once you've updated the secret fields, update the submission_id in upvotes.py. 
The submission id refers to the literal Reddit post you want to turn live. 
This id can be found in the url of the post. It's about 5 characters long.

Then run via your terminal:
```
$> python3 upvotes.py
```
If you do not have python3 installed, see here: [Python](https://realpython.com/installing-python/).

## Tips

The sleep_interval field in upvotes.py is set to about 15 seconds. This means the program updates the Reddit post every 15 seconds.
You can speed this up or slow it down. Just be careful not to get throttled by the Reddit API.
