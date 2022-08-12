# 启动服务器
docker run --name my_mongodb -d -p 27017:27017 -v D:\mongodb:/data/db -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=PassForCfe123 -e TZ=Asia/Shanghai mongo:4.4

# 启动客户端
mongo [--host localhost] [--port 27017]
mongo --authenticationDatabase "admin" -u "root" -p

show dbs
use admin
show collections


# 启动replica set

# C:\Windows\System32\drivers\etc\hosts新增配置(Windows) 或 /etc/hosts(Linux)
# mongors
127.0.0.1       mongo1
127.0.0.1       mongo2
127.0.0.1       mongo3
# 客户端主机hosts配置
远程主机ip(如：192.168.71.20)       mongo1
远程主机ip(如：192.168.71.20)       mongo2
远程主机ip(如：192.168.71.20)       mongo3
# 连接字符串
'mongodb://mongo1:27021,mongo2:27022,mongo3:27023/?replicaSet=dbrs'

# windows powershell
cd D:\data_files\notes\misc\mongodb\mongors
docker-compose up -d

# 等待10秒
docker exec -it mongo1 /scripts/rs-init.sh

# bash
chmod u+x *.sh
./startdb.sh

# 连接终端
docker exec -it mongo1 sh


# 重新部署replica set
docker-compose down
删除数据库目录：data1,data2,data3
执行启动replica set步骤