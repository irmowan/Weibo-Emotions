from __future__ import print_function

import sys
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

    fields = line.split('\t')

    fields[-2] = fields[-2] or -2

    tweet = "".join(fields[5: -6]) 

    for keyword, emotion in emotions.iteritems():
        if keyword in tweet:
            c[emotion] += 1
    
    return " ".join(fields[0: 5] + fields[-6: -1] + fields[5: -6] + [str(c[0]), str(c[1])])

def analyse(path, emotions, outputPath):
    lines = sc.textFile(sys.argv[2], use_unicode=False)

    results = lines.map(count)

    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: naive emotions-file tweets-file result-file")
        exit(-1)
    sc = SparkContext(appName = "WeiboNaive")

    emotions = load_emotions(sys.argv[1])

    analyse(sys.argv[2], emotions, sys.argv[3])
