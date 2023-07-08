#!/usr/bin/env python3
"""Creatr App"""
from flask import Flask, Response, request, Request, abort, jsonify
from demo.utils.checker import inbox_prechecker
from demo import config


app = Flask(__name__)

def is_ap_requested(ap_request: Request) -> bool:
    """Check request accept headers."""
    accept_str = ap_request.headers.get("accept")
    if accept_str is None:
        return False
    for i in [
        "application/activity+json",
        "application/ld+json",
    ]:
        if accept_str.startswith(i):
            return True
    return False


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


@app.route("/.well-known/webfinger")
def wellknown_webfinger() -> Response:
    """Exposes servers WebFinger data."""
    resource = request.args.get("resource")

    if resource not in [f"acct:{config.USERNAME}@{config.DOMAIN}", config.ID]:
        abort(404)

    resp = jsonify(
        {
            "subject": f"acct:{config.USERNAME}@{config.DOMAIN}",
            "aliases": [config.ID],
            "links": [
                {
                    "rel": "http://webfinger.net/rel/profile-page",
                    "type": "text/html",
                    "href": config.ID,
                },
                {
                    "rel": "self",
                    "type": "application/activity+json",
                    "href": config.ID,
                },
            ],
        },
    )
    resp.headers["Access-Control-Allow-Origin"]  = "*"
    resp.headers["Content-Type"] = "application/jrd+json; charset=utf-8"

    return resp
