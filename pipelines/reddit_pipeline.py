from etls.reddit_etls import connect_reddit, extract_posts, transform_posts, load_data_to_csv
from utils.constants import REDDIT_CLIENT_ID, REDDIT_SECRET, OUTPUT_PATH
import pandas as pd

def reddit_pipeline(filename: str, subreddit: str, time_filter='day', limit=None) :
    #connecting to reddit instance
    isinstance = connect_reddit(REDDIT_CLIENT_ID, REDDIT_SECRET, "etl_script by u/Forsaken-Sundae2712")
    #extraction
    posts = extract_posts(isinstance, subreddit, time_filter, limit)
    #transformation
    transformed_posts = pd.DataFrame(posts)
    transformed_posts = transform_posts(transformed_posts)
    
    #loading
    file_path = f'{OUTPUT_PATH}/{filename}.csv'
    load_data_to_csv(transformed_posts, file_path)

    return file_path
