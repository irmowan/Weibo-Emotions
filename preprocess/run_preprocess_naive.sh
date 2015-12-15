#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 6 preprocess_naive.py hdfs:///weibo/data/emotions.txt hdfs:///weibo/data/tweets.txt hdfs:///weibo/data/naive
