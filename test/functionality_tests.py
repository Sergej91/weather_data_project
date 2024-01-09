"""
Unit and functionality tests
"""

import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from src.weather_data_script import get_weather_data
from src.db_handler import c_db_handler

def test_db_handler_read():
    """
    Try reading existing collection: admin->system.users
    """

    db = c_db_handler()
    assert db.connect()
    retrieved_collection = db.get_collection("admin", "system.users")
    assert retrieved_collection is not None
    assert len(retrieved_collection) >= 1


def test_db_handler_write_rm():
    """
    Try writing, reading and removing entry
    """

    db = c_db_handler()
    assert db.connect()
    
    db_name = "test_db"
    collection_name = "test_collection"
    doc = {
        "name": "test",
        "number": 3.14159265359,
        "description": "This is a test entry!"
    }

    assert db.write_to_collection(db_name, collection_name, doc)
    retrieved_doc = db.find_document_by_key_value(db_name, collection_name, "name", "test")
    assert retrieved_doc == doc

    assert db.remove_document_by_key_value(db_name, collection_name, "name", "test")
    assert db.remove_collection(db_name, collection_name)
    assert db.remove_database(db_name)

