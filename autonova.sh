#!/bin/bash

# This is the trigger for nonova to add the activities on the .ini file
# If this is your first time using nonova run python nonova -a
# And follow the instruccions over there to add your credentials and then add n number of tasks
# you want to run daily 

# Remember to update your path, too lazy to make it automatic.

# Avtivate VENV!
source /Users/itexico/Documents/Projects/nonova/nonova/bin/activate

# Run teh thing
python /Users/itexico/Documents/Projects/nonova/nonova.py -r
