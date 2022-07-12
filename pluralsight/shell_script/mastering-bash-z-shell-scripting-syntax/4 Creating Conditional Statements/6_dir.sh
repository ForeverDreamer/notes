#!/bin/bash
declare -l DIR
# -n: 不换行
echo -n "Enter a directory to create: "
# -r 屏蔽\，如果没有该选项，则\作为一个转义字符，有的话 \就是个正常的字符了
read -r DIR
if [[ -e $DIR ]]; then
    echo "$DIR already exists"
else
    if [[ -w $PWD ]]; then
        mkdir "$DIR"
    else
        echo "You don't have write permission to $PWD"
        exit 2
    fi
fi