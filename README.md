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

<<<<<<< HEAD
## Phase 2: Quaries
### Database Updates & Constraints


### Updates and Enhancements  
This phase refines database logic, implements constraints, and adds advanced querying capabilities.  

#### 1. **Data Updates**  
- **Release Date Adjustment**: Discharge dates now auto-set to **3 days after birth**. 
  - *The Code*:
    ![The Code](stage%202/resources/update%203%20days%20after%20birth.png)
  - *Before*:  
    ![Unsorted Dates](stage%202/resources/before%20update.png)  
  - *After*:  
    ![Updated Dates](stage%202/resources/after.png)  

- **Room Occupancy Logic**: Rooms marked "occupied" only if **two mothers** are assigned.  
  - *The Code*:
    ![The Code](stage%202/resources/occupied%20code.png)
  - *Before*:  
    ![Room Before](stage%202/resources/before%20occupied.png)  
  - *After*:  
    ![Room After](stage%202/resources/after%20occupied.png)  

- **Mother Data Correction**: Updated phone number for Mother ID 34.
  - *The Code*:
    ![The Code](stage%202/resources/34%20maternity.png)  
  - *Before*:  
    ![Phone Before](stage%202/resources/before%2034.png)  
  - *After*:  
    ![Phone After](stage%202/resources/after%2034.png)  

---

#### 2. **Table Constraints**  
1. **Default Room Status**: New rooms default to "available".  
   ![Constraint 1](stage%202/resources/default%20to%20clear%20room.png)  
2. **Mother Age Validation**: Blocks invalid ages (e.g., <18 or >50).  
   ![Constraint 2](stage%202/resources/constrain%20mother%20age.png)  
3. **NULL Prevention**: Ensures baby records have no NULL values.  
   ![Constraint 3](stage%202/resources/constraint%20beby%20null.png)  

---

#### 3. **Data Deletions**  
1. **Purge Old Records**: Deleted births before `2024-04-07`.
   - *The Code*:
    ![The Code](stage%202/resources/delete%20date.png)  
   - *Before*:  
     ![Before Deletion](stage%202/resources/before%20delete%20date.png)  
   - *After*:  
     ![After Deletion](stage%202/resources/after%20delete%20date.png)  

2. **Remove Inexperienced Doctors**: Deleted doctors with **0 years** of cesarean experience.
   - *The Code*:
    ![The Code](stage%202/resources/0%20seniority.png)  
   - *Before*:  
     ![Doctors Before](stage%202/resources/before%20seniority.png)  
   - *After*:  
     ![Doctors After](stage%202/resources/after%20seniority.png)  

3. **Unassigned Nurses**: Removed nurses not linked to any room.
   - *The Code*:
    ![The Code](stage%202/resources/nurses%20no%20room.png)  
   - *Before*:  
     ![Nurses Before](stage%202/resources/before%20nurses.png)  
   - *After*:  
     ![Nurses After](stage%202/resources/after%20nurses.png)  

---

#### 4. **Advanced Queries**  
| #  | Query Purpose | Screenshot | Output |
|----|---------------|------------|--------|
| 1  | Rooms with 1 mother + night-shift nurse | ![Query 1](stage%202/resources/1%20query.png) | ![Result 1](stage%202/resources/1.1%20query.png) |
| 2  | Mothers with multiple births on same date | ![Query 2](stage%202/resources/2%20query.png) | ![Result 2](stage%202/resources/2.2%20query.png) |
| 3  | Avg baby weight per birth type (last year) | ![Query 3](stage%202/resources/3%20query.png) | ![Result 3](stage%202/resources/3.3%20query.png) |
| 4  | Nurses caring for ~2 babies/room | ![Query 4](stage%202/resources/4%20query.png) | ![Result 4](stage%202/resources/4.4%20query.png) |
| 5  | Monthly birth rate averages | ![Query 5](stage%202/resources/5%20query.png) | ![Result 5](stage%202/resources/5.5%20query.png) |
| 6  | Natural births by experienced doctors (≥2 yrs) | ![Query 6](stage%202/resources/6%20query.png) | ![Result 6](stage%202/resources/6.6%20query.png) |
| 7  | Male cesarean babies (mothers aged 30+, 1 child) | ![Query 7](stage%202/resources/7%20query.png) | ![Result 7](stage%202/resources/7.7%20quey.png) |
| 8  | Nurses/mothers in Room 10 (May) | ![Query 8](stage%202/resources/8%20query.png) | ![Result 8](stage%202/resources/8.8%20query.png) |

