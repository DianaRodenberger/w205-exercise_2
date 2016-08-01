Instructions to run the Twitter Streaming Application 'Tweetwordcount'

1) Before running the application, verify that you have streamparse, python 2.7.6 and postgress installed.
2) Start postgres from directory /data
	$./start_postgres.sh
3) Run all applications under user 'root'
4) Clone repository https://github.com/DianaRodenberger/w205-exercise_2.git
	$git clone https://github.com/DianaRodenberger/w205-exercise_2.git
5) Create database in postgres using script in directory w205-exercise_2
	$python createdb.py
6) Go to directory Tweetwordcount
        $cd Tweetwordcount
7) Run streaming application
	$sparse run
8) Stop execution after 5 minutes or longer (5 minutes recommended)
	hit keys Ctrl+C
9) Go to directory w205-exercise_2
	$cd w205-exercise_2
10)Run serving scripts
	10.1) Run script to get the number of occurrences for a given word
		$python finalresults.py Trump
	10.2) Or run script to get the number of occurrences for each word collected from the stream of tweets
		$python finalresults.py
	10.3) Run script to get words that have occurences within the input range
		$python histogram.py 150 200
	10.4) Run script to get the top 20 words in a csv file. The csv file can be used to create a plot.
		$python top20words_csv.py
