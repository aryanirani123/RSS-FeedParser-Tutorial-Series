"""
Introduction to RSS FeedParser
 url for parsing: https://timesofindia.indiatimes.com/rssfeedstopstories.cms

"""

from email.feedparser import FeedParser
import feedparser
url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

newsfeed = feedparser.parse(url)
entry = newsfeed.entries[0]
#print(entry.keys())

print("Post Title: ",entry.title)
print("Post Link: ", entry.link)
