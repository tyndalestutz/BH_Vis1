from scipy import special
import matplotlib as plt
from math import pi,cos,sin

#error function
def ERF(x,x0,w):
    return 0.5 * (special.erf(((x)-(x0))/(w)) + 1.0)

destination_directory = r"./"
t_final = 2000
num_data_pts = 1000
deltat = (t_final)/num_data_pts
BH1radius = 0.25
BH2radius = 0.25
orbital_period = 225
omega = 2*pi/orbital_period

#Replace 'synthetic_data.txt' here  
with open(destination_directory + "synthetic_data_BH1xyOnly_Commas.csv", "w") as file:
    file.write("time BH1x BH1y BH1z \n")
    for i in range(num_data_pts):
        time = deltat * i 
        orbital_separation = ERF(time, 1000, -500) 
        #BH1 coords
        BH1x = 0.5 * orbital_separation * cos(omega * time)
        BH1y = 0.5 * orbital_separation * sin(omega * time)
        BH1z = 0
        #BH2 coords
        BH2x = -0.5 * orbital_separation * cos(omega * time)
        BH2y = -0.5 * orbital_separation * sin(omega * time)
        BH2z = 0
        
        #typecast
        outstr = str(time) + "," + str(BH1x) + "," + str(BH1y) + "\n" #+ str(BH2x) + " " + str(BH2y) + "\n"
        file.write(outstr)
