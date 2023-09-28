from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter
from planet import Planet, convert_data_relative_earth, np

#------------------------------------------------------------#
# setting up writer object to save mp4 video #
#------------------------------------------------------------#
metadata = dict(title='solar system', artist='ZaidShamsi',
                comment='solar system circular orbit')
frames_per_second = 24
writer = FFMpegWriter(fps=frames_per_second, metadata=metadata)

# ffmpeg executable downloaded from https://github.com/BtbN/FFmpeg-Builds/releases for windows 64
# update the path to ffmpeg.exe (usually located in bin folder)
plt.rcParams['animation.ffmpeg_path'] = r'..\ffmpeg.exe'

# mercury - #1a1a1a, #B7B8B9
# Jupiter - #b07f35 #e1e1e2
# Saturn - #b08f36 #fae5bf
# Uranus - #5580aa #ACE5EE
# neptune - #366896 #5b5ddf
mercury = Planet(planet_radius=2439, orbital_distance=0.4, revolution_time_period=87.97, color='#B7B8B9')
venus = Planet(planet_radius=6051, orbital_distance=0.72, revolution_time_period=224.7, color='#e6e6e6')
earth = Planet(planet_radius=6378, orbital_distance=1, revolution_time_period=365.25, color='#287AB8')
mars = Planet(planet_radius=3389, orbital_distance=1.524, revolution_time_period=687, color='#993d00')
jupiter = Planet(planet_radius=69911, orbital_distance=5.2, revolution_time_period=4330.6, color='#b07f35')
saturn = Planet(planet_radius=58232, orbital_distance=9.5, revolution_time_period=10756, color='#b08f36')
uranus = Planet(planet_radius=25362, orbital_distance=19.8, revolution_time_period=30687, color='#5580aa')
neptune = Planet(planet_radius=24662, orbital_distance=30, revolution_time_period=60190, color='#366896')

planet_list = [mercury, venus, mars, jupiter, saturn, uranus, neptune]
convert_data_relative_earth(earth, planet_list, planet_radius_scale_factor=10, orbital_raidus_scale_factor=1)

number_of_revolutions = 165 # earth revolutions
duration_of_video = 165 # sec
number_of_time_steps = frames_per_second*duration_of_video
t = np.linspace(0, number_of_revolutions*earth.revolution_time_period, number_of_time_steps)

#--------------------------------------------------#
# setting up figure and axis to plot each planet #
# sun at center #
#--------------------------------------------------#
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)
ax.set_aspect('equal')
xy_limit_max = np.max([mercury.orbital_distance, venus.orbital_distance, earth.orbital_distance, mars.orbital_distance,
                   jupiter.orbital_distance, saturn.orbital_distance, uranus.orbital_distance, neptune.orbital_distance])
xy_limit_max = neptune.orbital_distance
xy_limt_min = 1.5*earth.orbital_distance

xy_limit_vec_zoom_in = np.geomspace(xy_limit_max, xy_limt_min, int(number_of_time_steps/2))
xy_limit_vec_zoom_out = np.geomspace(xy_limt_min, xy_limit_max, int(number_of_time_steps/2))
xy_limit_zoom = np.append(xy_limit_vec_zoom_in, xy_limit_vec_zoom_out)

def set_axis_limit(axes_object, xy_limit, factor=1.1):
    custom_xlim = (-factor*xy_limit, factor*xy_limit)
    custom_ylim = (-factor*xy_limit, factor*xy_limit)
    axes_object.set_xlim(custom_xlim)
    axes_object.set_ylim(custom_ylim)

set_axis_limit(ax, xy_limit_max)
ax.set_facecolor('black')

mercury_rev_x, mercury_rev_y = mercury.get_rev_xy_coordinates(t)
venus_rev_x, venus_rev_y = venus.get_rev_xy_coordinates(t)
earth_rev_x, earth_rev_y = earth.get_rev_xy_coordinates(t)
mars_rev_x, mars_rev_y = mars.get_rev_xy_coordinates(t)
jupiter_rev_x, jupiter_rev_y = jupiter.get_rev_xy_coordinates(t)
saturn_rev_x, saturn_rev_y = saturn.get_rev_xy_coordinates(t)
uranus_rev_x, uranus_rev_y = uranus.get_rev_xy_coordinates(t)
neptune_rev_x, neptune_rev_y = neptune.get_rev_xy_coordinates(t)

for a_planet in planet_list:
    a_planet.draw_orbit(ax, 0.6, '-', 'None', 1.5)

#--------------------------------------------------------------------#
# Animating the planet motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
with writer.saving(fig, "solar_system.mp4", dpi=200):
    for i, t_item in enumerate(t):
        fig.suptitle('{} earth years'.format(round(t_item/365.25, 1)), fontsize=12, color=earth.color)
        planet_me = mercury.draw_planet(ax, mercury_rev_x[i], mercury_rev_y[i])
        planet_v = venus.draw_planet(ax, venus_rev_x[i], venus_rev_y[i])
        planet_e = earth.draw_planet(ax, earth_rev_x[i], earth_rev_y[i])
        planet_ma = mars.draw_planet(ax, mars_rev_x[i], mars_rev_y[i])
        planet_j = jupiter.draw_planet(ax, jupiter_rev_x[i], jupiter_rev_y[i])
        planet_s = saturn.draw_planet(ax, saturn_rev_x[i], saturn_rev_y[i])
        planet_u = uranus.draw_planet(ax, uranus_rev_x[i], uranus_rev_y[i])
        planet_n = uranus.draw_planet(ax, neptune_rev_x[i], neptune_rev_y[i])
        plt.pause(0.001)
        writer.grab_frame()
        set_axis_limit(ax, xy_limit_zoom[i])
        if i != len(t)-1:
            planet_me.remove()
            planet_v.remove()
            planet_e.remove()
            planet_ma.remove()
            planet_j.remove()
            planet_s.remove()
            planet_u.remove()
            planet_n.remove()

plt.show()