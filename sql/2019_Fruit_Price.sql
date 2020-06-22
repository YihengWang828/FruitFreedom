/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/6/15 16:16:01                           */
/*==============================================================*/


drop table if exists 2019_Fruit_Price;

/*==============================================================*/
/* Table: 2019_Fruit_Price                                      */
/*==============================================================*/
create table 2019_Fruit_Price
(
   month                int not null,
   day                  int not null,
   type                 char(32) not null,
   price                float not null
);

