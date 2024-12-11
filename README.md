# Wine Reviews Data Pipeline  

This project processes a CSV file containing wine reviews by cleaning the data and storing it in an SQLite3 database. It includes a Python script to automate the workflow and a Bash script for easy execution.  

## Features  
- Extracts raw data from a CSV file.  
- Cleans and validates the data.  
- Stores the cleaned data in an SQLite3 database.  
- Logs details of the changes during processing.  
- Automates the workflow with a Python script.  
- Simplifies execution using a Bash script.  

## Project Structure  
```plaintext  
wine_reviews/  
├── data/  
│   ├── raw/                     # Folder for the original raw CSV file  
│   │   └── wine_rev.csv     # Original wine reviews CSV file  
│   ├── processed/
│   │   └── clean_reviews.csv  # Cleaned wine reviews CSV file
│   │   └── clean_reviews.db   # SQLite3 database file
├── logs/                        # Folder for log files  
│   └── data_cleaning.log              # Log file for pipeline execution  
├── scripts/  
│   ├── script.py       # Python script for data extraction, cleaning, and storage  
│   └── script.sh        # Bash script to start the pipeline  
├── README.md                    # Project documentation  


