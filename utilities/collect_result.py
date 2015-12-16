from __future__ import print_function

import codecs
import sys
from pyspark import SparkContext

if __name__ == '__main__':
    sc = SparkContext(appName = "collect_result")

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage(only running on local): collect_result input_path(hdfs) output_path(local) #sample(optional)")
        exit(-1)

    if len(sys.argv) == 4:
        nsample = int(sys.argv[3])
        lines = sc.textFile(sys.argv[1]).takeSample(False, nsample)
    else:
        lines = sc.textFile(sys.argv[1]).collect()

    with codecs.open(sys.argv[2], 'w', "utf-8") as f:
        for line in lines:
            f.write(line + '\n')
