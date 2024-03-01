## MySQL with Docker
- 시작 전에 .env 파일을 만들고 MYSQL_ROOT_PASSWORD=<yourpassword>를 작성해주세요

### Pulling mysql image from docker hub
```bash
docker pull mysql:8
docker run --name mysql_test --env-file .env -d -p 3306:3306 -v ${pwd}/test_volume:. mysql:8
docker exec -it mysql_test /bin/bash
```
- --name option은 생성할 mysql container의 이름을 지정하는 옵션입니다.
- -e option은 컨테이너 내 환경변수를 추가하는 명령어입니다.
- -p option은 <host port:container port>로 host에서 3306으로 접근했을 시 container 내부 3306 port로 연결시켜줍니다.


### mysql usage
```
mysql -u root -p
SHOW DATABASES;
CREATE DATABASE USER;
use USER;

CREATE TABLE USER (ID INT(10) NOT NULL, NAME CHAR(20) NOT NULL);
INSERT INTO USER VALUES(1, "KIM");
INSERT INTO USER VALUES(2, "LEE");
SELECT * FROM USER;
```
