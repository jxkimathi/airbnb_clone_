"""The initialization file for the project"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
