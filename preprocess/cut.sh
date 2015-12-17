#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 cut.py hdfs:///weibo/data/emotions.txt hdfs:///weibo/data/naive hdfs:///weibo/result/cut
