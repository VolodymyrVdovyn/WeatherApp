# WheatherApp(Django project)

Clone this project to your computer:

    $ git clone https://github.com/VolodymyrVdovyn/WheatherApp.git

Navigate to the folder with this project.

For activate python virtual enviroment run:

    $ python -m venv venv
    $ source venv/bin/activate

To install requirements run:

    $ pip install -r requirements.txt

Perform migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate

Start the local server:

    $ python manage.py runserver

Then visit `http://localhost:8000` to view the app.