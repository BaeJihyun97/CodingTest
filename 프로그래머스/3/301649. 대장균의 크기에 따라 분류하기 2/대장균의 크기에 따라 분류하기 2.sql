with sizes as (
    select e.ID, rank() over (order by e.SIZE_OF_COLONY DESC) / t.TOT_NUM as ORDER_PER 
    from ECOLI_DATA as e , (select count(*) as TOT_NUM from ECOLI_DATA) as t
)
select ID, case when ORDER_PER <= 0.25 THEN "CRITICAL" 
                when ORDER_PER > 0.25 and ORDER_PER <= 0.50 THEN "HIGH" 
                when ORDER_PER > 0.50 and ORDER_PER <= 0.75 THEN "MEDIUM" 
                ELSE "LOW" end as COLONY_NAME
from sizes
order by ID;
