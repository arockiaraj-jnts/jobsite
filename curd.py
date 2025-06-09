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

def save_job(jobid,data):
  with engine.begin() as conn:
    query=text("insert into  applications(job_id,fullname,linkedin_url,email,education,work_experience,resume_url) " \
    "values(:job_id,:fullname,:linkedinurl,:email,:education,:work_experience,:resume_url)")
    conn.execute(query,
                 {
                  'job_id':jobid,
                 'fullname':data['name'],
                 'linkedinurl':data['linkedin_url'],
                 'email':data['email'],
                 'education':data['edu'],
                 'work_experience':data['exp'],
                 'resume_url':data['rurl']
                 }
                 )