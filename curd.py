from jesus   import engine
from sqlalchemy import text

def load_job():
  print("Fetching data...")
  with engine.connect() as conn:
    results = conn.execute(text("select * from jobs")) 
    jobs=[];
    for row in results:
      jobs.append(dict(row._mapping))
    return jobs; 

def load_job_byID(id):
  print("Fetching data...")
  with engine.connect() as conn:
    results = conn.execute(text("select * from jobs where id= :val"),{"val":id}) 
    row = results.fetchone()
    if row:
        return(dict(row._mapping))  # Convert row to dict
    #else :    
    #    return None