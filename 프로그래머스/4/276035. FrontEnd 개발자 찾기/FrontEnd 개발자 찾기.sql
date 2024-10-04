-- 코드를 작성해주세요
with fe as (
    select CODE from SKILLCODES where CATEGORY="Front End"
)
select DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME from DEVELOPERS as d, fe
where d.SKILL_CODE & fe.CODE = fe.CODE
order by 1 asc;