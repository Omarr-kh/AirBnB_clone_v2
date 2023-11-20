#!/usr/bin/python3
'''This module instantiates an object of DBStorage or FileStorage'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
