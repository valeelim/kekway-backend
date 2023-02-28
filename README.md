# kekway-backend

The API URL: https://kekway.herokuapp.com/
The FE URL: https://kekway.vercel.app/

# Prerequisites

1. Make sure you have python installed

2. The database used for this project is Postgresql, you have to setup `psql` if you want to run it on your local machine (unless you change the database to the default sqlite3)

3. If you do decide to use Postgresql, you would need to configure the environment variables (explained below)

# Getting Started
Steps shown below are only for Windows users. (Mac users should still follow the same steps, just with a different command)

1. Create a virtual environment
```
pip install virtualenv
python -m venv env
.\env\Scripts\activate
```

2. Install all the dependencies
```
pip install -r requirements.txt
```

3. Migrate the database
```
python .\manage.py migrate
```

4. Create the `.env` according to the `env.sample` file

5. Run the app using
```
python .\manage.py runserver
```

The app should now be available at http://localhost:8000
