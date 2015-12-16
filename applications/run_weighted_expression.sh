#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 weighted_expression.py hdfs:///weibo/data/naive hdfs:///weibo/data/emotions.txt hdfs:///weibo/result/weighted_expression
