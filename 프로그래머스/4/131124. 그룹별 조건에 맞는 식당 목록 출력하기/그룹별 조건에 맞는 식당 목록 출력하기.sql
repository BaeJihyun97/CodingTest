-- 코드를 입력하세요
with rc as (
    SELECT MEMBER_ID, count(*) as REVIEW_COUNT from REST_REVIEW
    group by MEMBER_ID),
mx as (
    select r.MEMBER_ID, r.REVIEW_COUNT, m.MEMBER_NAME from rc as r join MEMBER_PROFILE as m on r.MEMBER_ID = m.MEMBER_ID
    where r.REVIEW_COUNT = (select max(REVIEW_COUNT) from rc) 
)
select m.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, '%Y-%m-%d')  
from mx as m join REST_REVIEW as r where m.MEMBER_ID = r.MEMBER_ID
order by 3, 2;