####################################################################################################################################################################
####################################################### This script is created by D. Niehoff #######################################################################
####################################################################################################################################################################

import os
from datetime import datetime

#define time constraints
now = datetime.now() #determine current data
year = now.strftime("%H") #replace H with Y #define current year
month = now.strftime("%M") #replace M with m #define current month

#Define folders
path = "c:\\test" #provide root foto folder
newpathyear = os.path.join(path, year)
newpathmonth = os.path.join(path, year, month)

#Create folder if it doesn't exist
if not os.path.exists(newpathyear):
    os.mkdir(newpathyear)

if not os.path.exists(newpathmonth):
    os.mkdir(newpathmonth)
