Duplicate File Removel Automation Using Python .

Objective
Design and develop a Python automation script that periodically  scans a specified directory , identifies duplicate files using files checksums, delete the duplicate files , generates the detailed log file through email .

General Developement guidelines
While developing the automation script , follow these rules:
1. Accept input through command-line arguments  or an input file.
2. Do not display the operational messages on the console. Store all the messages , error and operation details in a log file. 

3. Define a seperate function for every seperate task .
4. Handel all expected exceptions to make the script robust.
5. Validate all inoput values before performing any operations.
6. Store all user-defined function in a seperate  user-defined module.
7. Write a clean,moduler,reusable and propperly documented code .
8. using meaningfull name for functions ,variable, modules and files.
9. provide Help and Usage operations for the script.





Problem statement
Developed an automation script nnamed :
DuplicateFileRemobel.py
The script should perform  the following operations:

1 . Accept directory name
    Accept absulute path of directory  from the user through the command line .
    the specified directory  may contains duplicate files.
    The script should recursively scan all files available inside the specified directory and its subdirectories.


2. Identify Duplicate files
    Calculate the checksum of every file using an appropriate hashing algorithm such as MD5 an SHA-256.
    file having the same checksum should considered duplicates.
    for every group of duplicate files:
    - Keep the first file 
    - Delete all remaning duplicate copies.
    - Store the complite pathof every deleted duplicate file in the  log file .

The script should not identify duplicate files only based on thir names . Duplicate detection must be performed using file content and checksum values.

3 create log directory named:

    Marvellous
    the directory should be created in the current working directory or at an appropriate predefined location .
    If the directory already exists, the script should use the existing directory insted of generating error.

4 create log file
    Create a log file inside Marvellous directory.
    The name of log file should contain the date and time at the wich log file is created.
    Example:
    DuplicateRemovelLog_20_07_2026__23_15.log
    The log file should contain:
    - Starting time of directory scanning 
    - Completion time of directory scanning 
    - named of directory scanned
    - total number of file scanned
    - total number of duplicate file found
    - Total number of dupllicate file deleted 
    - Complite path of all deleted duplicate files
    - Checksum values of duplicate files
    - errors encountered during execution
    - email delevery status

    All Operational messages should be written in the log files insted of being displayed on the console.


5. periodic Execution
    Accept all time interval in minutes through the command line
    The duplicate file removel operation should be performed repeatedly after specified time interval.
    For Example : if the interval is 50, the directory should be scanned every 50 minutes.
    The Time interval must be:
    - numaric
    - Greater then zero
    - expressed in minutes
    The script should continue running untill it is manually terminated 

6. Email Notification
    Accept the reciver's email address  througn the command line.
    After compliting each duplicate-file removel operation.
    - send an email to specified reciver.
    - attach the generated log file to the email.
    - Include operation statistics in the email body.
    


