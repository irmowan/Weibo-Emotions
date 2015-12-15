from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext

def forward_predict(line):
    fields = line.split('\t')

    text = fields[10]
    npos = int(fields[-2])
    nneg = int(fields[-1])

    emotion = (npos and not nneg and "Positive") or (not npos and nneg and "Negative") or "Ambivalent"

    return (emotion, 1 if '//' in text else 0)

def analyse(path, outputPath):
    lines = sc.textFile(path, use_unicode=False)

    results = lines.map(forward_predict).reduceByKey(add)

    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: emotion_forward naive_date result-path")
        exit(-1)

    sc = SparkContext(appName = "emotion_forward")

    analyse(sys.argv[1], sys.argv[2])
    
    sc.stop()
