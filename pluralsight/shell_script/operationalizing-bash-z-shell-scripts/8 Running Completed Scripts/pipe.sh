#!/bin/bash
declare -l line
until [[ $line == 'stop' ]]
do
  line=$(cat /var/log/pipe)
  echo "$line" >> /var/log/pipe.out
done
