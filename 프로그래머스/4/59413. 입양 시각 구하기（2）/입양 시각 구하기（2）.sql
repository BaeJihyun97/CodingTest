-- 코드를 입력하세요
with recursive HOURS(h) as (
    select 0 as h 
    union all
    select h + 1 from HOURS where h < 23
)
select h.h as HOUR, count(a.ANIMAL_ID) as COUNT
from HOURS as h left outer join (SELECT extract(hour from DATETIME) as h, ANIMAL_ID from ANIMAL_OUTS ) as a on h.h = a.h
group by HOUR
order by HOUR;