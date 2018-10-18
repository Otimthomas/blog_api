Blog_api
-The API has two models, the user model that stores the user information, that is the name, email, and password
-The blogpostmodel that stores the blogs content, author, title.

This is a CRUD API that can create a user or blog, retrieve a user or blog, update a blog, and delete a user or blog.

Setup
-----

- Create a virtual environment
- Install all the requirements in the RequestParser.txt
- Run python app.py to start the server
- Test the API endpoints using postman

REST ENDPOINTS
There are two major objects in the app:
-User
-Blogpost

USERS:
  http://localhost:5000/users/
    GET: This URL will return all the users in the database with their stored information

  http://localhost:5000/user/<name>
    GET: This URL will return a particular user <name> with the respective information
    POST: This URL will create a new user <name>
    DELETE: This URL will delete an existing user <name>
    PUT: This URL will update the user details with <name>

BLOGPOST:
  http://localhost:5000/blogs/
    GET: This URL will return all the blogs in the database with their stored information

  http://localhost:5000/blog/<title>
    GET: This URL will return a particular blog <title> with the respective information
    POST: This URL will create a new blog <title>
    DELETE: This URL will delete an existing blog <title>
    PUT: This URL will update the blog details with <title>
