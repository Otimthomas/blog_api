from db import db

class BlogPostModel(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text)
    author = db.Column(db.String(100))


    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author


    def json(self):
        return {'title': self.title, 'body': self.body, 'author': self.author}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
