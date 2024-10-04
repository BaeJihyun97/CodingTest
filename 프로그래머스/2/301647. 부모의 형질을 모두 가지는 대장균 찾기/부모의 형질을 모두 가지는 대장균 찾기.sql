-- 코드를 작성해주세요
select e.ID, e.GENOTYPE, p.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA as e join ECOLI_DATA as p on e.PARENT_ID = p.ID
where e.GENOTYPE & p.GENOTYPE = p.GENOTYPE
order by e.ID asc;