import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bolts_control')

def get_wip_user():
    """
    Get the work-in-progress data of bolts from user 
    """
    print("Please provide WIP data from today's work: ")
    print("Data should be six numbers, separated by commas.")
    print("Example: 21,23,10,54,20,36")

    data_str = input("Enter your WIP here: ")
    print(f"The data provided is {data_str}")

get_wip_user()
