# Challenge 03 Python script to map data from csv to json

So first we open the file in read mode both the files and load it into a variable or data frame

then we compare env of both the read files and if they exists and aer same, copy into json variable wrt to env and other header from csv variable.

then open the same json file in write mode and dump the loaded json variable into it.

we are using argesparse to take the appropriate input with the cli command of python we use ie 
python copy_detail.py --env DEV/PROD --json ./configs/config.json --csv ./configs/input.csv