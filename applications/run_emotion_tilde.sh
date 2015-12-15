#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 emotion_tilde.py hdfs:///weibo/data/naive hdfs:///weibo/result/emotion_tilde
