CREATE INDEX idx_doctors_id ON doctors (id);
CREATE INDEX idx_locations_doctor_id ON locations (doctor_id); 
CREATE INDEX idx_locations_timestamp ON locations (time_stamp);