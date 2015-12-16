from __future__ import print_function

import codecs
import sys
import subprocess
from pyspark import SparkContext
from operator import add
import re

def pre_process(line):
    a0 = re.compile('\[(^\])*\]')
    a1 = re.compile('http[a-zA-Z0-9/:.]*')
    a2 = re.compile('www.[a-zA-Z0-9/:.]*')
    #line=a0.sub(line)
    line=a1.sub(line)
    line=a2.sub(line)
    return line

def get_repost_count(line):
    line=line.split('\t')
    return (line[1],int(line[4]))

def analyse(path, outputPath):
    lines = sc.textFile(sys.argv[1], use_unicode=False)
    results=lines.map(get_repost_count).reduceByKey(add).map(lambda (x,y):(y,x)).sortByKey(False)
    # chinese words in the output files are shown as \x343
    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: naive tweets-file result-file")
        exit(-1)
    sc = SparkContext(appName = "Find celebrities")
    analyse(sys.argv[1], sys.argv[2])
