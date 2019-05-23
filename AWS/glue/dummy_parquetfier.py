import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "mydb", table_name = "articles", transformation_ctx = "dynamic_frame")

mapped_df = ApplyMapping.apply(frame = dynamic_frame, mappings = [("article", "string", "article", "string"), ("price", "double", "price", "double"), ("quantity", "int", "quantity", "int"), ("comment", "string", "comment", "string"), ("date", "string", "date", "string")], transformation_ctx = "mapped_df")

resolvechoice = ResolveChoice.apply(frame = mapped_df, choice = "make_struct", transformation_ctx = "resolvechoice")

dropnullfields = DropNullFields.apply(frame = resolvechoice, transformation_ctx = "dropnullfields")

parquet_df = glueContext.write_dynamic_frame.from_options(frame = dropnullfields, connection_type = "s3", connection_options = {"path": "s3://bucketmehdi/articlesParquet"}, format = "parquet", transformation_ctx = "parquet_df")

job.commit()
