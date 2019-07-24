#!/bin/bash
cd /
cd /Users/ryani/Automation/KETask/venv2
source bin/activate
cd /Users/ryani/Automation/KETask/tests/home/
pytest --alluredir /Users/ryani/Automation/KETask/Reports
