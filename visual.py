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
vel_splash_ms = [20, 20, 40, 4.09, 500] # m/s
dia_splash_um = [420, 550, 550, 2630, 200] #um
names_splash = [
    "Thibault Xavier, Davide Zuzio, Matthias Averseng, \nand J-L Estivalezes. Toward direct numerical \nsimulation of high speed droplet impact.",
    "NZ Mehdizadeh, S Chandra, and J Mostaghimi. \nSplashing of a small droplet impinging \non a solid surface at high velocity",
    "NZ Mehdizadeh, S Chandra, and J Mostaghimi. \nSplashing of a small droplet impinging \non a solid surface at high velocity",
    "Xiaodan Lin, Qiao Wang, Yingchun Wu, Longchao \nYao, Zhiliang Xue, and Xuecheng Wu. 3d \nvisualization of droplet splash dynamics with high-speed digital holography.",
    "KK Haller, Y Ventikos, D Poulikakos, and P \nMonkewitz. Computational study of high-speed\n liquid droplet impact."
]

# velocities, diameters, and studies which recorded full rebounding behavior - FOR MOST STUDIES, WE DON'T HAVE ENOUGH INFO TO TELL FULL REBOUND FROM DEPOSITION
"""
vel_fr_ms = [90, 90]
dia_fr_um = [20, 52]
names_fr = [
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
    "Radu Cimpeanu and Demetrios T Papageorgiou. \nThree-dimensional high speed drop impact \nonto solid surfaces at arbitrary angles",
]
"""

# velocities, diameters, and studies which recorded deposition behavior
vel_spr_ms = [1.0, 10, 0.277, 1.417, 50, 16.9]
dia_spr_um = [2.28e3, 550, 2e3, 2e3, 200, 49.5]
names_spr = [
    "Yokoi et al - Numerical studies of the \n influence of the dynamic contact angle \non a droplet impacting on a dry surface", 
    "NZ Mehdizadeh, S Chandra, and J Mostaghimi. \nSplashing of a small droplet impinging \non a solid surface at high velocity",
    "G Chaidron, A Soucemarianadin, and P Attan´e. \nStudy of the impact of drops onto solid surfaces",
    "G Chaidron, A Soucemarianadin, and P Attan´e. \nStudy of the impact of drops onto solid surfaces",
    "Tomoki Kondo and Keita Ando. Simulation of \nhigh-speed droplet impact against a dry/wet \nrigid wall for understanding the mechanism of liquid jet cleaning",
    "Claas Willem Visser, Philipp Erhard Frommhold, \nSander Wildeman, Robert Mettin, Detlef Lohse, \nand Chao Sun. Dynamics of high-speed micro-drop impact"
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

# scatter the data for each specific case of droplet behavior: red: splash, blue: full rebound, green: deposition
scatter_splash = plt.scatter(vel_splash_ms, dia_splash_um, marker='x', color="red") 
scatter_spr = plt.scatter(vel_spr_ms, dia_spr_um, marker='x', color='green')

# create a cursor for each specific case of droplet behavior
mplcursors.cursor(scatter_splash, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_splash[sel.index]))
mplcursors.cursor(scatter_spr, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_spr[sel.index]))

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
vel_arr_spr_ms = np.array(vel_spr_ms)
dia_arr_spr_um = np.array(dia_spr_um)

# convert diameters to meters
dia_arr_splash_m = np.array(dia_splash_um) * 1e-6
dia_arr_spr_m = np.array(dia_spr_um) * 1e-6

# define properties of water (density, viscosity, surface tension for water-air interface)
rho = 997
mu = 0.89e-3
o = 72.8e-3

# Calculate Re and We number for different impact cases
Re_arr_splash = rho * vel_arr_splash_ms * dia_arr_splash_m / mu
We_arr_splash = rho * vel_arr_splash_ms**2 * dia_arr_splash_m / o
Re_arr_spr = rho * vel_arr_spr_ms * dia_arr_spr_m / mu
We_arr_spr = rho * vel_arr_spr_ms**2 * dia_arr_spr_m / o

# convert Reynolds and Weber numbers back to a list
Re_splash = Re_arr_splash.tolist()
We_splash = We_arr_splash.tolist()
Re_spr = Re_arr_spr.tolist()
We_spr = We_arr_spr.tolist()

# plot the data for each specific case of droplet behavior
scatter2_splash = plt.scatter(Re_splash, We_splash, marker='x', color='red')
scatter2_spr = plt.scatter(Re_spr, We_spr, marker='x', color='green')

# create a cursor for each specific case of droplet behavior
mplcursors.cursor(scatter2_splash, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_splash[sel.index]))
mplcursors.cursor(scatter2_spr, hover=True).connect("add", lambda sel: sel.annotation.set_text(names_spr[sel.index]))

# print Reynolds and Weber numbers 
print(Re_splash)
print(We_splash)
print(Re_spr)
print(We_spr)

# display plot
plt.show()