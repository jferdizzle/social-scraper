import sys
from twitter import scrape_twitter

if __name__ == "__main__":
    social_platform = sys.argv[1]
    if social_platform == 'twitter':
        search_term = sys.argv[2]
        since = sys.argv[3]

        scrape_twitter(search_term, since)
        print('Twitter Scrape Complete! Check the twitter_scrapes folder.')
    else:
        print('A %s scraper has not yet been implemented' % social_platform)