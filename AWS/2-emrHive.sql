CREATE EXTERNAL TABLE IF NOT EXISTS people(
  fn string,
  ln string,
  age int,
  country string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION
  's3a://itinsight-fr/RAW/';

CREATE TABLE IF NOT EXISTS people_analytics(
  fn string,
  ln string,
  age int)
PARTITIONED BY (
  country string) STORED AS ORC 
LOCATION
  's3a://itinsight-fr/DATA';

insert into table people_analytics partition (country='MA') select fn,ln,age  from people where country ='MA' and age BETWEEN 27 AND 50 ;

INSERT OVERWRITE DIRECTORY 's3a://itinsight-fr/DATA/result/' SELECT fn,ln, age, country FROM people WHERE age BETWEEN 30 AND 40;
