import os

dirs =  [x[0][9:] for x in os.walk("leetcode/")][1:]

problems = {}

for entry in dirs:
  path = entry 
  entry = entry.split("-")
  num = int(entry[0])
  problems[num] = {"title": ' '.join(entry[1:]).title(), "path": f"./leetcode/{path}"}

problem_list = ""

for problem in range(1, 3416):
  if problem in problems:
    problem_list += f"[{problem}. {problems[problem]['title']}]({problems[problem]['path']})\n"
1

with open("readme.md", "w") as text_file:
    text_file.write(problem_list)