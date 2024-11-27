import snowflake.connector
import pandas as pd

# Snowflake credentials
SNOWFLAKE_CONFIG = {
    'user': 'your-snowflake-user-name',
    'password': 'your-snowflake-password',
    'account': 'your-snowflake-account-name',
    'warehouse': 'your-snowflake-warehouse-name',
    'database': 'your-snowflake-database-name',
    'schema': 'your-snowflake-schema-name',
    'role' : 'your-snowflake-role-name'
}

# File path
LOCAL_FILE_PATH = "Paste-your-dataset-path"  

def upload_to_snowflake():
    # Read local data
    df = pd.read_csv(LOCAL_FILE_PATH)

    # Establish Snowflake connection
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    cursor = conn.cursor()

    # Upload data to Snowflake
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO ROHAN.CONN.MY_TABLE (YearsExperience, Salary) 
            VALUES (%s, %s)
        """, ( row['YearsExperience'], row['Salary']))

    # Close the connection
    conn.close()
    print("Data uploaded successfully.")

if __name__ == "__main__":
    upload_to_snowflake()
