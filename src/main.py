datetime = ["import datetime\n","print datetime.datetime.now()\n"]

with open("version.md", "w") as file:
    file.writelines(datetime)
