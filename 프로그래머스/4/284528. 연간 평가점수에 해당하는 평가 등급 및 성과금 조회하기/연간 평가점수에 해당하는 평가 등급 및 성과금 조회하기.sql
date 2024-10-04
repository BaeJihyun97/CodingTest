-- 코드를 작성해주세요

with scores as (select EMP_NO, avg(SCORE) as SCORE from HR_GRADE group by 1)

select e.EMP_NO, e.EMP_NAME, 
        case when s.SCORE >= 96 then "S"
            when s.SCORE >= 90 then "A" 
            when s.SCORE >= 80 then "B" else "C" end as GRADE,
        case when s.SCORE >= 96 then e.SAL * 0.2
            when s.SCORE >= 90 then e.SAL * 0.15
            when s.SCORE >= 80 then e.SAL * 0.1 else 0 end as BONUS
from HR_EMPLOYEES as e left join scores as s on e.EMP_NO = s.EMP_NO
order by 1 asc;