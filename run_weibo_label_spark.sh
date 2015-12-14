#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 weibo_label_spark.py hdfs:///weibo/data/emotions.txt hdfs:///weibo/data/tweets.txt hdfs:///weibo/result/naive
