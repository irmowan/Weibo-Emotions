from __future__ import print_function

import sys
from pyspark import SparkContext
from datetime import datetime
from operator import add

def identification_emotion_pair(line):
    fields = line.split()
    
    identification = fields[9]
    npos = int(fields[-2])
    nneg = int(fields[-1])

    emotion = (npos and not nneg and 1) or \
              (not npos and nneg and -1) or \
              (npos and nneg and npos >= nneg and 2) or \
              (npos and nneg and npos < nneg and -2) or 0

    key = "%s:%d" % (identification, emotion)
    return (key, 1)

def analyse(path, outputPath):
    lines = sc.textFile(path, use_unicode=False)

    results = lines.map(identification_emotion_pair)\
              .reduceByKey(add)\
              .map(lambda pair: "%s %i" % pair)

    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: emotion_identification naive-data result-path")
        exit(-1)

    sc = SparkContext(appName = "emotion_identification")

    analyse(sys.argv[1], sys.argv[2])

    sc.stop()
