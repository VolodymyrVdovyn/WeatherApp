# WeatherApp(Django project)

Clone this project to your computer:

    $ git clone https://github.com/VolodymyrVdovyn/WheatherApp.git

Navigate to the folder with this project:

    $ cd WheatherApp/

For activate python virtual enviroment run:

    $ python -m venv venv
    $ source venv/bin/activate

To install requirements run:

    (venv)$ pip install -r requirements.txt

Perform migrations:

    (venv)$ python manage.py makemigrations
    (venv)$ python manage.py migrate

Start the local server:

    (venv)$ python manage.py runserver

Then visit `http://localhost:8000` to view the app.
