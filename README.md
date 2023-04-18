# Bloglite: Snapshot of the application
## Landing page - Login/Register
![image](https://user-images.githubusercontent.com/90550267/232662994-2de8522b-1e2d-468e-ace2-8f5969176efb.png)

## Homepage/Dashboard
![image](https://user-images.githubusercontent.com/90550267/232662981-b5c8883b-a76a-4124-8782-03ba78ff3078.png)

## My-profile Page
![image](https://user-images.githubusercontent.com/90550267/232662952-44df1ebe-0906-4c5c-b3e2-8ef1b2129a5e.png)

## Searching and engaging with other users
![image](https://user-images.githubusercontent.com/90550267/232662945-b5cb0e48-09d5-4447-9693-472d1eaa2745.png)

------------------------------------------------------------------------------------------------------------------

# Run the application 

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

### terminal #4 - Mailhog server

- Check your system architecture and download the appropriate version from the [Mailhog repo releases](https://github.com/mailhog/MailHog/releases/v1.0.0)
- run the .exe file to start a local mailhog server




