from flask_restful import Resource, reqparse
from models.blogpostmodel import BlogPostModel

class Blog(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('body',
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument('author',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )
    """
    parser.add_argument('user_id',
        type=int,
        required=True,
        help='A user id is required'
    )"""

    def get(self, title):
        blog = BlogPostModel.find_by_title(title)
        if blog:
            return blog.json()
        return {'message': 'Blog was not found'}

    def post(self, title):
        blog = BlogPostModel.find_by_title(title)
        if blog:
            return {'message': 'A blog with that title already exits.'}, 400
        else:
            data = Blog.parser.parse_args()
            blog = BlogPostModel(title, **data)

            try:
                blog.save_to_db()
            except:
                return {'message': 'An error occurred while creating the blog'}, 500

        return blog.json(), 201

    def delete(self, title):
        blog = BlogPostModel.find_by_title(title)

        if blog:
            blog.delete_from_db()
        return {'message': 'Successfully Deleted'}

    def put(self, title):
        data = Blog.parser.parse_args()

        blog = BlogPostModel.find_by_title(title)

        if blog is None:
            blog = BlogPostModel(title, **data)
        else:
            blog.content = BlogModel['content']
            blog.author = BlogModel['author']

        blog.save_to_db()
        return blog.json()


class BlogList(Resource):
    def get(self):
        return {'Blogs': [blog.json() for blog in BlogPostModel.query.all()]}
