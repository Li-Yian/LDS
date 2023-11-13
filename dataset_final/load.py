#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:31:18 2023

@author: yian
"""
import pandas as pd
import pyodbc

# connect database
server = 'tcp:lds.di.unipi.it'
database = 'Group_ID_3_DB'
username = 'Group_ID_3'
password = 'XHG33RAE'

# CSV file path
custody = 'custody.csv'
participant = 'participant.csv'
gun = 'gun.csv'
dates = 'dates.csv'
geography = 'geography.csv'

# SQL Server connect string
connectionString = (
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + server
        + ";DATABASE="
        + database
        + ";UID="
        + username
        + ";PWD="
        + password
    )
# create database connection
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()


# read CSV to DataFrame
df = pd.read_csv(custody)
df_p = pd.read_csv(participant)
df_gun = pd.read_csv(gun)
df_dates = pd.read_csv(dates)
df_geo = pd.read_csv(geography)

# insert data into table
'''
insert_query = "INSERT INTO custody (custody_id, participant_id, gun_id, date_id, crime_gravity, incident_id, geography_id) VALUES (?, ?, ?, ?, ?, ?, ?)"

for index, row in df.iterrows():
    values = tuple(row)
    cursor.execute(insert_query, values)
    cnxn.commit()
'''
insert_participant = "INSERT INTO participant (participant_id, participant_type, paticipant_age_group, participant_gender, participant_status) VALUES (?, ?, ?, ?, ?)"

for index, row in df_p.iterrows():
    values = tuple(row)
    cursor.execute(insert_participant, values)
    cnxn.commit()

insert_gun = "INSERT INTO gun (gun_id, gun_stolen, gun_type) VALUES (?, ?, ?)"

for index, row in df_gun.iterrows():
    values = tuple(row)
    cursor.execute(insert_gun, values)
    cnxn.commit()
'''
insert_dates = "INSERT INTO dates (date_id, date, day, month, year, quarter, day_of_the_week) VALUES (?, ?, ?, ?, ?, ?, ?)"

for index, row in df_dates.iterrows():
    values = tuple(row)
    cursor.execute(insert_dates, values)
    cnxn.commit()
'''
insert_geo = "INSERT INTO geography (geo_id, latitude, longitude, city, state, continent) VALUES (?, ?, ?, ?, ?, ?)"

for index, row in df_geo.iterrows():
    values = tuple(row)
    cursor.execute(insert_geo, values)
    cnxn.commit()

# close connect
cursor.close()
cnxn.close()
