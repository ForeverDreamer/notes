# 启动服务器
docker run --name my_mongodb -d -p 27017:27017 -v D:\mongodb:/data/db -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=PassForCfe123 -e TZ=Asia/Shanghai mongo:4.4

# 启动客户端
mongo [--host localhost] [--port 27017]
mongo --authenticationDatabase "admin" -u "root" -p

show dbs
use admin
show collections

# 启动replica set
# windows powershell
cd D:\data_files\notes\misc\mongodb\mongors
docker-compose up -d
# 等待5秒
docker-compose exec mongo1 /scripts/rs-init.sh
# 连接终端
docker exec -it mongo1 sh

# bash
./startdb.sh
