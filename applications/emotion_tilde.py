from __future__ import print_function

from pyspark import SparkContext

def predict(line):
    fields = line.split()

    tweet_id = fields[0]
    text = fields[9]
    npos = int(fields[-2])
    nneg = int(fields[-1])

    emotion = (npos and not nneg and "Positive") or (not npos and nneg and "Negative") or "Ambivalent"

    return (emotion, 1 if '~' in text else 0)

def analyse(path, outputPath):
    lines = sc.textFile(sys.argv[1], use_unicode=False)

    results = lines.map(predict).reduceByKey(add)

    results.saveAsTextFile(outputPath)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: emotion_tilde naive-data result–path")
        exit(-1)

    sc = SparkContext(appName = "emotion_tilde")

    analyse(sys.argv[1], sys.argv[2])
