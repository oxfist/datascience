import sys
import json

def read_tweets(file):
    tweets = []
    for line in file:
        tweets.append(json.loads(line))
    return tweets

def compute_totals(tweets):
    sums = {}
    for tweet in tweets:
        terms = tweet["text"].split()
        for term in terms:
            sums[term] = sums.get(term, 0) + 1
    return sums

def compute_overall_sum(sums):
    overall_sum = 0.0
    for key in sums:
        overall_sum += sums[key]
    return overall_sum

def calculate_frequency(sums, overall_sum):
    for key in sums:
        print key, sums[key]/overall_sum

def main():
    tweet_file = open(sys.argv[1])
    tweets = read_tweets(tweet_file)
    tweet_file.close()
    sums = compute_totals(tweets)
    overall_sum = compute_overall_sum(sums)
    calculate_frequency(sums, overall_sum)    

if __name__ == '__main__':
    main()