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

