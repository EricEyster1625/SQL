 
 IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'TESTDATA')
	DROP TABLE TESTDATA
GO
 create table testdata ( 
	ID INT IDENTITY(1,1)
	,RUNDATE DATETIME2
	,CONSTRAINT PK_TESTDATA  PRIMARY KEY CLUSTERED (ID)


	)

GO

DECLARE @I INT = 0 
WHILE @I < 1000
BEGIN
	INSERT INTO TESTDATA (RUNDATE) 
	VALUES (GETDATE())
	SET @I = @I + 1 
END


SELECT * 
FROM testdata
WHERE RUNDATE < DATEADD(SECOND, -1 , GETDATE() ) 