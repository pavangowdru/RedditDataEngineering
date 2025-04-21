from praw import Reddit
from utils.constants import POST_FIELDS
import numpy as np
import pandas as pd
import os

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        print("Connected to Reddit API successfully.")
        return reddit
    except Exception as e:
        print(f"Error connecting to Reddit API: {e}")
        return None
    
def extract_posts(reddit_instance, subreddit_name, time_filter='day', limit=None):
    try:
        
        subreddit = reddit_instance.subreddit(subreddit_name)

        posts_list = []

        if time_filter == 'day' or time_filter == 'week' or time_filter == 'month' or time_filter == 'year':
            posts = subreddit.top(time_filter, limit=limit)

            for post in posts:
                post_dict = vars(post)
                print(post_dict)
                post = {key: post_dict[key] for key in POST_FIELDS}
                posts_list.append(post)

        else:
            raise ValueError("Invalid time filter. Use 'day', 'week', 'month', or 'year'.") 
        
        return posts_list
    
    except Exception as e:
        print(f"Error extracting posts: {e}")
        return None
    
def transform_posts(posts_df : pd.DataFrame) -> pd.DataFrame:
    try:
        #posts_df['created_utc'] = pd.to_datetime(posts_df['created_utc'], unit='s')
        #posts_df.over_18 = np.where((posts_df.over_18==True), 1, 0)
        posts_df['author'] = posts_df['author'].astype(str) 

        return posts_df
    
    except Exception as e:
        print(f"Error transforming posts: {e}")
        return None

def load_data_to_csv(df: pd.DataFrame, path: str) -> None:
    try:
        # if not os.path.exists(path):
        #     os.makedirs(path)

        if df is not None:
            df.to_csv(path, index=False)
            print(f"Data loaded to {path} successfully.")
        else:
            logging.info("No data to write to CSV.")        
    except Exception as e:
        print(f"Error loading data to CSV: {e}")
