import tweepy

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_sec = 'xxx'


def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_sec)
    return tweepy.API(auth)


def collect_tweets(keyword, stop_num):
    keyword = keyword.strip()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword, limit=stop_num)
    show_content(tweets)

def stalker(victim, no):
    "This will find a certain number of tweets from our victim"
    tweets = twitter.user_timeline(screen_name=victim, count=no)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))


def show_content(tweets):
    for tweet in tweets:
        print("\n" + tweet.text)

def post_tweet(status):
    twitter.update_status(status=status)


def see_timeline(no):
    for tweet in tweepy.Cursor(twitter.home_timeline).items(no):
        print("\n {} tweeted by {}".format(tweet.text, tweet.user.name))


if __name__ == '__main__':

    twitter = authenticate()

    # If the authentication was successful, you should
    # see the name of the account print out
    print('You are now logged in as {}'.format(twitter.me().name))
    collect_tweets('#ShefCodeFirst', 10)

    # Retrieves a single tweet from our Twitter home time line
    # and wraps it in a special, "list-like" Cursor structure from
    # the tweepy library so that we can loop through it using a for-loop.
    for status in tweepy.Cursor(twitter.home_timeline).items(1):
        # Process a single status
    #     print(status._json)
    	print(status.text)

    #     # Saving the Json in a variable
    #     json_var = status._json

    # post_tweet('Tweeting from Python in a #ShefCodeFirst class! 🍕✨')
