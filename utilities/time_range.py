from __future__ import print_function

import sys
from pyspark import SparkContext

if __name__ == '__main__':
    sc = SparkContext(appName = "time_range")

    if len(sys.argv) != 3:
        print("Usage: time_range data result")
        exit(-1)

    lines = sc.textFile(sys.argv[1])

    range = lines.map(lambda x: (float(x.split('\t')[2]), float(x.split('\t')[2])))\
                 .reduce(lambda a, b: (min(a[0], b[0]), max(a[1], b[1])))

    print(range)
    
