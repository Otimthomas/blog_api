from db import db

class BlogModel(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(150), nullable=False)

    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #user = db.relationship('UserModel')


    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        #self.user_id = user_id

    def json(self):
        return {'title': self.title,
            'content': self.content,
            'author': self.author
            #'user_id': self.user_id
        }


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delelte_from_db(self):
        db.session.delete()
        db.session.commit()


    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()


    @classmethod
    def find_all(cls, title):
        return cls.query.filter_by(title=title).all()
