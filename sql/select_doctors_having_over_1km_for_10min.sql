SELECT d.name, SUM(l.distance) AS total_distance
FROM doctors d
JOIN locations l ON d.id = l.doctor_id
WHERE l.time_stamp >= NOW() - INTERVAL '10 minutes'
GROUP BY d.name
HAVING SUM(l.distance) > 1000;