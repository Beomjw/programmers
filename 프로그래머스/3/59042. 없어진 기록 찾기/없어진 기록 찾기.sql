SELECT B.ANIMAL_ID, B.NAME FROM ANIMAL_OUTS AS B LEFT JOIN ANIMAL_INS AS A ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL 
ORDER BY ANIMAL_ID


