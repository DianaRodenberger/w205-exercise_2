#Sample code snippets for working with psycopg


#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2
import sys

word=""
if len(sys.argv) > 1:
    word = sys.argv[1]



conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")




#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

cur = conn.cursor()


if len(word) > 0:
    cur.execute("SELECT word, count from Tweetwordcount where word=%s", (word,))
else:
    cur.execute("SELECT word, count from Tweetwordcount")
    

if len(word) > 0:
    records = cur.fetchall()
    for rec in records:
       print "word = ", rec[0]
       print "count = ", rec[1], "\n"
else:
    print "Total number of occurrences of % is %" % (word, cur.fetchone())

conn.commit()
cur.close()
conn.close()



#if __name__ == "__main__":
#    if len(sys.argv) > 1:
