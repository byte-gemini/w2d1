#!/usr/bin/env bash

rm *.db
python3 mapper.py
python3 model.py
python3 controller.py
rm -rf __pycache__
