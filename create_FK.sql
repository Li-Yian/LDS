USE Group_ID_3_DB;
CREATE TABLE [custody] 
   (
      [custody_id] INT NOT NULL,
	  [participant_id] INT NOT NULL,
	  [gun_id] INT NOT NULL,
	  [geo_id] INT NOT NULL,
	  [date_id] INT NOT NULL,
	  [crime_gravity] INT NOT NULL,
	  [incident_id] INT NOT NULL
      , CONSTRAINT FK_custody_participant FOREIGN KEY (participant_id)
        REFERENCES [participant] (participant_id)
	  , CONSTRAINT FK_custody_gun FOREIGN KEY (gun_id)
	    REFERENCES [gun] (gun_id)
	  , CONSTRAINT FK_custody_geography FOREIGN KEY (geo_id)
	    REFERENCES [geography] (geo_id)
	  , CONSTRAINT FK_custody_dates FOREIGN KEY (date_id)
        REFERENCES [dates] (date_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
   )
;