#!/bin/bash

spark-submit --deploy-mode cluster --master yarn-cluster --num-executors 10 find_celebrities.py hdfs:///weibo/data/naive hdfs:///weibo/result/celebrities
