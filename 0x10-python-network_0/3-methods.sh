#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | sed -n 's/^Allow: //p'
