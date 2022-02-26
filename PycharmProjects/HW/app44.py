from pathlib import Path

path = Path("ecommerce")
print(path.exists()) # returns a boolean value after checking that whether a directory exists or not

path1 = Path("trial")
path1.mkdir() # mkdir stands for make directry,f similarly to remove directory we can use rmdi nr