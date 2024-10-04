-- 코드를 입력하세요
# with onl as (select * from ONLINE_SALE_ID)

with tot as (
    (select  PRODUCT_ID, SALES_AMOUNT, SALES_DATE, NULL as USER_ID from OFFLINE_SALE) 
    union all 
    (select PRODUCT_ID, SALES_AMOUNT, SALES_DATE, USER_ID from ONLINE_SALE))
select date_format(SALES_DATE, "%Y-%m-%d") as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT from tot 
where EXTRACT(month from SALES_DATE) = 3 and EXTRACT(year from SALES_DATE) = 2022
order by 1, 2, 3; 