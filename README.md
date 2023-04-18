# Bloglite

## To run the backend:
```
cd backend
virtualenv bloglite
bloglite/Scripts/activate
pip install -r requirements.txt

python app.py
```

## To the run the frontend
```
cd frontend
npm install
npm i bootstrap@5.3.0-alpha3
npm run serve
```

## BACKEND JOBS:

1. Open a WSL prompt/Git Bash on windows
2. Install following command sequence on Ubuntu terminal
```
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip
```
3. Open three terminals and start a virtual environment such as follows:
```
cd "/mnt/<followed by the complete path to the backend folder>" // Make sure you're inside the backend dir
virtualenv bloglite
source bin/activate
pip install -r requirements.txt
```

### terminal #1 - Redis server
```
redis-server
```

### terminal #2 - Celery Worker server
```
celery -A app.celery worker -l info
```

### terminal #3 - Celery beat server
```
celery -A app.celery beat --max-interval 2 -l INFO
// --max-interval : maximum interval to check for beat updates
```
