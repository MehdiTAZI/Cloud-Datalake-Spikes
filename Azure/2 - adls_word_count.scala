val words = sc.textFile("adl://engiedatalake.azuredatalakestore.net/out/wordcount.txt")
val counts = words .flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)
counts.saveAsTextFile("adl://engiedatalake.azuredatalakestore.net/out/wordcount-result.txt")
