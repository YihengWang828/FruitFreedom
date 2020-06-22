use ffdbs;
/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/6/22 11:29:12                           */
/*==============================================================*/


drop table if exists all_category;

/*==============================================================*/
/* Table: all_category                                          */
/*==============================================================*/
create table all_category
(
   category             char(32) not null,
   brand                varchar(255) not null,
   price                float not null,
   sales                bigint not null,
   delivermark          float not null,
   describemark         float not null,
   servermark           float not null,
   marks                float not null,
   picture              varchar(255) not null
);

