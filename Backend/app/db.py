# import mysql.connector

# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",  # Replace with your XAMPP password if any
#         database="chatbot_db"
#     )
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/dbname'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)