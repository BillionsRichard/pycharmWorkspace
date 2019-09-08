#!/usr/bin/env bash
HADOOP_CMD="/usr/local/src/hadoop-2.6.0/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar"
INPUT_FILE_PATH="/data/The_Man_of_Property.txt"
OUTPUT_FILE_PATH="/output/wc"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_FILE_PATH

#Step1
$HADOOP_CMD jar $STREAM_JAR_PATH \
 -input $INPUT_FILE_PATH \
 -output $OUTPUT_FILE_PATH \
 -mapper "python map.py" \
 -reducer "python red.py" \
 -file ./map.py \
 -file ./red.py \
 -jobconf mapred.job.name="wordCount"



