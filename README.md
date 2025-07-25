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
- [Phase 2: Integration](#phase-2-Queries)  
   - [Database Updates & Constraints](#database-updates--constraints)
   - [Data Updates](#data-updates)
   - [Table Constraints](#table-constraints)
   - [Data Cleanup Operations](#data-cleanup-operations)
   - [Advanced Queries](#advanced-queries)
   - [Transaction Management](#transaction-management)
   - [Conclusion](#conclusion-2)
- [Phase 3: Integration](#phase-3-Integration)
   - [Integrations with 2 different data-bases](#integrations-with-2-different-data-bases)
   - [New ERD](#new-erd)
   - [New DSD](#new-dsd)
   - [Combination ERD](#combination-erd)
   - [Combination DSD](#combination-dsd)
   - [Views](#views)
   - [Conclusion](#conclusion-3)
- [Phase 4: Programs](#phase-4-programs)
   - [Programs and Triggers on the Data-base](#programs-and-triggers-on-the-data-base)
   - [Programs](#programs)
   - [Triggers](#triggers)
   - [Conclusion](#conclusion-4)
- [Phase 5: GUI](#phase-5-gui)
   - [Gui for Managing the Maternity department](#graphical-user-interface-for-managing-the-maternity-department)
   - [Technologies used](#technologies-used)
   - [Login screen](#login-screen)
   - [Data display](#data-display)
   - [Data oprations display](#data-operations-display)
   - [Query display](#query-display)
   - [Program display](#program-display)
   - [Conclusion 5](#conclusion-5)

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

## Phase 2: Quaries
### Database Updates & Constraints

#### Data Updates

The second phase involved several important data updates to optimize the database:

1. **Discharge Date Standardization**  
   All discharge dates were updated to be exactly 3 days after the birth date, ensuring consistency in patient stays.
   
   ![Discharge Date Update](stage%202/resources/discharge_date_update.png)

   Before update:
   ![Date Status Before](stage%202/resources/historical_before.png)
   
   After update:
   ![Date Status After](stage%202/resources/historical_after.png)

2. **Room Occupancy Status**  
   Room status was updated to mark rooms as "Occupied" only when they contain two mothers, improving resource allocation.
   
   ![Room Update](stage%202/resources/occupied_code.png)

   Before update:
   ![Room Status Before](stage%202/resources/room_status_before.png)
   
   After update:
   ![Room Status After](stage%202/resources/room_status_after.png)

3. **Patient Contact Information**  
   Updated contact information for specific patients when necessary, such as phone number updates.
   
   ![Patient Contact Update](stage%202/resources/maternity.png)

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
   
   ![Age Validation](stage%202/resources/mother_age_validation.png)

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
   
   ![Room-Nurse Query](stage%202/resources/1%20query.png)
   
   Results:
   ![Room-Nurse Results](stage%202/resources/1.1%20query.png)

2. **Multiple Birth Analysis**  
   Query identifying mothers who delivered more than one baby on the same date and their delivery types.
   
   ![Multiple Births Query](stage%202/resources/2%20query.png)
   
   Results:
   ![Multiple Births Results](stage%202/resources/2.2%20query.png)

3. **Birth Type and Baby Weight Correlation**  
   Query calculating average baby weight by delivery type over the past year.
   
   ![Weight Analysis Query](stage%202/resources/3%20query.png)
   
   Results:
   ![Weight Analysis Results](stage%202/resources/3.3%20query.png)

4. **Nurse Workload Analysis**  
   Query identifying nurses who cared for exactly 2 babies per room on average.
   
   ![Nurse Workload Query](stage%202/resources/4%20query.png)
   
   Results:
   ![Nurse Workload Results](stage%202/resources/4.4%20query.png)

5. **Monthly Birth Statistics**  
   Query calculating average births per month throughout the year.
   
   ![Monthly Stats Query](stage%202/resources/5%20query.png)
   
   Results:
   ![Monthly Stats Results](stage%202/resources/5.5%20query.png)

6. **Natural Birth and Doctor Experience**  
   Query listing natural births and their attending doctors, excluding those with less than two years' experience.
   
   ![Natural Birth Query](stage%202/resources/6%20query.png)
   
   Results:
   ![Natural Birth Results](stage%202/resources/6.6%20query.png)

7. **Comprehensive Birth Analysis**  
   Complex query returning baby information, mother details, birth type, and baby count for mothers over 30 with male babies delivered by cesarean section.
   
   ![Comprehensive Query](stage%202/resources/7%20query.png)
   
   Results:
   ![Comprehensive Results](stage%202/resources/7.7%20query.png)

8. **Room Occupancy by Shift**  
   Query showing nurse names, shifts, and number of mothers in room 10 during May.
   
   ![Room Occupancy Query](stage%202/resources/8%20query.png)
   
   Results:
   ![Room Occupancy Results](stage%202/resources/8.8%20query.png)

### Transaction Management

The database implements transaction control to ensure data integrity:

1. **Rollback Operations**  
   Capability to revert changes when necessary, preserving data integrity.
   
   Initial state:
   ![Initial State](stage%202/resources/rollback2.png)
   
   After update:
   ![Updated State](stage%202/resources/rollback3.png)
   
   After rollback:
   ![Rollback State](stage%202/resources/rollback4.png)

2. **Commit Operations**  
   Finalizing changes to make them permanent in the database.
   
   Before update:
   ![Pre-Commit State](stage%202/resources/commit1.png)
   
   After update:
   ![Post-Update State](stage%202/resources/commit2.png)
   
   After commit:
   ![Post-Commit State](stage%202/resources/commit3.png)

## Conclusion 2

The Maternity Ward Database provides a comprehensive solution for managing hospital maternity departments. Through a well-designed data structure, targeted constraints, and powerful analytical capabilities, the system offers an efficient way to manage births, track patient information, coordinate medical staff, and optimize resource allocation.

The implementation demonstrates best practices in database design, including proper relationship modeling, constraint implementation, transaction management, and analytical query capabilities. This ensures data integrity while providing valuable insights to improve hospital operations and patient care.

## Phase 3: Integration
### Integrations with 2 different data-bases

At this stage, we have experimented integrating our system.
First, we got a pair's other data-base and according to the tables, we have created their ERD:

1. CancerPatient
Primary Key: patient_id
Foreign Keys:-

2. Department
Primary Key: department_id
Foreign Keys: -

3. OncologyStaff
Primary Key: staff_id
Foreign Keys: department_id → Department(department_id)

4. Diagnosis
Primary Key: diagnosis_id
Foreign Keys: patient_id → CancerPatient(patient_id)
staff_id → OncologyStaff(staff_id)

5. TreatmentPlan
Primary Key: plan_id
Foreign Keys: diagnosis_id → Diagnosis(diagnosis_id)

6. TreatmentSession
Primary Key: session_id
Foreign Keys: plan_id → TreatmentPlan(plan_id)
staff_id → OncologyStaff(staff_id)

7. SideEffectReport
Primary Key: report_id
Foreign Keys: session_id → TreatmentSession(session_id)
staff_id → OncologyStaff(staff_id) 

### New ERD
Based on the conclusions of the tables we created the ERD:
![ERD](stage%203/Images/New_ERD.png)

### New DSD
DSD:
   ![DSD](stage%203/Images/New_DSD.png)

Integrating the two databases into one combined database:

After we uploaded their data-base to ours, We made their tables as foreign tables in our database.
Then, we operated design actions in order to integrat both of the data-bases.
Based on the "Department" table, their data-base, we connected "Department" table primary key as a foreign key in "Doctor"&"Nurse" tables, in our data-base.
As well as the "department_id" = 7 , represents "maternity department":
Doctor table:
   ![Doctor](stage%203/Reasources/update_doctor_table.png)
Nurse table:
   ![Nurse](stage%203/Reasources/update_nurse_table.png)

### Combinated ERD
Combinated ERD:
   ![ERD](stage%203/Images/Combination_ERD.png)

### Combinated DSD
Combinated DSD:
   ![DSD](stage%203/Images/Combination_DSD.png)

### Views

1. **Create first view** 

First:
   ![First](stage%203/Reasources/create_my_view.png)

A. First Query of the view
Query 1:
   ![Query_1](stage%203/Reasources/my_view_query_1.png)

B. Second Query of the view
Query 2:
   ![Query_2](stage%203/Reasources/my_view_query_2.png)

2. **Create second view** 

Second:
   ![Second](stage%203/Reasources/create_their_view.png)

A. First Query of the view
Query 1:
   ![Query_1](stage%203/Reasources/their_view_query_1.png)

B. Second Query of the view
Query 2:
   ![Query_2](stage%203/Reasources/their_view_query_2.png)


## Conclusion 3

In this phase, we successfully integrated our database with another system's medical database. We began by analyzing and modeling their schema, creating a comprehensive ERD and DSD based on their tables and relationships. Following this, we imported their database and defined their tables as foreign tables within our own system.

Using shared attributes like `department_id`, we established meaningful connections between our tables (e.g., Doctor, Nurse) and theirs (e.g., Department). This enabled seamless integration and ensured relational consistency.

Finally, we created combined ERD and DSD models to reflect the merged structure and designed two sets of views—one from our perspective and one from theirs—to enable efficient querying and data analysis across both datasets. This phase laid a solid foundation for a unified and interoperable system.


## Phase 4: Programs
### Programs and triggers on the data-base

This stage includes programs of varying complexity based on the data, 
and appropriate triggers for database integrity.

### Programs

1. **Program 1**
The program checks who the mothers who gave birth by cesarean section are, and transfers them to a room on the 4th or 5th floor randomly depending on the available room.


Function - Draws a free room on the appropriate floors and returns the room number to the procedure:
   ![Function](stage%204/program1/resources1/function1.jpg)


Procedure - receives the maternity's id and updates the maternity's table with the appropriate room id that it receives from the function:
   ![Procedure](stage%204/program1/resources1/procedure1.jpg)


Main program - checks which mothers gave birth by cesarean section and sends the maternity's id to the procedure, and returns an updated table:
   ![Main program1](stage%204/program1/resources1/program1.1.jpg)
   ![Main program2](stage%204/program1/resources1/program1.2.jpg)


Execution of the program:
   ![Execution](stage%204/program1/resources1/exectution1.jpg)


Output of the program:
   ![Output](stage%204/program1/resources1/output1.jpg)


1. **Program 2**
The program selects a random department: if it's a maternity ward, it updates the information about doctors and nurses and returns a summary of births in the past year. otherwise, it returns a summary of data on cancer patients, including types of cancer, number of patients, average age, and planned treatment plans.


Function - Draws a department id and returns the id to the main program:
   ![Function](stage%204/program2/resources2/function2.png)


Procedure - Updates each doctor's years of experience by another year, and if there is an identical nurse ID in the "OncologyStaff" table, updates the nurse's name according to the "OncologyStaff" table:
   ![Procedure](stage%204/program2/resources2/procedure2.png)


Main program - Receives a department id, if the id is the maternity department then updates the nurse and doctor data in the procedure and returns an updated table. otherwise, returns a table of information about the department:
   ![Main program1](stage%204/program2/resources2/program2.1.png)
   ![Main program2](stage%204/program2/resources2/program2.2.png)


Execution of the program:
   ![Execution](stage%204/program2/resources2/execution2.png)


Output of the program:
   ![Output](stage%204/program2/resources2/Output2.png)


### Triggers

1. **Trigger 1**
The trigger runs a function immediately after adding a new birth record in the birth_record table, and within the function it retrieves one doctor who specializes in the type of birth entered and automatically links him to the birth record in the midwife table.


Function for Trigger:
   ![Function_Trigger](stage%204/triggers/trigger1/FunctionForTrigger1.jpg)


Create the trigger:
   ![Create_trigger](stage%204/triggers/trigger1/CreateTrigger1.jpg)


Check output:
   ![Output](stage%204/triggers/trigger1/CheckOutput1.jpg)


1. **Trigger 2**
The trigger operates when a nurse is removed from a room assignment, and automatically searches for another nurse with the same shift who is not assigned to that room. If one is found, it assigns her to that room instead of the deleted nurse.


Function for Trigger:
   ![Function_Trigger](stage%204/triggers/trigger2/FunctionForTrigger2.jpg)


Create the trigger:
   ![Create_trigger](stage%204/triggers/trigger2/CreateTrigger2.jpg)


Check output:
   ![Output](stage%204/triggers/trigger2/CheckOutput2.jpg)


## Conclusion 4

At this stage, we implemented advanced logic and automation within the database to improve operational efficiency and maintain data integrity. Two comprehensive programs were developed to manage room assignments for cesarean deliveries and to handle staff updates and ward treatments. These programs demonstrate the integration of functions and procedures to support real-time decision-making and automated data handling.

In addition, we designed and implemented two key triggers to maintain database consistency and automate staff assignment. A trigger that ensures that each birth registration is immediately associated with a specialist, and a trigger that ensures that room assignments remain covered when a nurse is removed, thus ensuring continuous patient care.

These automated processes significantly reduce the need for manual intervention, minimize errors, and ensure that the system dynamically adapts to real-world scenarios, laying a strong foundation for future scalability and reliability of the hospital management system.

## Phase 5: GUI
### Graphical User Interface for Managing the Maternity Department

This phase includes building a browser-based interface that allows project managers to interact with the database in a clear and user-friendly way.  
The interface supports full CRUD operations (Create, Read, Update, Delete), as well as running predefined queries and stored procedures.

## Technologies Used

The system's interface is web-based and was developed using the **Visual Studio Code** environment.  
The backend is written in **Python**, using the **Flask** framework to handle server-side logic and enable communication between the backend and frontend.  
The frontend consists of static HTML, CSS, and JavaScript files served by Flask.

### Login screen

The main screen displays a login form with the following fields:

- **Username**: Enter your username (project manager).
- **Password**: Enter your personal password.
- Click the **Login** button.

If the username and password are correct, the user is redirected to the system's main dashboard.  
If the credentials are incorrect, an error message appears prompting the user to try again.

![login_screen](stage%205/images/login.png)


### Data display

Once logged in, the user can navigate between six main tabs:

1. **Maternity Data**

Displays all maternity records:
   ![maternity_data](stage%205/images/maternity_database.png)

2. **Baby Data**

Displays all baby records:
   ![baby_data](stage%205/images/baby_database.png)

3. **Birth Record Data**

Displays detailed birth records:
   ![birthrecord_data](stage%205/images/birthrecord_database.png)


### Data operations display
Allows users to perform the following operations:

1. **Add New Data**

Insert new maternity, baby, or birth record:
   ![addnew_data](stage%205/images/addnew.png)

2. **Update Data**

Modify details of an existing entry:
   ![update_data](stage%205/images/update.png)

3. **Delete Data**

Remove a selected entry from the database:
   ![delete_data](stage%205/images/delete.png)

3. **search Data**

Search by id from the database:
   ![search_data](stage%205/images/search.png)



### Query display
Contains three buttons, each executing a different predefined query.  
Upon clicking, the relevant data is displayed below:

1. **Room and Night Shift Nurse Assignment**

   ![query1](stage%205/images/query1.png)

2. **Birth Type and Baby Weight Correlation**

   ![query2](stage%205/images/query2.png)

3. **Monthly Birth Statistics**

   ![query3](stage%205/images/query3.png)


### Program display
This section displays the result of procedures, such as:

**Find an Available Room**

The procedure searches for a free room on the appropriate floor and returns its number:
   ![program1](stage%205/images/program1.png)


## Conclusion 5

In this phase, we designed and implemented a full browser-based graphical user interface for managing the maternity department database.

The system allows project managers to:
- Log in securely with personal credentials
- View, insert, update, and delete data from the maternity, baby, and birth record tables
- Run predefined queries and stored procedures through a user-friendly interface
- Navigate easily between six main tabs, each serving a specific purpose

This phase significantly improved data accessibility and usability, enabling intuitive and efficient management of all database operations directly from the web.

The interface was developed using Python and Flask for the backend, and is served via a static frontend rendered in the browser.


