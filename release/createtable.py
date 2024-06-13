# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE USERS(
# MAGIC   name string,
# MAGIC   salary INT
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail users;

# COMMAND ----------

abfss://unity-catalog-storage@dbstorage27spt7kro27ns.dfs.core.windows.net/2231600627143994/__unitystorage/catalogs/500ed1b2-a906-4a16-a79b-677d53e532e6/tables/5b7d5e3f-6b4e-4c10-aad0-457c817f0003

# COMMAND ----------

dbutils.fs.ls('abfss://unity-catalog-storage@dbstorage27spt7kro27ns.dfs.core.windows.net/2231600627143994/__unitystorage/catalogs/500ed1b2-a906-4a16-a79b-677d53e532e6/tables/')

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE hive_metastore.default.test (
# MAGIC   name string,
# MAGIC   salary INT
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO hive_metastore.default.test (name, salary) VALUES 
# MAGIC ('Alice', 75000),
# MAGIC ('Bob', 55000),
# MAGIC ('Charlie', 68000),
# MAGIC ('Diana', 62000),
# MAGIC ('Eve', 71000);
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail hive_metastore.default.test;
