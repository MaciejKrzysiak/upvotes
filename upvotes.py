import time
import json
import praw

sleep_interval = 15


def main():

    # Submission IDs can be found in the url to your post. They are 6 characters long.
    submission = reddit.submission("Your Submission ID Here")

    # Sort by most upvoted/downvoted comments.
    upvoted_submission_comments = sorted(
        submission.comments, key=lambda x: x.score, reverse=True
    )
    downvoted_submission_comments = sorted(submission.comments, key=lambda x: x.score)

    edited_body = f"Number of Comments: {submission.num_comments} \n\n Number of Updoots: {submission.score} \n\n Updoot Ratio: {submission.upvote_ratio} \n\n The 5 Most Upvoted Comments:\n\n"

    for comment in upvoted_submission_comments[0:5]:
        edited_body = edited_body + f"'{comment.body}',\n\n"

    edited_body = edited_body + "The 5 Most Downvoted Comments: \n\n"
    for comment in downvoted_submission_comments[0:5]:
        edited_body = edited_body + f"'{comment.body}',\n\n"

    # Update body of submission.
    submission.edit(edited_body)

    print(submission.comments.list())


if __name__ == "__main__":

    # Place all your private information in this file.
    f = open(
        "super_secret.json",
    )

    data = json.load(f)

    # Authenticate with the Reddit API.
    # client_id and client_secret pertain to the id and secret given by Reddit to a developer.
    # Obtain yours here: https://www.reddit.com/prefs/apps
    # Password and username refer to your reddit account information.
    # User agent is just a way to name your app.
    reddit = praw.Reddit(
        client_id=data["client_id"],
        client_secret=data["client_secret"],
        password=data["password"],
        user_agent=data["user_agent"],
        username=data["username"],
    )

    # Check that we are actually logged in.
    try:
        reddit.user.me()
    except Exception as e:
        print("Failed to authenticate. Double check your id, passwords, etc.")
        print(e)

    # Infiite loop that edits our Reddit submission every sleep_interval seconds.
    # Be careful not to get throttled by Reddit.
    while True:
        i = 0
        print(f"editing run {i}...")
        i = i + 1
        main()
        print("sleeping...")
        time.sleep(sleep_interval)
