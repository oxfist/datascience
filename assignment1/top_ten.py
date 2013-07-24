import sys
import json
from operator import itemgetter

def read_tweets(file):
    tweets = []
    for line in file:
        tweets.append(json.loads(line))
    return tweets

def compute_hashtags_sum(tweets):
    sums = {}
    for tweet in tweets:
        if "delete" in tweet.keys():
            continue
        hashtags = tweet["entities"]["hashtags"]
        for hashtag in hashtags:
            sums[hashtag["text"]] = sums.get(hashtag["text"], 0.0) + 1
    return sums

def sort_by_sum(sums):
    return sorted(sums.iteritems(), key=itemgetter(1), reverse=True)

def print_hashtags(hashtags):
    i = 1
    for (hashtag, count) in hashtags:
        if i > 10:
            break
        print hashtag, count
        i += 1

def main():
    tweet_file = open(sys.argv[1])
    tweets = read_tweets(tweet_file)
    tweet_file.close()
    sums = compute_hashtags_sum(tweets)
    hashtags = sort_by_sum(sums)
    print_hashtags(hashtags)    

if __name__ == '__main__':
    main()