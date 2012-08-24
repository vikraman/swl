
use 'swldb';

drop table if exists `product_price`;
drop table if exists `product`;

create table `product`(
    `id` serial,
    `name` varchar(128) not null,
    `url` varchar(512) not null,
    primary key (`id`)
) engine=innodb;

create table `product_price`(
    `id` bigint unsigned,
    `ts` timestamp,
    `price` int unsigned not null,
    primary key (`id`,`ts`),
    foreign key (`id`) references `product`(`id`)
    on delete cascade on update cascade
) engine=innodb;
