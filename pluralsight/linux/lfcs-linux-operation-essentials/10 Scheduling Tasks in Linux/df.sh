#!/usr/bin/bash
FILE=/tmp/df.txt
df -h > $FILE
mail -s "df $(date +%F)" tux < $FILE && rm $FILE
