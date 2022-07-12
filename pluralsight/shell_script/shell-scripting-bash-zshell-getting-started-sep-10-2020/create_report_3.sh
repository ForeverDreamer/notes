#!/bin/bash -x

# -x: 输入调试信息 或 如果使用!#/usr/bin/env bash, set -x

# sudo apt install shellcheck
## shellcheck create_report.sh

# create_report_3.sh H6 ~/data
# 命令行参数："$1"第一个参数，"$2"第二个参数，以此类推。。。
container="$1"
directory="$2"

# -- 指定选项结束位置，解决参数前边带"-"的问题
mkdir -p -- "$directory"
# {}, 变量分割符，避免歧义
# 终端定义：export input_file=shipments.csv, export让子进程应用父进程变量
grep -- "$container" "$input_file" > "$directory/${container}_report.csv"

#echo "Wrote report $directory/${container}_report.csv"
printf "Wrote report %s/%s_report.csv" "$directory" "${container}"