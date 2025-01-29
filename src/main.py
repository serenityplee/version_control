from datetime import datetime

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("version.md", "w") as f:
    f.write(f"Time: {time}\n")

print("updated")
