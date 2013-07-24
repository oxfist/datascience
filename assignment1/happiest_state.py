import sys
import json
from operator import itemgetter

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
    tweet_sentiment = 0
    terms = tweet["text"].split()
    for term in terms:
        if term in scores:
            tweet_sentiment += scores[str(term).lower()]
    return tweet_sentiment

def states_sentiment(tweets, scores):
    states = {}
    for tweet in tweets:
        if "delete" in tweet.keys() or tweet["place"] is None:
           continue
        if tweet["place"]["country_code"] == "US" :
            sentiment = derive_sentiment(tweet, scores)
            state = tweet["place"]["full_name"][-2:]
            states[state] = states.get(state, 0) + 1
    return states

def get_happiest_state(states):
    print sorted(states.iteritems(), key=itemgetter(1), reverse=True)[0][0]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = read_scores(sent_file)
    tweets = read_tweets(tweet_file)
    sent_file.close()
    tweet_file.close()
    states = states_sentiment(tweets, scores)
    get_happiest_state(states)

if __name__ == '__main__':
    main()