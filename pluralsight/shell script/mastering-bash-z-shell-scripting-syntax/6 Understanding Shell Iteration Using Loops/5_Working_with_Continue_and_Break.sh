#!/bin/bash
echo 显示非目录
for file in *; do
    if [[ -d $file ]]; then
        continue
    fi
    stat -c "%n %F" "$file"
done

echo 显示非普通文件
for file in *; do
    if [[ -f $file ]]; then
        continue
    fi
    stat -c "%n %F" "$file"
done

echo 遇到目录退出
for file in *; do
    if [[ -d $file ]]; then
        continue
    fi
    stat -c "%n %F" "$file"
done

echo 遇到普通文件退出
for file in *; do
    if [[ -f $file ]]; then
        continue
    fi
    stat -c "%n %F" "$file"
done