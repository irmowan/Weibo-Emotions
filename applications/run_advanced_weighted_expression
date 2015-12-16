#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 advanced_weighted_expression.py hdfs:///weibo/data/naive hdfs:///weibo/data/emotions.txt hdfs:///weibo/data/emotion_dict_filter.txt hdfs:///weibo/result/advanced_weighted_expression

