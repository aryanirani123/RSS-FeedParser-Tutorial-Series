"""
Advanced FeedParser for Medium 
url to be used : https://aryanirani123.medium.com/feed
Use the datetime library for getting blogs between 
a specific times

"""


from datetime import date, datetime
from email import feedparser
import feedparser

url = "https://aryanirani123.medium.com/feed"
blog_feed = feedparser.parse(url)
content = blog_feed.entries

#print(blog_feed.entries[0].published)



compare_blog_time = "2022-05-01 7:18:01"
#print(type(compare_blog_time))
format = "%Y-%m-%d %H:%M:%S"

changed_compare_time = datetime.strptime(compare_blog_time,format)
#print(type(changed_compare_time))

new_format = "%a, %d %b %Y %H:%M:%S %Z"

for blog in content:
    
    if datetime.strptime(blog.published,new_format) > changed_compare_time:
        print(blog.title)
        print(blog.published)
    

