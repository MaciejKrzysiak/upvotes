import os
import sys
import praw

def main():
    submission = reddit.submission("8dmv8z")
    print(submission)

if __name__ == "__main__":

    f = open(
        "super_secret.json",
    )

    data = json.load(f)
    secret_key = data["secret_key"]

    reddit = praw.Reddit(
        client_id = data["client_id"],
        client_secret = data["client_secret"],
        password = data["password"],
        user_agent = data["user_agent"],
        username = data["username"],
    )

    opts = None
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "h",
            [
                "help",
            ],
        )
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            help()
            sys.exit()
        #elif opt in ("-s", "--source"):

    main()