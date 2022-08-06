"""
FeedParser for Medium 
url to be used : https://aryanirani123.medium.com/feed

"""

import feedparser

feed_url = "https://aryanirani123.medium.com/feed"

blog_feed = feedparser.parse(feed_url)

#Get the title of the website

website_title = blog_feed.feed.title

#print(website_title)

content = blog_feed.entries
#print(blog_feed.entries[0].title)
#print(blog_feed.entries[0].link)
#print(blog_feed.entries[0].published)


for blog in content:
    print(blog.title)
    print(blog.link)
    print(blog.published)
