-- 코드를 작성해주세요

select case when count(case when s.CATEGORY="Front End" then 1 end)>0 and count(case when s.NAME="Python" then 1 end)>0 then "A"
            when count(case when s.NAME="C#" then 1 end)>0 then "B"
            when count(case when s.CATEGORY="Front End" then 1 end)>0 then "C"
            else NULL end as GRADE ,d.ID, d.EMAIL 
from DEVELOPERS as d LEFT JOIN SKILLCODES as s on d.SKILL_CODE & s.CODE = s.CODE
group by d.ID, d.EMAIL
having GRADE is not NULL
order by GRADE, ID;
