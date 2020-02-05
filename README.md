# TDE Central
A TOM to Consolidate the Identification and Multi-Facility Followup of Transients in Galaxy Centers


## Installation

TDE Central requires Python 3.7+. Create a new virtualenv:

    python3 -m venv new env
    source env/bin/activate

Now that you have the virtualenv activated, you can install the requirements:

    pip install -r requirements.txt

Set up the database:

    ./manage.py migrate

Run the tests:

    ./manage.py test

Run a development server:

    ./manage.py runserver

