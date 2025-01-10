import os
import urllib.request
import json
from datetime import datetime

username = "ultirequiem"

dirs =  [x[0][9:] for x in os.walk("leetcode/")][1:]

problems = {}

for entry in dirs:
  path = entry 
  entry = entry.split("-")
  num = int(entry[0])
  problems[num] = {"title": ' '.join(entry[1:]).title(), "path": f"./leetcode/{path}"}

problem_list = ""
total = 0

for problem in range(1, 3416):
  if problem in problems:
    problem_list += "- [{number}) {name}]({path})\n ".format(number=problem, name=problems[problem]["title"], path=problems[problem]["path"])
    total +=1

updated = False

with urllib.request.urlopen(f"https://leetcode-stats-api.herokuapp.com/{username}") as url:
    data = json.load(url)
    actual_total = data["totalSolved"]
    updated = total == actual_total

readme = f"""## Problems Solved

{problem_list}

Total solved: {total} ({f'Updated' if updated else "Outdated"} | {datetime.today().strftime("%Y-%m-%d")})
My account: https://leetcode.com/u/{username}

## Credits

- [Open Source LeetCode API](https://github.com/JeremyTsaii/leetcode-stats-api)

"""

with open("readme.md", "w") as text_file:
    text_file.write(readme)