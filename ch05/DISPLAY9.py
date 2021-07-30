from ti_system import *
import ti_graphics as scr

tw, th = 8, 15
xmin, xmax, ymin, ymax = tw, 319, 30+th, 239

nta, nty = 4, 4
lx = [xmin + k*(xmax-xmin)/(2*nta+1) for k in range(1, 2*nta+1)]
ly = [ymin + k*(ymax-ymin)/(2*nty+1) for k in range(1, 2*nty+1)]
l = (xmax-xmin+1) / (2*nta+1)

scr.cls()
for i in range(nty):
  scr.drawString(str(i), xmin-tw, ly[i*2])
  for j in range(nta):
    scr.drawString(str(j), lx[j*2], ymin-th)
    scr.setPen(j, i)
    scr.setColor((255,0,0))
    scr.fillArc(lx[j*2], ly[i*2], lx[j*2+1]-lx[j*2], ly[i*2+1]-ly[i*2], 0, 3150)
    scr.setColor((0,0,0))
    scr.drawArc(lx[j*2], ly[i*2], lx[j*2+1]-lx[j*2], ly[i*2+1]-ly[i*2], 0, 3150)

disp_wait()
