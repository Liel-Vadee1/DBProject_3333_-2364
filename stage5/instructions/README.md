# Maternity Ward Database Management System

## Overview
This is a comprehensive graphical user interface (GUI) application for managing a maternity ward database. The system provides full CRUD (Create, Read, Update, Delete) operations for managing maternity records, baby information, birth records, and includes advanced reporting and procedure execution capabilities.

## System Requirements
- Python 3.7 or higher
- PostgreSQL database
- Required Python packages (see requirements.txt)

## Installation Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Setup
Ensure your PostgreSQL database is running with the following configuration:
- Host: localhost
- Port: 5432
- Database: maternity_ward (or your database name)
- Username: Lielv
- Password: lielvadee3055

### 3. Database Schema
Make sure your database contains all the required tables from the previous stages:
- maternity
- baby
- birth_record
- room
- nurse
- doctor
- midwife
- attending_to

## Running the Application

### Start the Application
```bash
python main.py
```

### Login Credentials
- Username: Lielv
- Password: lielvadee3055

## Application Features

### 1. Login Screen
- Secure authentication with database connection verification
- Default credentials pre-filled for convenience
- Error handling for connection issues

### 2. Maternity Management Tab
**CRUD Operations:**
- **Create**: Add new maternity records with name, age, phone, and room assignment
- **Read**: View all maternity records with room information
- **Update**: Modify existing maternity records
- **Delete**: Remove maternity records (with cascade deletion of related records)

**Features:**
- Data validation for age constraints (14-55 years)
- Room availability checking
- Double-click to populate form fields from table selection

### 3. Baby Management Tab
**CRUD Operations:**
- **Create**: Add new baby records with weight and gender
- **Read**: View all baby records
- **Update**: Modify baby information
- **Delete**: Remove baby records (with cascade deletion)

**Features:**
- Weight validation (must be numeric)
- Gender selection dropdown (M/F)
- Automatic ID generation

### 4. Birth Records Tab (Linking Table)
**CRUD Operations:**
- **Create**: Create new birth records linking mothers and babies
- **Read**: View comprehensive birth records with mother and baby details
- **Update**: Modify birth record information
- **Delete**: Remove birth records

**Features:**
- Delivery type selection (C-Section/Vaginal)
- Date validation for birth and discharge dates
- Foreign key relationship management
- Comprehensive view showing related data from multiple tables

### 5. Reports & Queries Tab
**Available Queries:**
1. **Night Shift Nurses Report**: Shows rooms with single mothers and their assigned night shift nurses
2. **Birth Weight Analysis**: Analyzes average baby weight by delivery type over the past year

**Features:**
- Dynamic result display in tabular format
- Query execution status feedback
- Scrollable results view

### 6. Procedures & Functions Tab
**Available Programs:**
1. **Room Assignment Program**: Automatically assigns C-section mothers to available rooms on floors 4 or 5
2. **Department Summary Program**: Randomly selects a department and provides relevant summary information

**Features:**
- One-click execution of complex database procedures
- Real-time execution feedback
- Results display in text format

## User Interface Features

### Design Elements
- Modern, clean interface with professional color scheme
- Intuitive tab-based navigation
- Consistent button styling and layout
- Responsive design with scrollable content areas

### Data Validation
- Input validation for all form fields
- Type checking for numeric fields
- Required field validation
- Database constraint enforcement

### Error Handling
- Comprehensive error messages
- Database connection error handling
- Transaction rollback on failures
- User-friendly error notifications

### User Experience
- Double-click to edit functionality
- Clear form buttons for easy data entry
- Refresh buttons to update data views
- Confirmation dialogs for delete operations

## Database Operations

### Transaction Management
- Automatic transaction handling
- Rollback on errors
- Commit on successful operations

### Cascade Operations
- Proper handling of foreign key relationships
- Cascade deletion for related records
- Data integrity maintenance

### Performance Features
- Efficient query execution
- Minimal database connections
- Optimized data retrieval

## Security Features
- Database connection authentication
- SQL injection prevention through parameterized queries
- Input sanitization
- Error message sanitization

## Troubleshooting

### Common Issues
1. **Database Connection Failed**
   - Check PostgreSQL service is running
   - Verify connection parameters in config.py
   - Ensure database exists and user has proper permissions

2. **Module Import Errors**
   - Install required packages: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Query Execution Errors**
   - Verify database schema matches expected structure
   - Check for missing tables or columns
   - Review database permissions

### Support
For technical support or questions about the application, refer to the database schema documentation and ensure all prerequisite stages have been completed successfully.

## File Structure
```
stage5/
├── main.py              # Main application entry point
├── database.py          # Database connection and operations
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
└── instructions/       # Documentation
    └── README.md       # This file
```

## Future Enhancements
- Export functionality for reports
- Advanced filtering and search capabilities
- Data backup and restore features
- User role management
- Audit logging