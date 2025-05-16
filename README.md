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
### Database Updates & Constraints

#### Data Updates

The second phase involved several important data updates to optimize the database:

1. **Discharge Date Standardization**  
   All discharge dates were updated to be exactly 3 days after the birth date, ensuring consistency in patient stays.
   
   ![Discharge Date Update](stage%202/resources/discharge_date_update.png)

2. **Room Occupancy Status**  
   Room status was updated to mark rooms as "Occupied" only when they contain two mothers, improving resource allocation.
   
   Before update:
   ![Room Status Before](stage%202/resources/room_status_before.png)
   
   After update:
   ![Room Status After](stage%202/resources/room_status_after.png)

3. **Patient Contact Information**  
   Updated contact information for specific patients when necessary, such as phone number updates.
   
   Before update:
   ![Contact Before](stage%202/resources/contact_before.png)
   
   After update:
   ![Contact After](stage%202/resources/contact_after.png)

#### Table Constraints

To maintain data integrity, the following constraints were implemented:

1. **Default Room Status**  
   Default constraint that automatically marks new rooms as "Available" when added to the database.
   
   ![Default Room Status](stage%202/resources/default_room_status.png)

2. **Mother Age Validation**  
   Check constraint that validates the mother's age is within a reasonable range when new records are inserted.
   
   ![Age Validation](stage%202/resources/age_validation.png)

3. **Baby Data Validation**  
   Not-null constraint ensuring all required baby information fields are populated.
   
   ![Baby Data Validation](stage%202/resources/baby_validation.png)

### Data Cleanup Operations

Several cleanup operations were performed to maintain database quality:

1. **Historical Record Removal**  
   Deleted birth records prior to April 7, 2024 to maintain relevant data only.
   
   Before deletion:
   ![Historical Records Before](stage%202/resources/historical_before.png)
   
   After deletion:
   ![Historical Records After](stage%202/resources/historical_after.png)

2. **Staff Qualification Filtering**  
   Removed doctors with zero years of experience in cesarean specialization.
   
   Before filtering:
   ![Doctors Before](stage%202/resources/doctors_before.png)
   
   After filtering:
   ![Doctors After](stage%202/resources/doctors_after.png)

3. **Unassigned Staff Cleanup**  
   Deleted nurse records not associated with any room to maintain data relevance.
   
   Before cleanup:
   ![Nurses Before](stage%202/resources/nurses_before.png)
   
   After cleanup:
   ![Nurses After](stage%202/resources/nurses_after.png)

### Advanced Queries

The database supports various analytical queries to extract valuable insights:

1. **Room and Night Shift Nurse Assignment**  
   Query returning rooms with single mothers and their assigned night shift nurses.
   
   ![Room-Nurse Query](stage%202/resources/room_nurse_query.png)
   
   Results:
   ![Room-Nurse Results](stage%202/resources/room_nurse_results.png)

2. **Multiple Birth Analysis**  
   Query identifying mothers who delivered more than one baby on the same date and their delivery types.
   
   ![Multiple Births Query](stage%202/resources/multiple_births_query.png)
   
   Results:
   ![Multiple Births Results](stage%202/resources/multiple_births_results.png)

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

## Future Enhancements