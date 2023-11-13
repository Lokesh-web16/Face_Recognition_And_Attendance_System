import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import messagebox

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime2-b14d6-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "578942":
        {
            "name": "Lokesh T",
            "major": "Computer-BCA",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:45:34"
        },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year":2017,
            "total_attendance":6,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year":2021,
            "total_attendance":12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "425486":
        {
            "name": "Kalam",
            "major": "Rocket Science",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:45:34"
        },
    "678426":
        {
            "name": "Ranganath",
            "major": "Principal",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "A",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:45:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Space X",
            "starting_year":2020,
            "total_attendance":7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)

messagebox.showinfo('Add To Database', 'Thank You ! Data Successfully Added')