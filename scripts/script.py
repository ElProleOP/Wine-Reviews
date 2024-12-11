import sqlite3
import pandas as pd
import logging
import sqlalchemy 

logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO, format = '%(message)s', filename='../logs/data_cleaning.log')

def clean_reviews(df):
    # Drop some null values
    df.dropna(subset = ['variety', 'country','price'], inplace = True)
    # Changing null values to descriptive information
    df.fillna({'designation': 'Unknown designation'}, inplace = True)
    df.fillna({'region_1': 'Unknown region'}, inplace = True)
    df.fillna({'region_2':'Unknown subregion'}, inplace = True)
    df.fillna({'taster_name':'Unknown taster name'}, inplace = True)
    df.fillna({'taster_twitter_handle': 'No twitter registered'}, inplace = True)

    # Renaming id column
    df.rename(columns = {'Unnamed: 0': 'wine_id'}, inplace = True)
    return df

def null_test(df):
    try:
        assert df.isnull().sum().sum() == 0
    except AssertionError as err:
        logger.exception(err)
        return err
    
def column_test(local_df, db_df):
    try:
        assert local_df.shape[1] == db_df.shape[1]
    except AssertionError as err:
        logger.exception(err)
        return err
    
def dtype_test(local_df, db_df):
    try:
        assert local_df.dtypes.equals(db_df.dtypes)
    except AssertionError as err:
        logger.exception(err)
        return err
    
def schema_test(local_df, db_df):
    try:
        assert local_df.columns.equals(db_df.columns)
    except AssertionError as err:
        logger.exception(err)
        return err
    
def main():
    with open('../logs/data_cleaning.log') as f:
        lines = f.readlines()
    if len(lines) == 0:
        version = "Version:1"
    else:
        version = "Version:" + str(int(lines[-1].split(':')[1][0]) + 1)

    reviews = pd.read_csv('../data/raw/wine_rev.csv')
    # get the current processed data if it exists
    try:
        con = sqlite3.connect('../data/processed/clean_reviews.db')
        db_df = pd.read_sql('SELECT * FROM wine_reviews_clean', con)
        con.close()
    except:
        db_df = pd.DataFrame()
    
    # clean the data
    local_df = clean_reviews(reviews)
    # test the data
    null_test(local_df)
    column_test(local_df, db_df)
    dtype_test(local_df, db_df)
    schema_test(local_df, db_df)
    # save the data
    con = sqlite3.connect('../data/processed/clean_reviews.db')
    local_df.to_sql('wine_reviews_clean', con, if_exists = 'replace', index = False)
    con.close()

    # log the data
    with open('../logs/data_cleaning.log', 'a') as f:
        f.write(f'{version} - Data cleaning completed successfully\n')

if __name__ == '__main__':
    main()
    

        