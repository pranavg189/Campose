import os

from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CameraImage(db.Model):
    __tablename__ = "cameraimg"
    id = db.Column(db.Integer, primary_key=True)
    imgur_id = db.Column(db.String, nullable=False, index=True, unique=True)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f"<CameraImage({self.id}): {self.imgur_id}>"
