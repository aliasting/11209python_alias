SELECT 站點名稱,MAX(更新時間)AS更新時間,行政區,地址 ,總車輛數,可借,可還
FROM 台北市YOUBIKE
GROUP BY 站點名稱 
HAVING 站點名稱 like'%三%'