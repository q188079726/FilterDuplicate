# 文件去重

#### 原理：
将每一个路径下的文件用路径作为 key，文件名 的 set 为值，放到一个数组里，用冒泡的方法一一比较，有重复的就把重复的文件名和路径打印出来

#### 使用方法：
将文件放到要查找的根目录下，使用命令行 python duplicate.py即可在同级目录下查看日志

