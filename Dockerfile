FROM openjdk:11-jre-slim

RUN apt-get update && \
    apt-get install -y python3 python3-pip procps && \
    apt-get clean

RUN pip3 install pyspark

WORKDIR /app

COPY pyspark_task.py .
COPY tests.py .
COPY main.py .

COPY run_all.sh .
RUN chmod +x run_all.sh
CMD ["./run_all.sh"]