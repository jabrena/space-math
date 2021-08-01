from ti_system import disp_wait
import ti_graphics as scr

# Screen parameters TI-84 Plus
tw, th = 8, 15
xmin, xmax, ymin, ymax = 0, 319, 30, 239

SUN_MERCURY_DISTANCE_MILL_KM = 57.9
SUN_VENUS_DISTANCE_MILL_KM = 108.2
SUN_EARTH_DISTANCE_MILL_KM = 149.6
SUN_MARS_DISTANCE_MILL_KM = 227.9   

SUN_RADIUS_KM = 696340
MERCURY_RADIUS_KM = 2439.7
VENUS_RADIUS_KM = 6051.8
EARH_RADIUS_KM = 6371
MARS_RADIUS_KM = 3389.5

RELATION_RADIUS_SUN_EARTH = SUN_RADIUS_KM / EARH_RADIUS_KM
print(RELATION_RADIUS_SUN_EARTH)

SCR_SMALL_PLANET = 4
SCR_SUN_RADIUS = RELATION_RADIUS_SUN_EARTH
print(SCR_SUN_RADIUS)
SCR_MERCURY_RADIUS = SCR_SMALL_PLANET * (MERCURY_RADIUS_KM / EARH_RADIUS_KM)
SCR_VENUS_RADIUS = SCR_SMALL_PLANET * (VENUS_RADIUS_KM / EARH_RADIUS_KM)
SCR_EARTH_RADIUS = SCR_SMALL_PLANET
SCR_MARS_RADIUS = SCR_SMALL_PLANET * (MARS_RADIUS_KM / EARH_RADIUS_KM)

#print(EXIT)

# The function drawArc(x, y, dx, dy, t1, t2)
# therefore makes it possible to draw an arc of an ellipse itself inscribed 
# in a rectangle of dimensions w and h pixel data
# with sides parallel to the edges of the screen
# and using the coordinate point (x, y) as top left vertex
# t1 and t2are the centrally oriented angles delimiting the arc in question, expressed in tenths of a degree.

BLACK_COLOR = (0,0,0)

SUN_COLOR = (239, 142, 56)
MERCURY_COLOR = (219,206,202)
VENUS_COLOR = (150, 131, 150)
EARTH_COLOR = (167, 222, 218)
MARS_COLOR = (153, 133, 122)


def fillCircle(x, y, r):
  scr.fillArc(x - r, y - r, 2 * r, 2 * r, 0, 3600)

EARH_ORBITAL_ECCENTRICITY = 0.01671 

scr.cls()
scr.setPen(0, 0)

scr.setColor(SUN_COLOR)
fillCircle(xmax / 2, ymax / 2, SCR_SMALL_PLANET)

scr.setColor(EARTH_COLOR)
scr.drawArc((xmax / 2) - 50, (ymax / 2) - 50, 100, 100 * (1 - EARH_ORBITAL_ECCENTRICITY), 0, 3600)

scr.setColor(EARTH_COLOR)
fillCircle(xmax / 2 + 50, ymax / 2, SCR_SMALL_PLANET)

TEXT = "Earth Orbits around Sun"
scr.setColor(BLACK_COLOR)
scr.drawString(TEXT, xmin + 50 , ymin + 10)

disp_wait()