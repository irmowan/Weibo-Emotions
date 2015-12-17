from __future__ import print_function

import codecs
import sys
import subprocess
from pyspark import SparkContext
from operator import add
import jieba

def cut_tweet(line):
    line=line.split('\t')
    line[10] = ' '.join(jieba.cut(line[10]))
    return '\t'.join(line)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: naive emotions-file tweets-file result-file")
        exit(-1)
    sc = SparkContext(appName = "WeiboNaive")
    lines = sc.textFile(sys.argv[2], use_unicode=False)
    results=lines.map(cut_tweet)
    results.saveAsTextFile(sys.argv[3])
