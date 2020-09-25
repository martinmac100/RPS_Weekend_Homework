from app import app

@app.route('/')
def test_message():
    return "Hello"