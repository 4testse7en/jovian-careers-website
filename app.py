from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Phnom Penh, Cambodia',
        'salary': 'Reai. 10,00,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Seamreab, Cambodia',
        'salary': 'Reai. 15,00,000',
    },
    {
        'id': 3,
        'title': 'Frontend Enginner',
        'location': 'Remote',
    },
    {   'id': 4,
        'title': 'Backend Enginner',
        'location': 'San francisco, USA',
        'salary': '$, 120,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)