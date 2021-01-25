import pandas
import csv
import datetime
import json
from datetime import datetime

with open('E:\Data Analysis\FB_Posts_2016_2021_v2\posts\your_posts_1.json') as posts:
   data = json.load(posts)
curses = ["fuck", "shit", "asshole", "bullshit", "motherfucker", "bastard", "douchebag", "jackass", "fucker", "bitch", "damn", "hell"]
for posts in data:
    pkeys = posts.keys()
    trump = 'N'
    cursing = 'N'
    if "data" in pkeys:
        content = posts["data"]
        if not content:
            pass
        else:
            keys = content[0].keys()
            if "post" in keys:
                try:
                    date = datetime.fromtimestamp(posts["timestamp"])
                    status = content[0]["post"]
                    if "Trump" in status:
                        trump = 'Y'
                    if any(word in status for word in curses):
                        cursing = 'Y'
                    with open("post_2016_2021.csv", 'a', encoding='utf-8', newline='') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow([date,status,trump,cursing])
                except KeyError:
                    pass


