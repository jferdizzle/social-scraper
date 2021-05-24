import twint


def scrape_twitter(search_term, since):
    # Configure
    c = twint.Config()
    c.Search = search_term
    c.Since = since
    c.Store_csv = True
    c.Output = "twitter_scrapes/tweets_since_%s.csv" % since
    c.Hide_output = True
    c.Stats = True

    # Run
    twint.run.Search(c)


