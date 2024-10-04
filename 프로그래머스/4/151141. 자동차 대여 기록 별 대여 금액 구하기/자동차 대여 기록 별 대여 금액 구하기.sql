-- 코드를 입력하세요
with t1 as (
    SELECT h.HISTORY_ID, h.car_id, c.DAILY_FEE * (DATEDIFF(h.end_date, h.start_date)+1) as FEE,
        case when DATEDIFF(h.end_date, h.start_date)+1 >= 90 then '90일 이상' 
            when DATEDIFF(h.end_date, h.start_date)+1 >= 30 then '30일 이상'
            when DATEDIFF(h.end_date, h.start_date)+1 >= 7 then '7일 이상' 
            else NULL end as DURATION_TYPE, c.CAR_TYPE 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h join CAR_RENTAL_COMPANY_CAR as c on h.CAR_ID = c.CAR_ID
    where c.CAR_TYPE = '트럭'
)
select t.HISTORY_ID, ROUND(t.FEE * (1-(coalesce(d.DISCOUNT_RATE, 0)) / 100)) as FEE
from t1 as t left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as d on t.DURATION_TYPE=d.DURATION_TYPE and t.CAR_TYPE=d.CAR_TYPE
order by 2 desc, 1 desc;

