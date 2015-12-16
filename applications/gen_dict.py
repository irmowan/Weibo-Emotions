from __future__ import print_function

import codecs
import sys
import subprocess
from pyspark import SparkContext
from operator import add
import re


def analyse(path, outputPath):
    lines = sc.textFile(sys.argv[1], use_unicode=False)
    numPos=lines.filter(lambda s :int(s.split('\t')[-2])>int(s.split('\t')[-1])).count()
    numNeg=lines.filter(lambda s :int(s.split('\t')[-2])<int(s.split('\t')[-1])).count()
    wcPos=lines.filter(lambda s :int(s.split('\t')[-2])>int(s.split('\t')[-1])).flatMap(lambda line : line.split('\t')[10].split(' ')).map(lambda word:(word,1)).reduceByKey(add)
    wcAll=lines.flatMap(lambda line : line.split('\t')[10].split(' ')).map(lambda word:(word,1)).reduceByKey(add)
    result=wcPos.leftOuterJoin(wcAll).filter(lambda (key,(v1,v2)):v2>1000).map(lambda (key,(v1,v2)):"%s %f"%(key,float(v1)/float(v2)))
    result.saveAsTextFile(outputPath)
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: naive tweets-file result-file")
        exit(-1)
    sc = SparkContext(appName = "Find celebrities")
    analyse(sys.argv[1], sys.argv[2])
