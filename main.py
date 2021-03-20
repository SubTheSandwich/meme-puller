import praw
import random

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
)



memesubreddits = ['memes', 'dankmemes', 'funny']

chosensubreddit = random.choice(memesubreddits)
subreddit = reddit.subreddit(chosensubreddit)

meme = subreddit.hot(limit=10)

List = []

for submission in meme:
    if submission.is_self != True:
        List.append(submission)

random_post = random.choice(List)

print(random_post.url)
