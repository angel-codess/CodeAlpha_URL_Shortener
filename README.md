# URL Shortener

A URL Shortener application built using Flask, MySQL, and React. This project allows users to shorten long URLs and redirect them to the original URL upon visiting the shortened link.

## Technologies Used:
- **Backend**: Flask (Python)
- **Frontend**: React (JavaScript)
- **Database**: MySQL
- **Other**: Docker (for containerization), Flask-SQLAlchemy (ORM for database interaction)

## Features:
- Shorten any URL and get a unique shortened link.
- Redirect to the original URL by accessing the shortened link.
- User-friendly interface to input URLs for shortening.

## Prerequisites:
1. Python 3.x
2. Node.js and npm
3. MySQL database
4. Docker (optional, for containerization)

## Setup Instructions:

```bash
1. Backend Setup (Flask + MySQL):

Step 1: Clone the repository
git clone https://github.com/yourusername/url_shortener.git
cd url_shortener

Step 2: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Step 3: Install Python dependencies
pip install -r requirements.txt

Step 4: Set up MySQL database
Create a MySQL database (e.g., url_shortener).
Update the config.py file in the Flask backend to include your MySQL credentials.

Step 5: Run the Flask app
flask run
The backend should now be running on http://localhost:5000.

2. Frontend Setup (React):
Step 1: Navigate to the frontend folder
cd frontend

Step 2: Install npm dependencies
npm install

Step 3: Start the React development server
npm start
The frontend will be available on http://localhost:3000.

3. Testing the Application:

Open http://localhost:3000 in your browser.
Enter a long URL into the input field and click "Shorten" to generate a shortened URL.
Copy the shortened URL and paste it into your browser’s address bar to be redirected to the original URL.
```

#### API Endpoints:
```bash
POST /api/shorten: Shorten a URL.
Request body: { "url": "<long-url>" }
Response: { "shortened_url": "<shortened-url>" }
GET /api/<shortened_url>: Redirect to the original URL.
Redirects to the original URL based on the shortened URL.
```
#### Troubleshooting:

If the Flask app doesn't start, make sure the MySQL server is running and the credentials in config.py are correct.
Ensure that the React frontend is pointing to the correct backend API (i.e., http://localhost:5000).
