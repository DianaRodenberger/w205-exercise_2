#Purpose: Gets two integers (k1,k2) and returns all the words that the total number of occurrences is between k1 and k2
#Author:  Diana Rodenberger



import psycopg2
import sys
import csv


#connect to database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#select words that the total number of occurrences is between k1 and k2
cur = conn.cursor()
#get the top 20 words
cur.execute("SELECT word, count from Tweetwordcount order by count desc limit 20")
records = cur.fetchall()
tweetwords = [['word','count']]
for rec in records:
    print "word = ", rec[0]
    print "count = ", rec[1], "\n"
    wordcount= [rec[0],rec[1]]
    tweetwords.append(wordcount)
    

conn.commit()
cur.close()
conn.close()

with open('tweetwords.csv', 'wt') as fout:
    cout = csv.writer(fout)
    cout.writerows(tweetwords)
    


