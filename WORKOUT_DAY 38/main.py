import requests
from dotenv import load_dotenv
import os
import datetime
import openpyxl

wb = openpyxl.load_workbook(filename="C:\\Users\\PC\\Desktop\\sheet.xlsx")
sheet = wb["Sheet1"]


def get_info(info: list) -> list:
    info_list = []
    time = datetime.datetime.now()
    for exercise in info:
        exercise_name = exercise["name"]
        duration = exercise["duration_min"]
        calories = exercise["nf_calories"]
        info_list.append((time.strftime("%d/%m/%Y"), time.strftime("%X"), exercise_name, duration, calories))
    return info_list


def delete():
    date = input("Insert the date you want to remove in the format of (dd/mm/yyyy): ")
    for index, row in enumerate(sheet.iter_rows(min_row=1, values_only=True)):
        for cell in row:
            if isinstance(cell, datetime.datetime):
                if date == cell.date().strftime("%d/%m/%Y"):
                    sheet.delete_rows(index + 1)
    wb.save("C:\\Users\\PC\\Desktop\\sheet.xlsx")


def save(info_to_save):
    for data in info_to_save:
        sheet.append(data)
    wb.save("C:\\Users\\PC\\Desktop\\sheet.xlsx")


load_dotenv(".env")
app_id = os.getenv("APPLICATION_ID")
app_key = os.getenv("APPLICATION_KEY")

choice = input("Would you like to add or remove to the worksheet? (a/r): ").lower()

if choice == "a":
    query = input("Have you exercised today? ")
    headers = {
        "x-app-key": app_key,
        "x-app-id": app_id,
    }

    params = {
        "query": query,
        "gender": "male",
        "weight_kg": 70.0,
        "height_cm": 174.0,
        "age": 21
    }

    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=headers)
    save(get_info(response.json()["exercises"]))
else:
    delete()
