#!/bin/bash
set -e

docker pull deepanshujain1999/learn-aws

docker run -d -p 8000:8000 deepanshujain1999/learn-aws
