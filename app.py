#!/usr/bin/env python3
"""Creatr App"""
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    """Show index page"""
    return "Hello Fediverse!"
