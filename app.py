from flask import Flask
from flask_restful import Api

from resources.user import User, UserList
from resources.blogpost import Blog, BlogList

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thomas'


@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(User, '/user/<string:name>')
api.add_resource(Blog, '/blog/<string:title>')
api.add_resource(BlogList, '/blogs/')
api.add_resource(UserList, '/users/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, port=5000)
