import pytest
from app import Weather  # Ensure this matches your Tkinter class import

def test_app_creation():
    app = Weather()
    assert app is not None  # Check if the app instance is created
