#!/bin/bash
# A bash script to displays the body size of URL
curl -sI "$1" | grep "Content-Length" | cut -d ':' -f 2 | cut -d ' ' -f 2
