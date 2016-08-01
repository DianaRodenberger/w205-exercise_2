#Purpose: Gets two integers (k1,k2) and returns all the words that the total number of occurrences is between k1 and k2
#Author:  Diana Rodenberger



import psycopg2
import sys

#retrieve the lower limit and upper limit of the range of occurrences requested.
if len(sys.argv) ==3:
    k1 = sys.argv[1]
    k2 = sys.argv[2]
    print k1
    print k2
else:
    print "You need to provide two values"

#connect to database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#select words that the total number of occurrences is between k1 and k2
cur = conn.cursor()
cur.execute("SELECT word, count from Tweetwordcount where count >= %s and count <= %s", (k1,k2))
records = cur.fetchall()
for rec in records:
    print "word = ", rec[0]
    print "count = ", rec[1], "\n"
conn.commit()
cur.close()
conn.close()



