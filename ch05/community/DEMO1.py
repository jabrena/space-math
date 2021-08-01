from ti_graphics import setColor,fillRect,sleep,cls
from ti_system import disp_wait

GRID_W = 9
GRID_H = 9

generation = 0

class Cell:
  def __init__(self,r,c,on=0):
    self.c = c
    self.r = r
    self.on = on

  def display(self):
    x=8
    y=8
    if self.on == 1:
      fill_rect(x+SZ*self.r, y+SZ*self.c, SZ, SZ,(0,0,0))
    else:
      fill_rect(x+SZ*self.r, y+SZ*self.c, SZ, SZ,(255,255,255))

  def checkNeighbors(self):
    neighbs = 0
    if self.on == 1: return 1
    for dr,dc in [[-1,0], [1,0], [0,-1],[0,1]]:
      try:
        if cellList[self.r + dr][self.c + dc].on == 1:
          neighbs += 1
      except IndexError:
        continue
    if neighbs in [1,4]:
      return 1
    else:
      return 0

def setup():
  global SZ, cellList
  width=200
  SZ = width // GRID_W + 1
  cellList = createCellList()

def draw():
  global generation,cellList
  while True:
    cellList = update(cellList)
    for row in cellList:
      for cell in row:
        cell.display()
    generation += 1
    if generation == 8:
      break
    sleep(0.5)

def update(cellList):
  newList = []
  for r,row in enumerate(cellList):
    newList.append([])
    for c,cell in enumerate(row):
      newList[r].append(Cell(r,c,cell.checkNeighbors()))
  return newList[::]
        
def createCellList():
  newList=[]
  for j in range(GRID_H): 
    newList.append([])
    for i in range(GRID_W):
      newList [j].append(Cell(i,j,0))
  newList [GRID_H//2][GRID_W//2].on = 1 
  return newList

def fill_rect(x,y,w,h,c):
  setColor(c)
  fillRect(x,y+24,w,h)

cls()
setup()
draw()
disp_wait()