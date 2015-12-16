#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 6 time_range.py hdfs:///weibo/data/naive hdfs:///weibo/result/time_range
