#!/bin/bash
# Sends a `DELETE` request and displays the body of response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
