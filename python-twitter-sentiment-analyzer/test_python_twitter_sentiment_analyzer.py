import TwitterClient


def test_main():

    # creating object of TwitterClient Class
    api = TwitterClient.TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '@sudeephazra', count = 200)

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

    positive_mentions = ""
    negative_mentions = ""

    for tweet in positive[:10]:
        positive_mentions += tweet['text'] +  "\n"

    for tweet in negative[:10]:
        negative_mentions += tweet['text'] +  "\n"

    negativeComments = negative_mentions
    negativeCount = len(negative)
    postiveComment= positive_mentions
    postiveCount =len(positive)
    totalCount =len(tweets)
    neutralCount =len(tweets) - len(negative) - len(positive)

    print("Call is made with %d positive, %d neutral and %d negative tweets out of %d tweets" % (postiveCount, neutralCount, negativeCount, totalCount))

if __name__ == "__main__":
# calling main function
    test_main()