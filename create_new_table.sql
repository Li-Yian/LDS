USE Group_ID_3_DB;
CREATE TABLE [geography](
[geo_id] INT PRIMARY KEY NOT NULL,
[latitude] FLOAT,
[longitude] FLOAT,
[city] VARCHAR(255),
[state] VARCHAR(255),
[continent] VARCHAR(255)
);

CREATE TABLE [dates](
[date_id] INT PRIMARY KEY NOT NULL,
[date] DATE,
[day] INT,
[month] INT,
[year] INT,
[quarter] INT,
[day_of_the_week] VARCHAR(10)
);