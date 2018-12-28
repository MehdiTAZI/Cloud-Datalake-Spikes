CREATE EXTERNAL TABLE IF NOT EXISTS myDB.articles (
  `article` string,
  `price` double,
  `quantity` int,
  `comment` string 
) PARTITIONED BY (
  `date` string 
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://bucketmehdi/articles/'

ALTER TABLE myDB.articles ADD PARTITION (`date`=2018) location 's3://mybucket/articles/2018'
ALTER TABLE myDB.articles ADD PARTITION (`date`=2019) location 's3://mybucket/articles/2019'

select * from articles where date='2019'
