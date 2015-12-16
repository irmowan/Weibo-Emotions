#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 gen_dict.py hdfs:///weibo/result/cut hdfs:///weibo/result/emotion_dict
