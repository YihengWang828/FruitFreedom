
drop table if exists sub_category;


create table sub_category
(
   type                 char(32),
   brand                varchar(255),
   price                float,
   sales                bigint,
   deliver              float,
   describemark           float,
   server               float,
   marks                float,
   picture              varchar(255)
);


drop table if exists all_category;


create table all_category
(
   marks                float not null,
   type                 char(32) not null,
   brand                varchar(255) not null,
   price                float not null,
   sales                bigint not null
);


drop table if exists Fruit;

create table Fruit
(
   region               char(32) not null,
   category             char(32) not null,
   min_price            float not null,
   max_price            float not null,
   avg_price            float not null,
   time                 date not null
);


drop table if exists today_recommendation;

create table today_recommendation
(
   ranking              int not null,
   fruit                char(32) not null,
   price                float not null,
   img                  varchar(255),
   primary key (ranking)
);



drop table if exists Map_Distribution;

create table Map_Distribution
(
   region               char(32),
   category             char(32),
   average_price        float
);



drop table if exists 2019_Fruit_Price;


create table 2019_Fruit_Price
(
   month                int not null,
   day                  int not null,
   type                 char(32) not null,
   price                float not null
);
