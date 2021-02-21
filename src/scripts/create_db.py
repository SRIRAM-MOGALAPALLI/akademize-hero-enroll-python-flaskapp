"""Create DB Script."""
# from flask import Flask
from src.app import db
print("\nHero Enroll Service:: Creating DB...")

db.create_all()
db.session.commit()
