/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/6/15 16:14:28                           */
/*==============================================================*/


drop table if exists Map_Distribution;

/*==============================================================*/
/* Table: Map_Distribution                                      */
/*==============================================================*/
create table Map_Distribution
(
   region               char(32),
   category             char(32),
   average_price        float
);



