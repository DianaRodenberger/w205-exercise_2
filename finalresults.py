#Purpose: Returns the total number of word occurrences in a stream. If no word was provided, then it
#         returns the toal number of occurrences for each word stored in table Tweetwordcount.
#Author:  Diana Rodenberger
#Assumptions:
#         1) database tcount has been created prior to the call to this script.
#         2) the script runs under user 'root'

import psycopg2
import sys



#Get word provided by user
if len(sys.argv) > 1:
    word = sys.argv[1]
else:
    word=""

#Connecting to a database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")


cur = conn.cursor()


if len(word) > 0:
    cur.execute("SELECT word, count from Tweetwordcount where word=%s", (word,))
else:
    cur.execute("SELECT word, count from Tweetwordcount order by word")
    
#fetch number of occurrences for each word
if len(word) == 0:
    records = cur.fetchall()
    for rec in records:
       print "word = ", rec[0]
       print "count = ", rec[1], "\n"
else:
    result = cur.fetchone()[1]
            
    print "Total number of occurrences of %s is %d" % (word, result)

#close cursor and connection
conn.commit()
cur.close()
conn.close()


