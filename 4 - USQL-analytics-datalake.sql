 @data_req = 
   EXTRACT article string
   , price float
   , quantity int
   , comment string
   FROM "/Entities/TTA/PricePrediction/Shared/{*}.csv"
   USING Extractors.Csv();

 @result =
   SELECT DISTINCT article, SUM(quantity) AS totalQuantity
   FROM @data_req
   GROUP BY article;

OUTPUT @result   
    TO "/Entities/TTA/PricePrediction/Results/first-u-sql-result.csv"
    USING Outputters.Csv();
