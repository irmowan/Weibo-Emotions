crawled from Weibo through its open APIs under the permission of Sina. (http://open.weibo.com/wiki/2/statuses/user_timeline)


There are two files:


1. emoticons.txt: 
list of emoticons we manually selected and labelled. 
Each line represents one emoticon labeled as 1 or 2, and 1 stands for the positive, 2 stands for the negative.


2. tweets.txt: 
the emotional tweet data are collected from 137,981 users posed in the year of 2012. 
The users are collected by breadth-first search starting from several Weibo-verified users with a large group of followers and then crawl each user’s followers’ list, add the new users into the searching queue. Then We use the selected emoticons to label their positive(tweets containing only positive emoticons), negative(tweets containing only negative emoticons) and ambivalent tweets(tweets containing both positive and negative emoticons). 16 million emotional tweets in total are recorded in this file.
Every line in the file contains the information of one tweet, 
and the fields of the tweet is filled in the columns seperated by a TAB character. Some fields may be missing but the space are saved, and the content of each columns are as follows.

The first 6 columns are about the tweets, 
which are the ids of the tweet and the user (these two ids are encrypted for privacy protection), 
timestamp (the time when this tweet is posted on line), 
number of comments, 
number of reposts, 
tweet text.

The last 5 columns are about the users, which are the gender of users(m stands for male, and f stands for female), the number of friends, followers, bi_followers, verified type(-1:ordinary users, 0 stands for celebrities, 1 stands for government, 2 stands for enterprises, 3 stands for medias, 4 stands for campus, 5 stands for websites, 6 stands for apps, 7 stands for organizations,8 stands for enterprises under investigation, 200 stands for junior members, and 220 stands for senior members).


Note that the information of users in each tweet are recorded when the tweets are posted, as a result, the users' information may change by time.
