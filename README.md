# DBProject_3333_-2364
# Maternity Ward Database

Hospital Maternity Department Management System

## Table of Contents  
- [Phase 1: Design and Build the Database](#phase-1-design-and-build-the-database)  
  - [Introduction](#introduction)  
  - [ERD (Entity-Relationship Diagram)](#erd-entity-relationship-diagram)  
  - [DSD (Data Structure Diagram)](#dsd-data-structure-diagram)  
  - [SQL Scripts](#sql-scripts)  
  - [Data](#data)
  - [Backup](#backup)  
- [Phase 2: Integration](#phase-2-integration)  

## Phase 1: Design and Build the Database  

### Introduction

The **Maternity Ward Database** is designed to efficiently manage information related to births, mothers, babies, medical staff, and hospital rooms. This system ensures smooth organization and tracking of essential details such as birth records, doctor assignments, baby information, and patient accommodations.

#### Purpose of the Database
This database serves as a structured and reliable solution for hospital maternity departments to:  
- **Manage birth records** including birth dates, discharge dates, and birth types (cesarean/regular).
- **Track patient information** by storing details about mothers and their babies.
- **Coordinate medical staff** by linking doctors and nurses to specific patients and rooms.
- **Monitor room availability** to efficiently allocate resources.
- **Store essential details** such as baby weight, doctor specialties, and nurse shift schedules.

#### Potential Use Cases
- **Hospital Administrators** can use this database to efficiently track births, assign staff, and manage room availability.
- **Medical Staff** can access patient information, birth details, and coordinate care.
- **Mothers** can have their information and that of their babies properly documented.
- **Management** can use the system for record-keeping, scheduling, and resource allocation.

This structured database helps streamline maternity ward operations, improving organization, patient care, and communication among all parties involved.

###  ERD (Entity-Relationship Diagram)    
![ERD Diagram](stage%201/resources/erd.png)  

###  DSD (Data Structure Diagram)   
![DSD Diagram](stage%201/resources/dsd.png)  

###  SQL Scripts  
Provide the following SQL scripts:  
- **Create Tables Script** - The SQL script for creating the database tables is available in the repository  
- **Insert Data Script** - The SQL script for inserting data to the database tables is available in the repository  
- **Drop Tables Script** - The SQL script for dropping all tables is available in the repository  
- **Select All Data Script**  - The SQL script for selecting all tables is available in the repository  
  
###  Data  
####  First tool: using [mockaro](https://www.mockaroo.com/) to create csv files
We used Mockaroo to generate realistic test data for our database entities including:
- Maternity (mothers) information
- Baby details
- Doctor records
- Nurse information
- Room data
- Birth records

Example of data generation using Mockaroo:
📜 **[Mockaroo files](stage%201/Filesmockaroo)**
![Mockaroo Data Generation](stage%201/resources/mockaroo.png)

####  Second tool: using GenerateData files
Example of data generation using GenerateData:
📜 **[GenerateData files](stage%201/generatedataFiles)**
![GenerateData Data Generation](stage%201/resources/generatedata.png)

####  Third tool: using text files
Additional data was imported using text files to populate the database tables:
📜 **[Text files](stage%201/DataImportFiles/maternity.csv)**
![Text File Data Import](stage%201/resources/txt.png)

### Backup 
- Backup procedures were implemented to ensure data safety:

#### Creating backup folders with today's date:
![Backup Creation](stage%201/resources/create.png)  

#### Data backup process:
![Data backup](stage%201/resources/databackup.png)

#### Data restoration process:
![Data Restoration](stage%201/resources/datarestore.png)

## Phase 2: Integration
