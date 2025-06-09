from flask import Flask, render_template, jsonify, json,request
from curd import load_job,load_job_byID,save_job

app = Flask(__name__)


def format_strings(text):
  return text.replace('•','</li><li>')

@app.route('/')
def hello_world():
   jobs=load_job()
   return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route('/api/jobs')
def list_jobs():
  jobs=load_job()
  #return json.dumps(jobs)
  return jsonify(jobs)

@app.route('/job_detail/<id>')
def job_detail(id):
  jobs=load_job_byID(id)
  transformtxt=format_strings(jobs['requirements'])
  #return transformtxt;
  jobs['requirements']=transformtxt
  #return json.dumps(jobs)
  return render_template('job_detail.html',jobs=jobs)

@app.route('/job/<id>/job_apply',methods=['post'])
def job_apply(id):
# data=request.args #from url or get
 data=request.form
 jobs=load_job_byID(id)
 #return jsonify(data)
 save_job(id,data)
 print("Datasaved")
 return render_template('job_submitted.html',application=data,jobs=jobs)



if (__name__ == '__main__'):
  app.run(debug=True)
