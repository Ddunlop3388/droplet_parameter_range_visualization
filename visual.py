import matplotlib.pyplot as plt
import mplcursors
import numpy as np

########### EDIT THESE ########################################################
# define velocities for each of the studies
vel_ms = [1.0, 90, 90, 90, 90, 20, 100, 30, 50, 150, 50]  # m/s
# define droplet diameters for each of the studies
dia_um = [2.28e3, 20, 52, 111, 236, 420, 2e3, 200, 200, 1e3, 50] # um 
# define droplet behavior for each study
behavior = ['fr', 'fr', 'fr', 'spl', 'spl', '.', '.',  '.', '.', '.', '.']

# velocities, diameters, and studies which recorded splashing behavior
vel_splash_ms = [90, 90] # m/s
dia_splash_um = [111, 236] #um
names_splash = [
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles"
]

# velocities, diameters, and studies which recorded full rebounding behavior
vel_fr_ms = [90, 90]
dia_fr_um = [20, 52]
names_fr = [
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
]

# velocities, diameters, and studies which recorded deposition behavior
vel_dep_ms = [1.0]
dia_dep_um = [2.28e3]
names_dep = [
    "Yokoi et al - Numerical studies of the \n influence of the dynamic contact angle \non a droplet impacting on a dry surface"
]


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

# scatter the data for each specific case of droplet behavior
scatter_splash = plt.scatter(vel_splash_ms, dia_splash_um, marker='x', color="red")
scatter_fr = plt.scatter(vel_fr_ms, dia_fr_um, marker='x', color="blue")
scatter_dep = plt.scatter(vel_dep_ms, dia_dep_um, marker='x', color='green')

# create a cursor for each specific case of droplet behavior
mplcursors.cursor(scatter_splash, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_splash[sel.index]))
mplcursors.cursor(scatter_fr, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_fr[sel.index]))
mplcursors.cursor(scatter_dep, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_dep[sel.index]))

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
vel_arr_splash_ms = np.array(vel_splash_ms)
dia_arr_splash_um = np.array(dia_splash_um)
vel_arr_fr_ms = np.array(vel_fr_ms)
dia_arr_fr_um = np.array(dia_fr_um)
vel_arr_dep_ms = np.array(vel_dep_ms)
dia_arr_dep_um = np.array(dia_dep_um)

# convert diameters to meters
dia_arr_splash_m = np.array(dia_splash_um) * 1e-6
dia_arr_fr_m = np.array(dia_fr_um) * 1e-6
dia_arr_dep_m = np.array(dia_dep_um) * 1e-6

# define properties of water (density, viscosity, surface tension for water-air interface)
rho = 997
mu = 0.89e-3
o = 72.8e-3

# Calculate Re and We number for different impact cases
Re_arr_splash = rho * vel_arr_splash_ms * dia_arr_splash_m / mu
We_arr_splash = rho * vel_arr_splash_ms**2 * dia_arr_splash_m / o
Re_arr_fr = rho * vel_arr_fr_ms * dia_arr_fr_m / mu
We_arr_fr = rho * vel_arr_fr_ms**2 * dia_arr_fr_m / o
Re_arr_dep = rho * vel_arr_dep_ms * dia_arr_dep_m / mu
We_arr_dep = rho * vel_arr_dep_ms**2 * dia_arr_dep_m / o

# convert Reynolds and Weber numbers back to a list
Re_splash = Re_arr_splash.tolist()
We_splash = We_arr_splash.tolist()
Re_fr = Re_arr_fr.tolist()
We_fr = We_arr_fr.tolist()
Re_dep = Re_arr_dep.tolist()
We_dep = We_arr_dep.tolist()

# plot the data for each specific case of droplet behavior
scatter2_splash = plt.scatter(Re_splash, We_splash, marker='x', color='red')
scatter2_fr = plt.scatter(Re_fr, We_fr, marker='x', color='blue')
scatter2_dep = plt.scatter(Re_dep, We_dep, marker='x', color='green')

# create a cursor for each specific case of droplet behavior
mplcursors.cursor(scatter2_splash, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_splash[sel.index]))
mplcursors.cursor(scatter2_fr, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_fr[sel.index]))
mplcursors.cursor(scatter2_dep, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_dep[sel.index]))

# print Reynolds and Weber numbers 
print(Re_splash)
print(We_splash)
print(Re_fr)
print(We_fr)
print(Re_dep)
print(We_dep)

# display plot
plt.show()