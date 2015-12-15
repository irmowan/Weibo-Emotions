#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 emotion_forward.py hdfs:///weibo/data/naive hdfs:///weibo/result/emotion_forward
