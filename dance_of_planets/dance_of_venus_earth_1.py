from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter
from planet import Planet, convert_data_relative_earth, np

#------------------------------------------------------------#
# setting up writer object to save mp4 video #
#------------------------------------------------------------#
metadata = dict(title='dance of venus and earth', artist='ZaidShamsi',
                comment='venus earth string art')
frames_per_second = 24
writer = FFMpegWriter(fps=frames_per_second, metadata=metadata)

# ffmpeg executable downloaded from https://github.com/BtbN/FFmpeg-Builds/releases for windows 64
# update the path to ffmpeg.exe (usually located in bin folder)
plt.rcParams['animation.ffmpeg_path'] = r'..\ffmpeg.exe'

# mercury - #1a1a1a, #B7B8B9
# venus - #e6e6e6, #f8e2b0
# mars - #993d00, #ad6242
mercury = Planet(planet_radius=2439, orbital_distance=0.4, revolution_time_period=87.97, color='#1a1a1a')
venus = Planet(planet_radius=6051, orbital_distance=0.72, revolution_time_period=224.7, color='#e6e6e6')
earth = Planet(planet_radius=6378, orbital_distance=1, revolution_time_period=365.25, color='#287AB8')
mars = Planet(planet_radius=3389, orbital_distance=1.524, revolution_time_period=687, color='#993d00')

planet_list = [mercury, venus, mars]
convert_data_relative_earth(earth, planet_list, planet_radius_scale_factor=10, orbital_raidus_scale_factor=1)

number_of_revolutions = 8 # earth revolutions
duration_of_video = 30 # sec
number_of_time_steps = frames_per_second*duration_of_video
t = np.linspace(0, number_of_revolutions*earth.revolution_time_period, number_of_time_steps) 

#--------------------------------------------#
# setting up figure and axis to plot planets #
# sun at center #
#--------------------------------------------#
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)
ax.set_aspect('equal')
xy_limit = np.max([mercury.orbital_distance, venus.orbital_distance, earth.orbital_distance, mars.orbital_distance])
custom_xlim = (-1.1*xy_limit, 1.1*xy_limit)
custom_ylim = (-1.1*xy_limit, 1.1*xy_limit)
ax.set_xlim(custom_xlim)
ax.set_ylim(custom_ylim)
ax.set_facecolor('black')

mercury_rev_x, mercury_rev_y = mercury.get_rev_xy_coordinates(t)
venus_rev_x, venus_rev_y = venus.get_rev_xy_coordinates(t)
earth_rev_x, earth_rev_y = earth.get_rev_xy_coordinates(t)
mars_rev_x, mars_rev_y = mars.get_rev_xy_coordinates(t)

#--------------------------------------------------------------------#
# Animating venus and earth motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
with writer.saving(fig, "dance_of_venus_and_earth_1.mp4", dpi=200):
    for i, t_item in enumerate(t):
        fig.suptitle('{} earth years'.format(round(t_item/365.25, 1)), fontsize=12, color=earth.color)
        line = plt.plot([venus_rev_x[i], earth_rev_x[i]], [venus_rev_y[i], earth_rev_y[i]], color='#287AB8', alpha=0.2, linewidth=1.0)
        planet_me = mercury.draw_planet(ax, mercury_rev_x[i], mercury_rev_y[i])
        planet_v = venus.draw_planet(ax, venus_rev_x[i], venus_rev_y[i])
        planet_e = earth.draw_planet(ax, earth_rev_x[i], earth_rev_y[i])
        planet_ma = mars.draw_planet(ax, mars_rev_x[i], mars_rev_y[i])

        plt.pause(0.001)
        writer.grab_frame()
        if i != len(t)-1:
            planet_me.remove()
            planet_v.remove()
            planet_e.remove()
            planet_ma.remove()

    # Adding 2 secs more video time, grabbing final screen
    for i in range(0, 2*24):
        writer.grab_frame()


plt.show()