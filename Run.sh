#!/bin/bash
python ELProject.py
mysqldump -u USER -pYOUR_PASSWORD --skip-opt --add-drop-table --skip-extended-insert --skip-add-locks DATABASE  > Log.sql


