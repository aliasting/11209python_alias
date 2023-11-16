/*1110*/
SELECT 站點名稱,(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還
    FROM 台北市youbike
WHERE 更新時間 IN (
	SELECT MAX (更新時間)
	FROM 台北市youbike
	GROUP BY 站點名稱 )

/*方法1:概念是將目前 table 同時命名為「a」,「b」後，
用 join 語法來達成自己與自己比對資料的結果，
再用 select distinct 的功能刪除重複資料*/
select a.* from 台北市youbike a
join (select distinct 站點名稱,max(更新時間) 更新時間
from 台北市youbike group by 站點名稱) b
on a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱

/*方法2:這是postgreSQL的特別語法,取得最新時間*/
SELECT *
FROM 台北市youbike
WHERE (更新時間,站點名稱) IN (
	SELECT MAX(更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱) 
/*搜尋站點*/
SELECT *
FROM 台北市youbike
WHERE (更新時間,站點名稱) IN (
	SELECT MAX(更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱
) AND 站點名稱 like '%台北%'

/*1116*/
SELECT *
FROM 台北市youbike
WHERE (更新時間,站點名稱) IN (
	SELECT MAX (更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱 )
AND 站點名稱 like '%台北%'

	