#!/bin/bash
# Sends a request and sets custom header.
curl -sH "X-School-User-Id: 98" "$1" 
