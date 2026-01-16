import snscrape.modules.twitter as sntwitter

for i, tweet in enumerate(
    sntwitter.TwitterSearchScraper("thales_ke").get_items()
):
    if i >= 10:
        break
    print(tweet.content)
