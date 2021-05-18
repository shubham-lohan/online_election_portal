# Project मतदान(Translation: Poll)

A mini-world databse to manage Delhi elctions on an online platform. This was created as a group project under the course Fundamentals of Database Systems - CSE-202 under the guidance of Dr. Mukesh Mohania.

>## Problem Statement

The Election Commission is planning to conduct state level elections in Delhi.It has approached our organisation MangoDB to create an online portal for this massive undertaking.

Using the Portal :
* Voters vote during the election
* Candidates can register themselves for the election and make/associate with candidates
* Media can fetch data and perform analysis
* Verification Official verifies documents for voters and candidates
* Election Official manages all the activities

>## Stakeholders

The following stakeholders will use our application : 
* Voters 
* Candidates
* Journalists / Media / Common Public
* Election Commision Officials
* Verification Authority

## Features

>### ER Diagram

* Created an ER diagram for designing the database which helped fill get a clear idea about decide the various logic elements needed for building the database.
* Created several entities and relationships between the entities which are necessary for organised functioning in a proper manner.
* Includes a few but necessary weak entities and an essential tertiary relationship which reduce several complexities in the project. 

>### Database Schema

* Created clear and well-defined schemas for all the necessary entities and relationships which were used for populating the DB.
* Database normalisation was done upto Fourth Normal Form(4NF) to eliminate redundancies, insertion, deletion and update anomalies.

>### Database Population

* Made over 10,000+ data entries into the DB.
* Several relations include attributes of `BLOB` data type for storing documents such as aadhaar card of voters, criminal history of candidates etc.

#### SQL Server

Hosted the DB on AWS for easier collaboration and access to the DB by all team members.

##### Details:

* username: demo
* password: q\`?x-\[%zx4S(Fv?e
* hostname: 31.220.51.212

>### SQL Queries
(to-do)

>### Web Portal
(to-do)

### References:
(to-do)
Embedded Query 4- 
https://stackoverflow.com/questions/1294385/how-to-insert-retrieve-a-file-stored-as-a-blob-in-a-mysql-db-using-python for inserting blob object into mysql db.
