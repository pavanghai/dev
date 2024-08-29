/*
Assuming we have a table with below records
Table Name Student 
------------------------------------------
CLASS  |   roolNo   |  DOB      |  Name  
------------------------------------------
ten    |   A025     | 19780101  |  Raj   
------------------------------------------
ten    |   A024     | 19780101  |  Shyam 
------------------------------------------
three  |   A023     | 19780101  |  sam   
------------------------------------------
ten    |   A020     | 19780101  |  rohit 
------------------------------------------
We want to update records if available, else insert below records 

five   |   A024     | 19780101  |  Shyam 
------------------------------------------
five   |   A023     | 19780101  |  sam   
------------------------------------------
ten    |   A019     | 19780101  |  shivam
------------------------------------------
five   |   A018     | 19780101  |  Raj 
------------------------------------------

In this example records for Shyam, Sam, Raj will be updated and shivam will be inserted
*/

SET SERVEROUTPUT ON ; -- Display output
SET ECHO ON ;
DECLARE
    V_CNT NUMBER; 
BEGIN
    MERGE INTO Student s
    USING (
        SELECT 'five' AS class, 'A024' AS rollNo, TO_DATE('19780101', 'YYYYMMDD') AS DOB, 'Shyam' AS name FROM dual UNION ALL
        SELECT 'five' AS class, 'A023' AS rollNo, TO_DATE('19780101', 'YYYYMMDD') AS DOB, 'sam' AS name FROM dual UNION ALL
        SELECT 'ten' AS class, 'A019' AS rollNo, TO_DATE('19780101', 'YYYYMMDD') AS DOB, 'shivam' AS name FROM dual UNION ALL
        SELECT 'five' AS class, 'A018' AS rollNo, TO_DATE('19780101', 'YYYYMMDD') AS DOB, 'raj' AS name FROM dual
    ) src
    ON (s.rollNo = src.rollNo)
    WHEN MATCHED THEN
        UPDATE SET s.class = src.class, s.name = src.name, s.DOB = src.DOB
    WHEN NOT MATCHED THEN
        INSERT (class, rollNo, DOB, name)
        VALUES (src.class, src.rollNo, src.DOB, src.name);

    V_CNT := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE('Number of records modified: ' || V_CNT);
END;
/
