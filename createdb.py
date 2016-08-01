#Purpose: Create a new database to store tweet counts.
#Assumptions: This script only runs once, before the streaming application 'Tweetwordcount' runs
#Programmer: Diana Rodenberger

import psycopg2


#Delete the database if there is already one

#connect to default database
conn=psycopg2.connect(database="postgres", user="postgres", password="pass",host="localhost", port="5432")
cur=conn.cursor()
#change the isolation level to 0 to drop the database
level = conn.isolation_level
conn.set_isolation_level(0)
#drop database if exists
cur.execute("DROP DATABASE IF EXISTS Tcount;")
cur.execute("CREATE DATABASE Tcount;")
conn.set_isolation_level(level)
#create a new database
conn.commit()
conn.close()

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur=conn.cursor()
#create table to store tweets
level = conn.isolation_level
conn.set_isolation_level(0)
cur.execute("CREATE TABLE Tweetwordcount (word TEXT PRIMARY KEY     NOT NULL, count INT     NOT NULL);")
conn.set_isolation_level(level)
conn.commit()
conn.close()




