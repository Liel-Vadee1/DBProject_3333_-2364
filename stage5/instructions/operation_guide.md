# Maternity Ward Management System - Operation Guide

## Getting Started

### 1. Application Startup
1. Open terminal/command prompt
2. Navigate to the stage5 directory
3. Run: `python main.py`
4. The login window will appear

### 2. Login Process
1. Enter username: `Lielv`
2. Enter password: `lielvadee3055`
3. Click "Login" button or press Enter
4. Upon successful authentication, the main application window opens

## Main Application Interface

### Navigation
The application uses a tabbed interface with 5 main sections:
- **Maternity Management**: Manage mother records
- **Baby Management**: Manage baby records  
- **Birth Records**: Manage birth record linking table
- **Reports & Queries**: Run predefined database queries
- **Procedures & Functions**: Execute stored procedures and functions

## Detailed Operation Instructions

### Maternity Management Tab

#### Adding a New Maternity Record
1. Navigate to "Maternity Management" tab
2. Fill in the form fields:
   - **Name**: Mother's full name
   - **Age**: Age in years (must be between 14-55)
   - **Phone**: Contact phone number
   - **Room ID**: Available room number
3. Click "Add" button
4. Success message will confirm the record was added
5. The data table will automatically refresh

#### Updating an Existing Record
1. Double-click on any record in the data table to populate the form
2. Modify the desired fields
3. Ensure the ID field is filled (auto-populated when double-clicking)
4. Click "Update" button
5. Confirm the changes in the success message

#### Deleting a Record
1. Enter the ID of the record to delete in the ID field
2. Click "Delete" button
3. Confirm deletion in the popup dialog
4. The record and all related birth records will be removed

#### Additional Features
- **Clear**: Clears all form fields
- **Refresh**: Reloads data from database
- **Double-click**: Populates form with selected record data

### Baby Management Tab

#### Adding a New Baby Record
1. Navigate to "Baby Management" tab
2. Fill in the form fields:
   - **Weight**: Baby's weight in kilograms (decimal allowed)
   - **Gender**: Select 'M' or 'F' from dropdown
3. Click "Add" button
4. The system automatically assigns a new ID

#### Updating Baby Information
1. Double-click on a baby record to load data into form
2. Modify weight or gender as needed
3. Click "Update" button
4. Changes are saved immediately

#### Deleting Baby Records
1. Enter the Baby ID in the ID field
2. Click "Delete" button
3. Confirm deletion (this will also remove related birth records)

### Birth Records Tab (Linking Table Operations)

#### Creating a New Birth Record
1. Navigate to "Birth Records" tab
2. Complete all required fields:
   - **Delivery Type**: Select "C-Section" or "Vaginal"
   - **Birth Date**: Format YYYY-MM-DD (e.g., 2025-01-15)
   - **Discharge Date**: Format YYYY-MM-DD
   - **Mother ID**: ID of existing mother record
   - **Baby ID**: ID of existing baby record
3. Click "Add" button
4. The system creates the linking relationship

#### Updating Birth Records
1. Double-click on a birth record to populate the form
2. Modify any fields as needed
3. Ensure Record ID is present
4. Click "Update" button

#### Viewing Comprehensive Birth Data
The birth records table displays:
- Record ID and delivery type
- Birth and discharge dates
- Mother's name
- Baby's gender and weight

This provides a complete view of the relationship between mothers, babies, and birth events.

### Reports & Queries Tab

#### Running Night Shift Nurses Report
1. Navigate to "Reports & Queries" tab
2. Click "Night Shift Nurses Report" button
3. Results show:
   - Room ID
   - Mother name
   - Assigned nurse name
   - Shift hours
4. Data appears in the results table below

#### Running Birth Weight Analysis
1. Click "Birth Weight Analysis" button
2. Results display:
   - Delivery type (C-Section/Vaginal)
   - Total number of births
   - Average baby weight for each delivery type
3. Analysis covers the past year of data

#### Interpreting Results
- Results appear immediately in the table format
- Success message indicates number of records found
- Empty results show "No records found" message
- Scroll bars allow viewing of large result sets

### Procedures & Functions Tab

#### Room Assignment Program (Program 1)
1. Navigate to "Procedures & Functions" tab
2. Click "Run Room Assignment Program" button
3. The program:
   - Identifies mothers who had C-sections
   - Finds available rooms on floors 4 or 5
   - Automatically assigns mothers to appropriate rooms
   - Updates room occupancy status
4. Results appear in the text area below
5. Check "Maternity Management" tab to see updated room assignments

#### Department Summary Program (Program 2)
1. Click "Run Department Summary Program" button
2. The program:
   - Randomly selects a department
   - If maternity department (ID=7): updates staff info and shows birth statistics
   - If other department: shows cancer patient data and treatment plans
   - Updates doctor seniority and nurse information
3. Execution results display in the text area

## Data Validation and Error Handling

### Input Validation
- **Age**: Must be between 14-55 years
- **Weight**: Must be a valid decimal number
- **Dates**: Must be in YYYY-MM-DD format
- **IDs**: Must be valid integers
- **Required Fields**: All fields must be completed before submission

### Error Messages
- **Database Errors**: Connection issues, constraint violations
- **Validation Errors**: Invalid data format or range
- **Operation Errors**: Failed CRUD operations

### Success Confirmations
- Green success messages for completed operations
- Automatic data refresh after successful operations
- Record count confirmations for query results

## Best Practices

### Data Entry
1. Always verify room availability before assigning mothers
2. Use consistent date formats (YYYY-MM-DD)
3. Double-check IDs when creating relationships
4. Clear forms after each operation to avoid confusion

### Data Management
1. Regularly refresh data views to see latest changes
2. Use double-click feature for accurate data editing
3. Confirm deletions carefully as they cascade to related records
4. Review query results for data accuracy

### System Maintenance
1. Monitor database connections for stability
2. Regular data backups (outside application)
3. Verify procedure execution results
4. Keep track of room assignments and availability

## Keyboard Shortcuts
- **Enter**: Submit login form
- **Double-click**: Load record data into form
- **Tab**: Navigate between form fields

## Troubleshooting Common Issues

### Form Not Submitting
- Check all required fields are filled
- Verify data formats (especially dates and numbers)
- Ensure database connection is active

### Data Not Appearing
- Click "Refresh" button to reload data
- Check database connection status
- Verify table permissions

### Procedure Execution Fails
- Check database connection
- Verify stored procedures exist in database
- Review error messages for specific issues

### Performance Issues
- Close and restart application if sluggish
- Check database server performance
- Limit large query result sets

This operation guide provides comprehensive instructions for using all features of the Maternity Ward Management System effectively and efficiently.