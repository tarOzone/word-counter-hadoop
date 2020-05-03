rm -rf output

chmod +x mapper.py
chmod +x reducer.py

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file ./mapper.py \
-mapper "python ./mapper.py" \
-file ./reducer.py \
-reducer "python ./reducer.py" \
-input ./literatures/3252.txt \
-output ./output/
