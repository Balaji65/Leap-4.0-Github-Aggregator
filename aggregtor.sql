CREATE DATABASE github_user;
use github_user;
create table user_data(
UNIQUE_ID VARCHAR(20),
REPO_NAME VARCHAR(20),
DOMAIN_NAME VARCHAR(20),
NO_OF_COUNT BIGINT(255),
DATE_RANGE DATE,
DATE_OF_RUN DATE);
desc user_data ;

INSERT INTO user_data VALUE('55667788','MANIC','hashicorp','20','2021-06-05',curdate());
select * from user_data;
