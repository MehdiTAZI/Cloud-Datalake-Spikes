echo "this line is composed of 7 characters" > wordcount.txt
echo "this one of 4 5" >> wordcount.txt
echo "with this one of 16 characters it makes a full file of a total of 28" >> wordcount.txt

hdfs dfs -put wordcount.txt adl://engiedatalake.azuredatalakestore.net/out/wordcount.txt
