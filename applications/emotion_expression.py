from __future__ import print_function

import sys
from pyspark import SparkContext

def predict(line):
    fields = line.split()
    
    tweet_id = fields[0]
    text = "".join(fields[10: -2])
    npos = int(fields[-2])
    nneg = int(fields[-1])

    emotion = (npos and not nneg and "Positive") or (not npos and nneg and "Negative") or "Ambivalent"

    return '%s %d %d %s %s' % (emotion, npos, nneg, text, tweet_id)

def analyse(path, outputPath):
    lines = sc.textFile(path, use_unicode=False)

    results = lines.map(predict)

    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: emotion_expression naive-data result-path")
        exit(-1)

    sc = SparkContext(appName = "emotion_expression")

    analyse(sys.argv[1], sys.argv[2])
