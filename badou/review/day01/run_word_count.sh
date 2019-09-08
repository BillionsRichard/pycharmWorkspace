#!/usr/bin/env bash


HADOOP_CMD="/usr/local/src/hadoop-2.6.0/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar"

INPUT_FILE_PATH_1="/root/badou/data/The_Man_of_Property.txt"
#INPUT_FILE_PATH_1="/data/1.data"
OUTPUT_PATH="/output/wc"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py" \
    -reducer "python red.py" \
    -file ./map.py \
    -file ./red.py

# 查看結果 TOP20 单词
#  hadoop fs -cat /output/wc/part-00000 |sort -rnk 2 | head -20