#!/bin/bash
#get Content Length
curl -I -s $1 | grep "Content-Length" | cut -b 17-
