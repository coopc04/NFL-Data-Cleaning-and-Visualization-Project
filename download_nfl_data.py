import pandas as pd
import requests

def download_nfl_data(season):
    url = f"https://github.com/nflverse/nflfastR-data/raw/master/data/play_by_play_{season}.parquet"
    df = pd.read_parquet(url)
    df.to_csv(f"../data/play_by_play_{season}.csv", index = False)
    print(f"Data for {season} saved to /data folder.")
    
download_nfl_data(2025)