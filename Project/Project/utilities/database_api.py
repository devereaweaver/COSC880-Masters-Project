from sqlalchemy import create_engine, Column, Integer, String, Float, Date, MetaData, Table
from sqlalchemy.orm import sessionmaker
import pandas as pd
from ..config import db_user, db_password, db_host, db_port, db_name

# Create database connection string
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Metadata object to hold schema information
metadata = MetaData()

# Define Time Series Data Table (Stock Prices)
time_series_table = Table(
    "time_series_data", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("ticker", String(10), nullable=False),
    Column("date", Date, nullable=False),
    Column("open_price", Float),
    Column("high_price", Float),
    Column("low_price", Float),
    Column("close_price", Float),
    Column("adj_close_price", Float),
    Column("volume", Integer)
)

# Define Macroeconomic Data Table
macro_data_table = Table(
    "macro_data", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("indicator", String(50), nullable=False),
    Column("date", Date, nullable=False),
    Column("value", Float, nullable=False)
)

def setup_database():
    """
    Creates the necessary tables in PostgreSQL if they do not already exist.
    """
    try:
        metadata.create_all(engine)
        print("Database tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")

# Create a session factory
#Session = sessionmaker(bind=engine)

def insert_time_series_data(df):
    """
    Inserts time series (stock price) data into PostgreSQL.
    :param df: Pandas DataFrame with columns: ['ticker', 'date', 'open_price', 'high_price', 'low_price', 'close_price', 'adj_close_price', 'volume']
    """
    try:
        df.to_sql("time_series_data", engine, if_exists="append", index=False)
        print(f"Inserted {len(df)} rows into time_series_data.")
    except Exception as e:
        print(f"Error inserting time series data: {e}")

def insert_macro_data(df):
    """
    Inserts macroeconomic indicator data into PostgreSQL.
    :param df: Pandas DataFrame with columns: ['indicator', 'date', 'value']
    """
    try:
        df.to_sql("macro_data", engine, if_exists="append", index=False)
        print(f"Inserted {len(df)} rows into macro_data.")
    except Exception as e:
        print(f"Error inserting macroeconomic data: {e}")

def run():
    setup_database()
