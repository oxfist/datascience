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

def derive_sentiment(tweet, scores):
    pos_sentiment = 0
    neg_sentiment = 0
    terms = tweet["text"].split()
    for term in terms:
        if term in scores:
        	sentiment = scores[str(term).lower()]
        	if sentiment >= 0:
        		pos_sentiment += 1
        	else:
        		neg_sentiment += 1
    if neg_sentiment == 0:
    	return 0
    else:
        return pos_sentiment / neg_sentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = read_scores(sent_file)
    tweets = read_tweets(tweet_file)
    sent_file.close()
    tweet_file.close()

    for tweet in tweets:
        tweet_sentiment = 0
        terms = tweet["text"].split()
        for term in terms:
            if term not in scores:
                print term, derive_sentiment(tweet, scores)

if __name__ == '__main__':
    main()