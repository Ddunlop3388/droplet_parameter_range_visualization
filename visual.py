import matplotlib.pyplot as plt
import mplcursors
import numpy as np

########### EDIT THESE ########################################################
# define velocities for each of the studies
vel_ms = [1.0, 90, 90, 90, 90, 20, 100, 30, 50, 150, 50]  # m/s
# define droplet diameters for each of the studies
dia_um = [2.28e3, 20, 52, 111, 236, 420, 2e3, 200, 200, 1e3, 50] # um 

# define names of the studies
names = [
    "Yokoi et al - Numerical studies of the \n influence of the dynamic contact angle \non a droplet impacting on a dry surface",
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
    "Thibault Xavier, Davide Zuzio, Matthias Averseng \n, and J-L Estivalezes. Toward direct \nnumerical simulation of high speed droplet impact",
    "Yanchao Liu, Xu Chu, Guang Yang, and Bernhard \nWeigand. Simulation and analytical modeling \nof high-speed droplet impact onto a surface",
    "Tomoki Kondo and Keita Ando. Simulation of \nhigh-speed droplet impact against a dry/wet rigid \nwall for understanding the mechanism of liquid jet",
    "Tomoki Kondo and Keita Ando. Simulation of \nhigh-speed droplet impact against a dry/wet rigid \nwall for understanding the mechanism of liquid jet",
    "Georgia Nykteri, Phoevos Koukouvinis, \nSilvestre Roberto Gonzalez Avila, Claus-Dieter Ohl, \nand Manolis Gavaises. A σ-υ two-fluid model with dynamic \nlocal topology detection: Application to high-speed droplet impact",
    "Claas Willem Visser et al. Dynamics of \nhigh-speed micro-drop impact: numerical simulations \nand experiments at frame-to-frame times below 100 ns"

]
###############################################################################


########################################################################### First Figure (Velocity and Diameter) ###############################################################
# create the first plot - velocity and diameter axes
plt.figure()

# title plot and label axes
#   velocity as x-coord
#   drop diameter as y coordinate
plt.title("Droplet Size and Velocity Ranges Other Studies")
plt.xlabel("Velocity (m/s)")
plt.ylabel(r"Diameter ($\mu m$)")


# plot the points from the other studies
plt.scatter(vel_ms, dia_um, marker='x')

# create a cursor object
cursor1 = mplcursors.cursor(hover=True)

# show the name of the article when hovering over the point
@cursor1.connect("add")
def on_add(sel):
    index = sel.index
    sel.annotation.set_text(names[index])

@cursor1.connect("remove")
def on_remove(sel):
    sel.annotation.set_visible(False)

############################################################################ Second Figure (Reynolds and Weber Number) ################################################################
# create the second plot - Re and We axes
plt.figure()

# title plot and label axes
#   velocity as x-coord
#   drop diameter as y coordinate
plt.title("Re and We Ranges of Other Studies")
plt.xlabel("Re")
plt.ylabel("We")

# convert vels and dias to numpy arrays
vel_arr_ms = np.array(vel_ms)
dia_arr_um = np.array(dia_um)

# convert diameters to meters
dia_arr_m = np.array(dia_um) * 1e-6

# define properties of water (density, viscosity, surface tension for water-air interface)
rho = 997
mu = 0.89e-3
o = 72.8e-3

# Calculate Re and We number
Re_arr = rho * vel_arr_ms * dia_arr_m / mu
We_arr = rho * vel_arr_ms**2 * dia_arr_m / o

# convert Reynolds and Weber numbers back to a list
Re = Re_arr.tolist()
We = We_arr.tolist()

cursor2 = mplcursors.cursor(hover=True)
# show the name of the article when hovering over the point
@cursor2.connect("add")
def on_add(sel):
    index = sel.index
    sel.annotation.set_text(names[index])

@cursor2.connect("remove")
def on_remove(sel):
    sel.annotation.set_visible(False)

# plot reynolds and Weber numbers
plt.scatter(Re, We, marker='x')

# display plot
plt.show()