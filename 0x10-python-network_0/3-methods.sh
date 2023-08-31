#!/bin/bash
# script that displays the methods allowed
curl -sI "$1" | grep Allow | awk '{print $2, $3, $4}'
