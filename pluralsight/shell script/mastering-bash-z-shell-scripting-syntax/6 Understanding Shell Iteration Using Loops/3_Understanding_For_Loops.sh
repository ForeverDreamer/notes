#!/bin/bash
for ((i=0; i<5; i++)); do
    echo "$i"
done

for ((i=5; i>0; i--)); do
    echo "$i"
done

declare -a users=("bob" "joe" "sue")
# 计算数组长度
echo user数量: ${#users[*]}

for ((i=0; i<${#users[*]}; i++)); do
    # sudo useradd "${users[$i]}"
    echo "${users[$i]}"
done

for f in *; do
# for f in *.sh; do
# for f in $(ls); do
    stat -c "%n %F" "$f"
done