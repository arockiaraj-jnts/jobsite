from sqlalchemy import create_engine, MetaData, Table, select
from dotenv import load_dotenv
import os

load_dotenv()
db_url = os.getenv('DATABASE_URL')
print("Connecting to database...")
engine = create_engine(db_url)
# Reflect the existing database schema
# Step 2: Reflect table
print("Reflecting tables...")
metadata = MetaData()
try:
    jobs = Table('jobs', metadata, autoload_with=engine)
except Exception as e:
    print("Error reflecting table:", e)
    exit()
