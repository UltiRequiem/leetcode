import os

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

readme = f"""
## Problems Solved
{problem_list}
Toal solved: {total}
"""

with open("readme.md", "w") as text_file:
    text_file.write(readme)