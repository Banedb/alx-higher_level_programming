-- displays the average temperature by city ordered by temp
USE hbtn_0c_0;
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
