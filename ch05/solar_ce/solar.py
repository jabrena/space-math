# Solar v.1.01 NW 23/10/2020
# https://nsi.xyz/solar
# par Jil Saint-Martin et Emmy Vadon

from math import sqrt
from random import randint

from polysol import *
screen_w, screen_h, font_h, set_pixel, fill_rect, draw_ellipse, fill_circle, draw_string, get_key = get_infos()

def cercle(x0,y0,r,c,e):
 for i in range(2*e):
   rt = max(0,r-i*0.5)
   draw_ellipse(x0,y0,rt,rt,c)

def cercle_plein(x0,y0,r,c1,e,c2):
 fill_circle(x0,y0,r-e,c2)
 fill_circle(x0,y0,r,c1)

def cercle_grade(x0,y0,R,c1,e,c2):
 for i in range(R):
   cercle(x0,y0,i,(c1[0]+i*(c2[0]-c1[0])//R,c1[1]+i*(c2[1]-c1[1])//R,c1[2]+i*(c2[2]-c1[2])//R),1)

systeme = (("Soleil",'centre du syteme solaire','0','1,989 × 10^30','696340', '0'),
           ("Mercure",'88','57','3,285 × 10^23','2439.7', '0'),
           ("Venus",'225','104','4,867 × 10^24','6051.8', '0'),
           ("Terre",'365','150','5,972 × 10^24','6371', 'Lune'),
           ("Mars",'687','220 ','6.39 × 10^23 ','3389,5','2'),
           ("Jupiter",'12','780 ','1.898 × 10^27','69911','3'),
           ("Saturne",'29','1,493','5.683 × 10^26','58232','~ 200'),
           ("Uranus",'84','2,9592','8.681 × 10^25','25362','27'),
           ("Neptune",'165','4,4762','1.024 × 10^26','24622','14'),
           )
coord = [[160,111,16], [180,110,6], [185,95,8], [120,100,9], [160,160,9], [115,150,15], [200,50,12], [170,20,9], [55,80,8]]
couleur1 = ((255,255,0), (251,136,7), (190,183,150), (30,160,173), (245,0,0), (162,125,105), (200,169,133), (191,209,232), (0,33,240))
couleur2 = ((235,128,0), (106,73,32), (121,104,83), (6,67,29), (101,12,12), (134,56,32), (189,138,80), (117,163,224), (5,15,81))

for k in range(len(coord)):
  coord[k][0] = coord[k][0]*screen_w//320
  coord[k][1] = coord[k][1]*screen_h//222
  coord[k][2] = coord[k][2]*screen_w//320
fill_rect(0,0,screen_w,screen_h,(0,0,0))
cercle_grade(screen_w//2,screen_h//2,197*screen_w//320,(0,35,143),10,(0,0,0))
cercle_grade(screen_w//2,screen_h//2,40*screen_w//320,couleur2[0],2,(0,35,143))
cercle_grade(screen_w//2,screen_h//2,coord[0][2],couleur1[0],2,couleur2[0])

def degrade(c1,c2,k):
 return (c1[0]+int(k*(c2[0]-c1[0])),c1[1]+int(k*(c2[1]-c1[1])),c1[2]+int(k*(c2[2]-c1[2])))

def tirage(n):
 for i in range(n):
   x=randint(0,screen_w)
   y=randint(0,screen_h)
   fill_rect(x,y,2,2,couleur(x,y))

def couleur(x,y):
 c=(couleur2[0],(13,89,175),(13,89,175),(44,122,211),(207,230,230),(207,230,230))
 d=sqrt((x-screen_w//2)**2+(y-screen_h//2)**2)/(screen_w/10+.5)
 return degrade(c[int(d)],c[(int(d)+1)%6],d-int(d))

tirage(250)
couleur, tirage = None, None

c_blanc=(255,255,255)
r_orb = (22,32,42,52,62,76,92,109)
for i in range(8):
   cercle(screen_w//2,screen_h//2,r_orb[i],(119,135,135),1)
r_orb = None
 
def solar_systeme_dessine(n, degrade=1):
 # Affiche un corps du sytème solaire, numéro du corps dans systeme[], degradé
 cercle_grade(coord[n][0], coord[n][1], coord[n][2], degrade and couleur1[n] or c_blanc, 2 + 9 * (n != 0), degrade and couleur2[n] or c_blanc)
 
def solar_systeme_texte(n=42, t=0): #affichage du texte en bas, de couleur associée à omega, avec les diverse infos
 try:
   get_keys()
   os = (192,53,53)
 except:
   os = (255,183,52)
 if n == 42 :
   fill_rect(1,screen_h-font_h,screen_w,font_h,os)
   draw_string("nsi.xyz/solar par Emmy & Jil ",2,screen_h-font_h,c_blanc,os)
 else:
   fill_rect(1,screen_h-font_h,screen_w,font_h,os)
   s = systeme[n][t]
   if t==1 and n:
     s = "periode de revo: " + s + ((n <=4 ) and " jours" or " ans")
   elif t==2:
     s = "dis soleil: " + s + " milli" + ((n <= 5 ) and "on" or "ard") + "s km"
   elif t==3:
     s = "masse: " + s + " kg"
   elif t==4:
     s = "rayon: " + str(s) + " km"
   elif t==5:
     s = "satellites connus: " + str(s)
   draw_string(s,2,screen_h-font_h,c_blanc,os)
 
solar_systeme_texte()
 
def navigation(): #navigation grâce aux flèches
  position = 0
  texte = 0  

  key = 0
  while key != 9:

    key = get_key()

    if key >=1 and key <=4:
      if key <= 2: #Gauche Droite
        avant = position
        position = min(max(position+2*(key == 1)-1, 0), 8) # le soleil [0] + 8 planète
        if avant != position:
          solar_systeme_dessine(avant)
        solar_systeme_dessine(position, 0)

      elif  key >= 3:  #haut bas
        texte = max(min(texte + 2*(key == 3) - 1, 5), 0) # Il faut donc avoir 5 données en plus du nom dans systeme[]

      solar_systeme_texte(position,texte)      

solar_systeme_dessine(0)

for k in range(1,9):
  cercle_grade(coord[k][0],coord[k][1],coord[k][2],couleur1[k],10,couleur2[k])

navigation()