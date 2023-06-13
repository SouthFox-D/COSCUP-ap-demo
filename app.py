#!/usr/bin/env python3
"""Creatr App"""
from flask import Flask, request
from demo.utils.checker import inbox_prechecker


app = Flask(__name__)

@app.route('/')
def index():
    """Show index page"""
    return "Hello Fediverse!"


@app.route("/inbox", methods=["POST"])
def inbox():
    """Process inbox request"""
    is_verify = inbox_prechecker(request)
    if is_verify:
        return "STUB"
    return "STUB"
