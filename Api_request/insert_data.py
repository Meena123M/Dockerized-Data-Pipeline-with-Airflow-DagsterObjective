import psycopg2
from api_request import fetch_daily_stock_data
def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5000",
            dbname="db",
            user="db_user",
            password="db_password"
        )
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def create_table(connection):
    try:
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS stock_data (
            id SERIAL PRIMARY KEY,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT
        );
        '''
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()  
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise


def alter_table_add_column(connection):
    try:
        alter_table_query = '''
        ALTER TABLE stock_data
        ADD COLUMN IF NOT EXISTS trade_date DATE;
        '''
        cursor = connection.cursor()
        cursor.execute(alter_table_query)
        connection.commit()
        cursor.close()
        print("Column added successfully.")
    except psycopg2.Error as e:
        print(f"Error altering table: {e}")
        raise

def insert_stock_data(connection, stock_data):
    try:
        insert_query = '''
        INSERT INTO stock_data ( open, high, low, close, volume,trade_date)
        VALUES (%s, %s, %s, %s, %s, %s);
        '''
        cursor = connection.cursor()
        for date, values in stock_data.items():
            open_price = float(values['1. open'])
            high_price = float(values['2. high'])
            low_price = float(values['3. low'])
            close_price = float(values['4. close'])
            volume = int(values['5. volume'])
            cursor.execute(insert_query, (open_price, high_price, low_price, close_price, volume,date))
        connection.commit()
        cursor.close()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")
        raise

def main():
    try:
        conn = connect_to_db()
        create_table(conn)
        alter_table_add_column(conn)
        stock_data = fetch_daily_stock_data('AAPL')
        insert_stock_data(conn, stock_data)
    except Exception as e:
        print(f"An error occurred: {e}")    
    finally:
        if conn:
            conn.close()

