
from __future__ import print_function

import sys
# from operator import add
from pyspark import SparkContext

def load_emotions(path):
    emotions = {}
    lines = sc.textFile(path, use_unicode=False).collect()
    for line in lines:
        x = line.split(':')
        emotions[x[0]] = int(x[1]) - 1
    return emotions

def add(x, y):
    return tuple([x[i] + y[i] for i in range(3)])

def expression_weight(line):
    fields = line.split('\t')
    text = fields[10]
    npos = int(fields[-2])
    nneg = int(fields[-1])
    # Set emotion weight
    # emotion = (pos, mid, neg)
    emotion = (npos and not nneg and (1, 0, 0)) or (not npos and nneg and (0, 0, 1)) or (0, 1, 0)
    ans = []
    for expression in expressions:
        if expression in text:
            ans.append((expression, emotion))
    return ans

def count_expression(line):
    fields = line.split('\t')
    text = fields[10]

def analyse(path, outputPath):
    lines = sc.textFile(path, use_unicode=False)
    results = lines.flatMap(expression_weight).reduceByKey(add).map(lambda pair: "%s %.2f" % (pair[0], float(pair[1][0] - pair[1][2]) / sum(pair[1])))
    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: weighted_expression naive_data emotion_path result-path")
        exit(-1)
    sc = SparkContext(appName = "weighted_expression")
    expressions = load_emotions(sys.argv[2])
    analyse(sys.argv[1], sys.argv[3])
    sc.stop()

