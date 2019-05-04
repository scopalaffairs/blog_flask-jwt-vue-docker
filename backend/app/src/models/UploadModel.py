# src/models/UploadMediaModel.py

import datetime
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
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.data = data.get('data')
        self.owner_id = data.get('owner_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
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
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
