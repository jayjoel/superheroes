# SA. Week 1 Code Challenge: SuperHeros

#### By **{List of contributors}**
This project was created and is sole property of Joel Nzuki.

## Project Overview
The Superhero API is a RESTful API built with Flask and SQLAlchemy, designed to manage superheroes and their powers. It allows users to create, read, update, and delete (CRUD) heroes , as well as manage their relationships.

## Content
1. Retrieve all heroes and their powers.
2. Retrieve a specific hero or power by ID.
3. Update a power's description.
4. Delete heroes  from the database.
5. Create relationships between heroes and powers.


### API ENDPOINTS USED

#### Heroes
1. GET /heroes-Retrieves all heroes.

2. GET /heroes/<id>-Retrieves a specific hero by ID.

3. DELETE /heroes/<id>-Deletes a hero by ID.


#### Powers
1. GET /powers-Retrieves all powers.

2. GET /powers/<id>-Retrieves a specific power by ID.

3. PATCH /powers/<id>Updates the description of a specific power.


#### Hero Powers
1. POST /hero_powers-Creates a new relationship between a hero and a power.


## Setup/Installation Requirements
* One would need either linux or wsl for window users
* A copy of visual basic code installed
* A github account

1. Open your terminal and go to the directory you wish to work from.
2. Go to the following url using ur github account https://github.com/jayjoel/superheroes
3. Go to the code tab and clone the ssh key
4. Go back to the terminal and type git clone <-followed by the ssh key you copied /cloned ->
5. Enter your new cloned repository and type in code .
6. On the visual studio code that has now opened, go to the the run tab.
7. Install the requied packages and set up the required database:

      #### Steps to follow:
      1. Create a virtual environment by, pipenv install && pipenv shell.
      2. Initialize the database - flask db init
                                    -flask db migrate -m "Initial migration."
                                    -flask db upgrade
      3. Seed the database, python seed.py.  


## Technologies Used
This program is built purely with python, flask, flask-sqlalchemy,flask-migrate and sqlite(for development) using the visual code environment.

## Support and contact details
For any issues please email me at jayjoelpn@gmail.com
### License
Apache License 2.0


