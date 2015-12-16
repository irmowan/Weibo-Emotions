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

def load_dict(path):
    dic = {}
    lines = sc.textFile(path, use_unicode=False).collect()
    for line in lines:
        x = line.split(' ')
        # change range from [0, 1] to [-1, 1]
        dic[x[0]] = float(x[1]) * 2 - 1
    return dic

def add(x, y):
    return tuple([x[i] + y[i] for i in range(2)])

def advanced_expression_weight(line):
    fields = line.split('\t')
    text = fields[10]
    npos = int(fields[-2])
    nneg = int(fields[-1])
    emotion = (npos and not nneg and 1) or (not npos and nneg and -1) or 0
    emotion = float(emotion)
    cnt = 1 # emotion is included
    words = text.split(' ')
    for word in words:
        if word in word_dict.keys():
            emotion += word_dict[word]
            cnt += 1
    emotion = emotion / cnt
    # Here, emotion at [-1, 1]
    ans = []
    for expression in expressions:
        if expression in text:
            ans.append((expression, (emotion, 1)))
    return ans

def analyse(path, outputPath):
    lines = sc.textFile(path, use_unicode=False)
    results = lines.flatMap(advanced_expression_weight).reduceByKey(add).map(lambda pair: "%s %.3f" % (pair[0], pair[1][0] / pair[1][1]))
    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: advanced_weighted_expression naive_data emotion-path emotion_dict-path result-path")
        exit(-1)
    sc = SparkContext(appName = "weighted_expression")
    expressions = load_emotions(sys.argv[2])
    word_dict = load_dict(sys.argv[3])
    analyse(sys.argv[1], sys.argv[4])
    sc.stop()

