SELECT ID, IF (SIZE_OF_COLONY > 1000, "HIGH", IF(SIZE_OF_COLONY <= 1000 AND SIZE_OF_COLONY > 100, "MEDIUM", "LOW"))AS SIZE FROM ECOLI_DATA
ORDER BY ID