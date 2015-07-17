#!/bin/bash
pip install --user -U -r requirements_pre.txt && pip install --user -U --trusted-host wxpython.org -r requirements.txt && echo -e "\nFinished successfully"