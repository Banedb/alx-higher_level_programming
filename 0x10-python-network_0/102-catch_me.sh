#!/bin/bash
# Sends a request and displays size of body of response.
curl -sLX PUT -d "user_id=98" -H "Origin: ALX" 0.0.0.0:5000/catch_me

