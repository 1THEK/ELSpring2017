#!/bin/bash
ssh YOUR_NP_ACCOUNT@wyvern.cs.newpaltz.edu 'mysql -h wyvern -pDATABASE_PASSWORD DATABASE_NAME -e "SOURCE /home/XXXXXX/WWW/Log.sql"'
