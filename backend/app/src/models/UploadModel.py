# src/models/UploadMediaModel.py

from marshmallow import fields, Schema

from . import db


class UploadModel(db.Model):
    """
    Upload Image Model.
    """

    __tablename__ = 'upload'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, data):
        self.data = data.get('data')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_media():
        return UploadModel.query.all()

    @staticmethod
    def get_one_medium(id):
        return UploadModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class UploadSchema(Schema):
    """
    Image Upload Schema
    """
    id = fields.Int(dump_only=True)
    data = fields.Str(required=False)
    owner_id = fields.Int(required=True)
