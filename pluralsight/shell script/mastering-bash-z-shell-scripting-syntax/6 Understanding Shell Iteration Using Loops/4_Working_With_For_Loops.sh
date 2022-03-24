#!/bin/bash
for ((i=1; i<10; i++)); do
    touch "file$i"
done

for ((i=9; i>0; i--)); do
    rm "file$i"
done

declare -a users=("bob" "sue" "jake")
declare -p users
echo user数量: ${#users[*]}

for ((i=0; i<${#users[*]}; i++)); do
    echo "${users[$i]}"
done