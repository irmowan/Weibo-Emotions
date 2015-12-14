# Author: irmo
# Date: 2015.12.14

# For unicode reading
import codecs

# From emotions.txt generate a dictionary of emotions

file_emotions = codecs.open('data/emotions.txt', 'r', 'utf-8')
dic = {}
for line in file_emotions:
    x = line.split(':')
    emotion = x[0][1:-1]
    label = int(x[1])
    dic[emotion] = label

file_emotions.close()

# Read line by line to analyse
file_tweets = codecs.open('data/tweets_sample.txt', 'r', 'utf-8')
cnt = 0
for line in file_tweets:
    fields = line.split()
    # Pick the weibo field up
    weibo = ""
    for i in range(5, len(fields)):
        if fields[i] in ['m', 'f']:
            break
        weibo += fields[i]
    pos = 0
    nag = 0
    # match the emotions
    for key in dic.keys():
        if key in weibo:
            if dic[key] == 1:
                pos += 1
            else:
                nag += 1
    print(weibo)
    if pos > 0 and nag == 0:
        print("Positive")
    if nag > 0 and pos == 0:
        print("Nagitive")
    if pos > 0 and nag > 0:
        print("Ambivalent, but more ", "positive" if pos > nag else "nagitive")
    cnt += 1
file_tweets.close()

print("Count of weibo: ", cnt)
