-- run as root
create database swldb;
grant usage on swldb.* to 'swl'@'localhost' identified by 'lws';
grant all privileges on swldb.* to 'swl'@'localhost' identified by 'lws';
