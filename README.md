Project Structure:

  user-crud-service/

    ├── app.py

    ├── db.sqlite

    ├── models.py

    ├── README.md

    └── requirements.txt

    app.py - This is the main Flask application file that contains all the routes and endpoints for the user CRUD service.

    db.sqlite - This is the SQLite database file that stores all the user information.

    models.py - This file defines the User model for the database.

    README.md - This is the documentation file that explains how to build/run the project.

    requirements.txt - This file contains all the Python packages required for the project.
  
<p><p>
Installation:

  1. Clone the repository.
     $ git clone https://github.com/northwesttrekker/user-crud-service.git
  
  2. Install the required packages.

     $ cd user-crud-service
     $ pip install -r requirements.txt


Usage:

  Run the Flask application:
  
  $ export FLASK_APP=app.py
  
  $ flask run
  
  bash shell commands:
  
  1. Create a new user.

     POST /users  
     {  
  
        "username": "userOne",
  
        "password": "password",
  
        "email": "userOne@hotmail.com",
  
        "info": "User info"  
  
     }

  2. Login to get JWT Token
  
     POST /login
     {
        "username": "userOne",
        "password": "password"
      }

   3. Get user info
      GET /users/{user_id}

   4. Update user info
      PUT /users/{user_id}
  
      {
  
        "email": "userOneUpdate@hotmail.com",
  
        "info": "Updated user information"
  
      }

   5. Delete user
      DELETE /users/{user_id}

Note: To make sure to include the JWT token in the Authorization header in those commands.
