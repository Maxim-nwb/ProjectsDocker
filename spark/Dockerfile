FROM bitnami/spark:3.2.1-debian-11-r0
USER 1001
COPY ProjectJobs.jar /opt/bitnami/spark/Project/ProjectJobs.jar
COPY postgresql-42.7.3.jar /opt/bitnami/spark/jars/postgresql-42.7.3.jar
COPY hive-site.xml /opt/bitnami/spark/conf/hive-site.xml
COPY core-site.xml /opt/bitnami/spark/conf/core-site.xm
COPY hdfs-site.xml /opt/bitnami/spark/conf/hdfs-site.xml
