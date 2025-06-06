from sqlalchemy import create_engine, MetaData, Table, select

# Setup database engine (change credentials accordingly)
# Step 1: Setup DB connection
print("Connecting to database...")
engine = create_engine('mysql+pymysql://root:root@localhost/jobsite')
# print(engine.url)


# Reflect the existing database schema
# Step 2: Reflect table
print("Reflecting tables...")
metadata = MetaData()
try:
    jobs = Table('jobs', metadata, autoload_with=engine)
except Exception as e:
    print("Error reflecting table:", e)
    exit()

# Step 3: Query function
def get_all_jobs():
    print("Fetching data...")
    with engine.connect() as conn:
        stmt = select(jobs)
        results = conn.execute(stmt).fetchall()
        print(f"Rows fetched: {len(results)}")
        return [dict(row._mapping) for row in results]

# Step 4: Run query and print results
#if __name__ == '__main__':
    jobs_data = get_all_jobs()
    for job in jobs_data:
        print(job)

