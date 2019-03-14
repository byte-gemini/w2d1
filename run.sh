#! Library/Frameworks/Python.framework/Versions/3.7/bin/python3

rm *.db
python3 mapper.py
python3 model.py
python3 controller.py
rm -rf __pycache__
