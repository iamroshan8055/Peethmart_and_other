docker pull mysql/mysql-server:latest
docker run --name=mysql_container -e MYSQL_ROOT_PASSWORD=root -d mysql/mysql-server:latest