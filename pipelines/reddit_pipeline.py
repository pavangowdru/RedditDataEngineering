from etls.reddit_etls import connect_reddit, extract_posts, transform_posts, load_to_csv
from utils.constants import CLIENT_ID, SECRET, USER_AGENT, OUTPUT_PATH
import pandas as pd

def reddit_pipeline(filename: str, subreddit: str, time_filter='day', limit=None) :
    #connecting to reddit instance
    isinstance = connect_reddit(CLIENT_ID, SECRET, USER_AGENT)
    #extraction
    posts = extract_posts(isinstance, subreddit, time_filter, limit)
    #transformation
    transformed_posts = pd.DataFrame(posts)
    transformed_posts = transform_posts(transformed_posts)
    
    #loading
    #load_to_database(transformed_posts, filename)
    load_to_csv(transformed_posts, OUTPUT_PATH)
