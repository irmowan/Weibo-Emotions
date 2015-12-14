from __future__ import print_function

import codecs
import sys
import subprocess
from pyspark import SparkContext

def load_emotions(path):
    emotions = {}

    lines = sc.textFile(path, use_unicode=False).collect()
    
    for line in lines:
        x = line.split(':')
        emotions[x[0]] = int(x[1]) - 1
    return emotions

def count(line):
    c = [0, 0]

    # bug here, but does not affect this program
    tweet = "".join(line.split()[5: -5]) 

    for keyword, emotion in emotions.iteritems():
        if keyword in tweet:
            c[emotion] += 1

    emotion = (c[0] and not c[1] and "Positive") or (not c[0] and c[1] and "Negative") or "Ambivalent"

    return "%s %d %d %s" % (tweet, c[0], c[1], emotion)

def analyse(path, emotions, outputPath):
    lines = sc.textFile(sys.argv[2], use_unicode=False)

    results = lines.map(count)

    # chinese words in the output files are shown as \x343
    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: naive emotions-file tweets-file result-file")
        exit(-1)
    sc = SparkContext(appName = "WeiboNaive")

    emotions = load_emotions(sys.argv[1])

    analyse(sys.argv[2], emotions, sys.argv[3])
