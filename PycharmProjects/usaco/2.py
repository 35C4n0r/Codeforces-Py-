'''
ID: jay20ma1
LANG: PYTHON3
TASK: beads
'''

f = open("beads.in", "r")
numBeads = int(f.readline())
beads = f.readline().strip()
f.close()
longestRun = 0
allWork = False
for i in range (numBeads):
  cIndex = i
  current = ""
  while beads[cIndex] == "w":
    cIndex = (cIndex + 1) % numBeads
    if cIndex == i:
      allWork = True
      break
  if allWork:
    break
  current = beads[cIndex]
  while beads[cIndex] == "w" or beads[cIndex] == current:
    cIndex = (cIndex + 1) % numBeads
    if cIndex == i:
      allWork = True
      break
  if allWork:
    break
  cRun = (cIndex - i) % numBeads
  #print("first cRun: " + str(cRun))

  cIndex = (i - 1) % numBeads
  while beads[cIndex] == "w":
    cIndex = (cIndex - 1) % numBeads
    if cIndex == i:
      allWork = True
      break
  if allWork:
    break
  current = beads[cIndex]
  while beads[cIndex] == "w" or beads[cIndex] == current:
    cIndex = (cIndex - 1) % numBeads
    if cIndex == i:
      allWork = True
      break
  if allWork:
    break
  cRun += (i - cIndex) % numBeads
  cRun -= 1
  longestRun = max(longestRun, cRun)
  #print("longestRun: " + str(longestRun) + " cRun: " + str(cRun) + " i: " + str(i))

f2 = open("beads.out", "w")
if allWork:
  f2.write(str(numBeads) + "\n")
else:
  f2.write(str(min(longestRun, numBeads)) + "\n")