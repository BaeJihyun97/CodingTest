-- 코드를 작성해주세요
with recursive findGeneration(ID, PARENT_ID, GENERATION) AS (
    select ID, PARENT_ID, 1 as GENERATION from ECOLI_DATA where PARENT_ID is null
    union all
    select e.ID, e.PARENT_ID, 1 + f.GENERATION
        from findGeneration as f join ECOLI_DATA as e on f.ID = e.PARENT_ID
        where f.GENERATION < 3
)

select ID from findGeneration where GENERATION = 3;