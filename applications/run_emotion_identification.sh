#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 6 emotion_identification.py hdfs:///weibo/data/naive hdfs:///weibo/result/emotion_identification
