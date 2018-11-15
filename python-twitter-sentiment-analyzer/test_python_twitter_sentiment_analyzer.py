import TwitterClient


def test_main():

    # creating object of TwitterClient Class
    api = TwitterClient.TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '@realDonaldTrump', count = 200)

    if len(tweets) == 0:
        print('No tweets found')
        return
    '''
    Main function to fetch tweets and count them as per sentiment
    '''
    # picking positive tweets from tweets
    positive = [t for t in tweets if t['sentiment'] == 'positive']
    # picking negative tweets from tweets
    negative = [t for t in tweets if t['sentiment'] == 'negative']

    # positive_mentions = ""
    # negative_mentions = ""

    for tweet in positive[:10]:
        # positive_mentions += tweet['text'] +  "\n"
        print(tweet['text'])

    for tweet in negative[:10]:
        # negative_mentions += tweet['text'] +  "\n"
        print(tweet['text'])

    _negativeCount = len(negative)
    _positiveCount = len(positive)
    _totalCount = len(tweets)
    _neutralCount = len(tweets) - len(negative) - len(positive)

    print("Call is made with %d positive, %d neutral and %d negative tweets out of %d tweets" % (_positiveCount,
                                                                                                 _neutralCount,
                                                                                                 _negativeCount,
                                                                                                 _totalCount))


test_main()
