#!/bin/bash
set -e

docker pull deepanshujain1999/learn-aws

docker run -d -p 5000:5000 --name my-app deepanshujain1999/learn-aws