*(Add rows for additional queries as needed.)*  

---

#### 5. **Transaction Management**  
- **Rollback Example**:
  - *The Code*:
    ![The Code](stage%202/resources/rollback1.png)  
  - *Before*: ![Pre-Rollback](stage%202/resources/rollback2.png)
  - *Update*: ![while-Rollback](stage%202/resources/rollback3.png)  
  - *After*: ![Post-Rollback](stage%202/resources/rollback4.png)  

- **Commit Example**:  
  - *The Code*:
    ![The Code](stage%202/resources/commit.png)  
  - *Before*: ![Pre-commit](stage%202/resources/commit1.png)  
  - *After*: ![Post-commit](stage%202/resources/commit2.png)
  - *After Commit*: ![after-commit](stage%202/resources/commit3.png)  

---

### Next Steps  
- **Phase 3**: UI development and performance tuning.  

---

<<<<<<< HEAD
3. **Birth Type and Baby Weight Correlation**  
   Query calculating average baby weight by delivery type over the past year.
   
   ![Weight Analysis Query](stage%202/resources/weight_analysis_query.png)
   
   Results:
   ![Weight Analysis Results](stage%202/resources/weight_analysis_results.png)

4. **Nurse Workload Analysis**  
   Query identifying nurses who cared for exactly 2 babies per room on average.
   
   ![Nurse Workload Query](stage%202/resources/nurse_workload_query.png)
   
   Results:
   ![Nurse Workload Results](stage%202/resources/nurse_workload_results.png)

5. **Monthly Birth Statistics**  
   Query calculating average births per month throughout the year.
   
   ![Monthly Stats Query](stage%202/resources/monthly_stats_query.png)
   
   Results:
   ![Monthly Stats Results](stage%202/resources/monthly_stats_results.png)

6. **Natural Birth and Doctor Experience**  
   Query listing natural births and their attending doctors, excluding those with less than two years' experience.
   
   ![Natural Birth Query](stage%202/resources/natural_birth_query.png)
   
   Results:
   ![Natural Birth Results](stage%202/resources/natural_birth_results.png)

7. **Comprehensive Birth Analysis**  
   Complex query returning baby information, mother details, birth type, and baby count for mothers over 30 with male babies delivered by cesarean section.
   
   ![Comprehensive Query](stage%202/resources/comprehensive_query.png)
   
   Results:
   ![Comprehensive Results](stage%202/resources/comprehensive_results.png)

8. **Room Occupancy by Shift**  
   Query showing nurse names, shifts, and number of mothers in room 10 during May.
   
   ![Room Occupancy Query](stage%202/resources/room_occupancy_query.png)
   
   Results:
   ![Room Occupancy Results](stage%202/resources/room_occupancy_results.png)

### Transaction Management

The database implements transaction control to ensure data integrity:

1. **Rollback Operations**  
   Capability to revert changes when necessary, preserving data integrity.
   
   Initial state:
   ![Initial State](stage%202/resources/initial_state.png)
   
   After update:
   ![Updated State](stage%202/resources/updated_state.png)
   
   After rollback:
   ![Rollback State](stage%202/resources/rollback_state.png)

2. **Commit Operations**  
   Finalizing changes to make them permanent in the database.
   
   Before update:
   ![Pre-Commit State](stage%202/resources/precommit_state.png)
   
   After update:
   ![Post-Update State](stage%202/resources/postupdate_state.png)
   
   After commit:
   ![Post-Commit State](stage%202/resources/postcommit_state.png)

## Conclusion

The Maternity Ward Database provides a comprehensive solution for managing hospital maternity departments. Through a well-designed data structure, targeted constraints, and powerful analytical capabilities, the system offers an efficient way to manage births, track patient information, coordinate medical staff, and optimize resource allocation.

The implementation demonstrates best practices in database design, including proper relationship modeling, constraint implementation, transaction management, and analytical query capabilities. This ensures data integrity while providing valuable insights to improve hospital operations and patient care.

## Phase 3: Integration

