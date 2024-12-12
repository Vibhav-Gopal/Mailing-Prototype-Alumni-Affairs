from mail_sender import *
from time import sleep
from htmlData import *
import pandas as pd

# data = pd.read_excel("data.xlsx")
# names = data["NAME"]
# emails = data["EMAIL"]
# data = pd.read_excel("Subscribers.xlsx")
# names = data["First name"]
# emails = data["Email"]
names =["Vibhav"]
emails = ["vibhavgopal2004+test@gmail.com"]
people = list(zip(names,emails))
subj = "Calling ECE Core Professionals: Volunteer for our Resume 101"
# for person in people:
#     name = person[0]
#     name = str(name)

#     email = person[1]
#     message = html_top + html_mid + html_bottom

#     print(name,"Sent at",email)
#     gmail_send_message(email,subj,message)
#     sleep(0.075)
# message = html_top + html_mid.format(name="Vibhav") + html_bottom
gmail_send_message("vibhavgopal2004+test@gmail.com", "Test",msg_text)


msg_markdown = """
# STD
This repo is designed specifically for simplifying the process of writing the relations from the Discovery Matrix.
But can be modified to satisfy various needs, the python file basically reads an excel file, with indexed columns and spits out the data in textual form in another file.

Added python script to calculate n-factor of reachability matrix

## Dependencies
* Python 3.9
* Pandas module
+ NumPy module

## Instructions
1. This script must be placed in the same folder as the excel sheet to be read
2. Create a new file named "results.txt" in the same folder as this script
3. The first row in the spreadsheet must be indexed, starting from 0, refer to the spreadsheet attached for reference
4. Change the value of the variables in the python script before executing to the number of rows/columns in the required table

## Limitations
+ Works only for square matrices
+ The value of correlation between two elements must be either a 1 or a 0
***
### Author
Vibhav - <vibhavgopal2004@gmail.com>

"""
