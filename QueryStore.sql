

--ENABLE QUERY STORE ON A DATABASE
ALTER DATABASE Logistics
SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE);

--ENABLE USING WAIT STATS
ALTER DATABASE Logistics
SET QUERY_STORE = ON ( WAIT_STATS_CAPTURE_MODE = ON );


--QUERY STORE SETTINGS 
select * 
from sys.database_query_store_options


--WHAT IS IN STORE FOR YOU
SELECT Txt.query_text_id, Txt.query_sql_text, Pl.plan_id, CAST(QUERY_PLAN AS  XML)  AS QueryPlan, Qry.*
FROM sys.query_store_plan AS Pl
INNER JOIN sys.query_store_query AS Qry
    ON Pl.query_id = Qry.query_id
INNER JOIN sys.query_store_query_text AS Txt
    ON Qry.query_text_id = Txt.query_text_id;


SELECT * 
FROM SYS.query_store_wait_stats

select * 
from sys.query_store_plan


EXEC sp_query_store_flush_db

--Force a plan 
--Get the query and plan ID from sys.query_store_plan
EXEC sp_query_store_force_plan
    @query_id = 105,
    @plan_id = 10;
