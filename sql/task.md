1. Предложите описание используемых таблиц в базе данных, включая информацию 
о названиях и формате полей. 

CREATE TABLE doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    latitude REAL NOT NULL, // Долгота
    longitude REAL NOT NULL, // Широта
    distance INTEGER NOT NULL, // Расстояние, которое пройдено, чтобы дойти до этой точки
    time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, // Время когда зафиксировано местоположение
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

2. Предложите индексы для каждой из таблиц, которые помогут быстрее 
выдавать информацию по идентификатору врача.

CREATE INDEX idx_doctors_id ON doctors (id);
CREATE INDEX idx_locations_doctor_id ON locations (doctor_id); 
CREATE INDEX idx_locations_timestamp ON locations (time_stamp);

3. Какие параметры должно принимать API на серверах проекта, чтобы можно 
было сохранять местонахождение того или иного врача? 

    id врача, новые координаты и расстояние 

4. Напишите SQL-запрос, который выведет информацию о врачах, которые 
в последние 10 минут переместились более чем на 1 км.

SELECT d.name, SUM(l.distance) AS total_distance
FROM doctors d
JOIN locations l ON d.id = l.doctor_id
WHERE l.time_stamp >= NOW() - INTERVAL '10 minutes'
GROUP BY d.name
HAVING SUM(l.distance) > 1000;

5. Напишите SQL-запрос, который выведет всех врачей, 
для которых нет информации об их перемещениях за последний час.

SELECT d.name
FROM doctors d
LEFT JOIN locations l ON d.id = l.doctor_id
WHERE l.doctor_id IS NULL OR l.time_stamp < datetime('now', '-10 minutes');