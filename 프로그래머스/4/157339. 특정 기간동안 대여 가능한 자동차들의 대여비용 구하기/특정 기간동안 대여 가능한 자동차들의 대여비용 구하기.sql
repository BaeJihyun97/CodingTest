-- 코드를 입력하세요
with disc as (
    select CAR_TYPE, DISCOUNT_RATE from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where DURATION_TYPE='30일 이상'
), cond1 as (
    select c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE, c.OPTIONS, d.DISCOUNT_RATE from CAR_RENTAL_COMPANY_CAR as c join disc as d on c.CAR_TYPE = d.CAR_TYPE
    where c.CAR_TYPE = "SUV" or c.CAR_TYPE = "세단"
), cond2op as (
    select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where START_DATE <= "2022-11-30" and END_DATE >= "2022-11-01"
    group by car_id
)
select * from (
    select c1.CAR_ID, c1.CAR_TYPE, cast(DAILY_FEE*30*(100-DISCOUNT_RATE)/100 as UNSIGNED) as FEE 
    from cond1 as c1 left join cond2op as c2 on c1.CAR_ID = c2.CAR_ID 
    where c2.CAR_ID IS NULL
) as fin
where FEE >= 500000 and FEE <= 2000000;

