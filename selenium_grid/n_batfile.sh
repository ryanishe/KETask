#!/bin/bash
cd /
cd /Users/ryani/Automation/selenium_grid
docker build -t ubuntu-desktop .
docker run -it -v /Users/ryani/Automation/KETask:/tmp/KETests ubuntu-desktop /bin/bash


docker build -t ubuntu-desktop . && docker run -v /Users/ryani/Automation/KETask:/tmp/KETests ubuntu-desktop /bin/bash -exec "cd /tmp/KETests/tests/home/ && pytest --alluredir /tmp/KETests/Reports/ --browser ubuntu_chrome"