import feedparser
import datetime
import time
from time import mktime

def pub_date(x):
    return x.published_parsed

def parse_feeds(url1, url2):
    feed1 = feedparser.parse(url1) 
    feed2 = feedparser.parse(url2)
    an_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
    recent_posts = [entry for entry in feed1.entries if datetime.datetime.fromtimestamp(mktime(entry.updated_parsed)) > an_hour_ago]
    recent_posts += [entry for entry in feed2.entries if datetime.datetime.fromtimestamp(mktime(entry.updated_parsed)) > an_hour_ago]
    # the above lambdas filter by time updated to show only items from last hour

    recent_posts.sort(key=lambda x: x.updated)
    recent_posts.sort(key=pub_date)

    
   # recent_posts.strftime(key=lambda x: x.strftime(x.published_parsed))
 
    for post in recent_posts:
        print("(", post.published_parsed.strftime(), ") ", '\n', "   TITLE: ", post.title, '\n', "      LINK: ", post.link, " ", sep= "")
    print("done")


#def time_sort_posts(posts=posts, )




if __name__ == '__main__':
  parse_feeds('https://www.sciencedaily.com/rss/top/technology.xml',  'https://www.wired.com/feed/category/gear/latest/rss')



    
    