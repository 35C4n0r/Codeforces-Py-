from pathlib import Path

path = Path()
for file in path.glob("*"): # glob is used to search a file here * means all files
   print(file)