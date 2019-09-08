/* select * from orders limit 10;
order_id    user_id eval_set    order_number    order_dow   order_hour_of_day    days_since_prior_order
2539329 		1       prior       1       		    2       		08
2398795 		1       prior       2       		    3       		07                  15.0
473747  		1       prior       3       		    3       		12                  21.0
2254736 		1       prior       4       		    4       		07                  29.0
431534  		1       prior       5       		    4       		15                  28.0
3367565 		1       prior       6       		    2       		07                  19.0
550135  		1       prior       7       		    1       		09                  20.0
3108588 		1       prior       8       		    1       		14                  14.0
2295261 		1       prior       9       		    1       		16                  0.0
Time taken: 1.078 seconds, Fetched: 10 row(s)
hive>
> select * from order_products_prior limit 10;
OK
order_id   product_id     add_to_cart_order  reordered
2         33120           1                 1
2         28985           2                 1
2         9327            3                 0
2         45918           4                 1
2         30035           5                 0
2         17794           6                 1
2         40141           7                 1
2         1819            8                 1
2         43668           9                 0

hive>  */
select user_id, count(user_id)
from orders join order_products_prior pri
on orders.order_id = pri.order_id
group by user_id

select user_id,product_id, count(1) as usr_prod_cnt
from oders join order_products_prior pri
on orders.order_id=pri.order_id
group by user_id, product_id
limit 10;

select user_id, product_id,
row_number() over(partition by user_id order by usr_prod_cnt desc) as row_num
from
(select user_id,product_id,
count(1) over(partition by user_id, product_id) as usr_prod_cnt
from orders
join order_products_prior pri
on orders.order_id=pri.order_id
group by user_id, product_id)t
limit 10;

select user_id, product_id,
row_number() over(distribute by user_id sort by usr_prod_cnt desc) as row_num
from
(select user_id,product_id,
count(1) as usr_prod_cnt
from orders
join (select * order_products_prior limit 3000) pri
on orders.order_id=pri.order_id
group by user_id, product_id)t
limit 10;

--结果收集 collect_list
select user_id, product_id,
row_number() over(distribute by user_id sort by usr_prod_cnt desc) as row_num
from
(select user_id,product_id,
count(1) as usr_prod_cnt,
count(1) over(partition by user_id) as total_prod_cnt
from orders
join (select * order_products_prior limit 3000) pri
on orders.order_id=pri.order_id
group by user_id, product_id)t
limit 10;

--作业2
-- 2. 建分区表，orders表按照order_dow建立分区表
-- orders_part，然后从hive查询orders动态插入
-- orders_part表中
-- hive> desc orders;
-- OK
-- col_name        data_type       comment
-- order_id                string
-- user_id                 string
-- eval_set                string
-- order_number            string
-- order_dow               string
-- order_hour_of_day       string
-- days_since_prior_order  string
-- Time taken: 0.263 seconds, Fetched: 7 row(s)
-- hive>
create table orders_part
(order_id string,
user_id string,
eval_set string,
order_number string,

order_hour_of_day string,
days_since_prior_order  string
)partitioned by (order_dow string)
row format delimited
fields terminated by '\t';

--动态插入分区
set hive.exec.dynamic.partition=true
set hive.exec.dynamic.partition.mode=nonstrict

insert overwrite table orders_part
partition(order_dow="1")---(dt='2018-10-28')
select order_id, user_id,eval_set,order_number,order_hour_of_day,days_since_prior_order
from orders where order_dow="1";

insert overwrite table orders_part
partition(order_dow)---(dt='2018-10-28')
select order_id, user_id,eval_set,order_number,order_hour_of_day,days_since_prior_order,order_dow
from orders;

--查询分区
--show partitions orders_part;

-- 1、 PV 每个商品被购买的数量。
select product_id,count(1) as pv
from order_products_prior
group by product_id;

-- 2、uv 每个商品有多少个用户购买
select product_id,count(distinct user_id) as uv
from orders join order_products_prior pri
on orders.order_id=pri.order_id
group by pri.product_id;

--3、reorders数
select product_id, sum(cast(reordered as int)) as reorderd_cnt
from order_products_prior
group by product_id
;