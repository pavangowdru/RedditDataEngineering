import praw

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='etl_script by u/Forsaken-Sundae2712'
)

print(reddit.read_only)  # should print: True (if connection is successful)

posts = reddit.subreddit('dataengineering').top('day', limit=1)

posts_list = []

POST_FIELDS = (
    'id',
    'title',
    'selftext',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'upvote_ratio',
    'over_18',
    'edited',
    'spoiler',
    'stickied',
)

for post in posts:
    post_dict = vars(post)
    #print(post_dict)
    post = {key: post_dict[key] for key in POST_FIELDS}
    posts_list.append(post)

print(posts_list)