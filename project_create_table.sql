CREATE TABLE particpiant (
		participant_id INT PRIMARY KEY NOT NULL,
		participant_age_group varchar(50),
		participant_gender varchar(10),
		participant_status varchar(50),
		participant_type varchar(50)
);

CREATE TABLE gun (
		gun_id INT PRIMARY KEY NOT NULL,
		gun_stolen varchar(50),
		gun_type varchar(50),
);

CREATE TABLE custody (
		custody_id INT PRIMARY KEY NOT NULL,
		participant_id INT,
		gun_id INT NOT NULL,
		geo_id INT NOT NULL,
		date_id INT NOT NULL,
		incident_id INT NOT NULL,
		crime_gravity INT NOT NULL
);


