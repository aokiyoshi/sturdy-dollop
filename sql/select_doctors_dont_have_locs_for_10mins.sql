SELECT d.name
FROM doctors d
LEFT JOIN locations l ON d.id = l.doctor_id
WHERE l.doctor_id IS NULL OR l.time_stamp < datetime('now', '-10 minutes');