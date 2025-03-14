import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['user'] = 'admin'  # Simulate a logged-in user
        yield client

def test_predict(client):
    test_data = {
        "Gender": "Male",
        "Married": "Unmarried",
        "ApplicantIncome": 5000,
        "Credit_History": "Cleared Debts",
        "LoanAmount": 50000
    }
    resp = client.post('/prediction', json=test_data)
    assert resp.status_code == 200

def test_result_approved(client):
    resp = client.get('/result?prediction=Approved')
    assert resp.status_code == 200
    assert b"Congratulations! Your loan application is approved." in resp.data

def test_result_rejected(client):
    resp = client.get('/result?prediction=Rejected')
    assert resp.status_code == 200
    assert b"Sorry! Your application is rejected." in resp.data
