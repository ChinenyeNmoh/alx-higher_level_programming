#!/bin/bash
# script that displays the size of the body of the response
curl -I "$1" | grep -i Content-Length | awk '{print $2}'
