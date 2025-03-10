from flask import Flask, render_template, request, redirect, url_for, session
import pickle

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load the model
model_pickle = open(r"C:\Users\DELL\Desktop\MLOPs\Flask\hemalatha\classifier.pkl", "rb")
clf = pickle.load(model_pickle)

# Dummy user credentials
USER_CREDENTIALS = {'admin': 'password123'}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if USER_CREDENTIALS.get(username) == password:
        session['user'] = username
        return redirect(url_for('dashboard'))
    else:
        return "Invalid username or password" 

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        Gender = 0 if request.form['Gender'].lower() == "male" else 1
        Married = 0 if request.form['Married'].lower() == "unmarried" else 1
        Credit_History = 0 if request.form['Credit_History'].lower() == "unclear debts" else 1
        ApplicantIncome = int(request.form['ApplicantIncome'])
        LoanAmount = int(request.form['LoanAmount'])

        result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
        pred = "Approved" if result == 1 else "Rejected"

        return redirect(url_for('result', prediction=pred))
    except Exception as e:
        return str(e)

@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    if prediction == "Approved":
        message = "Congratulations! Your loan application is approved."
    else:
        message = "Sorry! Your application is rejected."
    return render_template('result.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
