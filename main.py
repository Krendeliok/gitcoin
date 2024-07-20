import os
import random

for i in range(160):
    year = '2024'
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    commit_date = f"{year}-{month:02}-{day:02}"
    d = f"{i} days ago"
    with open(f"test{day}.txt", "a") as file:
        file.write(d + '\n')
        os.system(f"git add .")
        os.system(f"git commit --date='{commit_date}' -m 'Commit number {i+1}'")
os.system("git push -u origin master")
