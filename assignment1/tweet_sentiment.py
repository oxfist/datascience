import sys
import json

def read_scores(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def read_tweets(file):
    tweets = []
    for line in file:
        tweets.append(json.loads(line))
    return tweets

def derive_sentiment(tweets, scores):
    for tweet in tweets:
        if "delete" in tweet.keys():
           continue
        tweet_sentiment = 0
        terms = tweet["text"].split()
        for term in terms:
            if term in scores:
                tweet_sentiment += scores[str(term).lower()]
        print tweet_sentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = read_scores(sent_file)
    tweets = read_tweets(tweet_file)
    sent_file.close()
    tweet_file.close()
    derive_sentiment(tweets, scores)

if __name__ == '__main__':
    main()