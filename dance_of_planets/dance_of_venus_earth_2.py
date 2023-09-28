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
mercury = Planet(planet_radius=2439, orbital_distance=0.4, revolution_time_period=87.97, color='#B7B8B9')
venus = Planet(planet_radius=6051, orbital_distance=0.72, revolution_time_period=224.7, color='#e6e6e6')
earth = Planet(planet_radius=6378, orbital_distance=1, revolution_time_period=365.25, color='#287AB8')
mars = Planet(planet_radius=3389, orbital_distance=1.524, revolution_time_period=687, color='#993d00')

planet_list = [mercury, venus, mars]
convert_data_relative_earth(earth, planet_list, planet_radius_scale_factor=10, orbital_raidus_scale_factor=1)

number_of_revolutions = 8 # earth revolutions
duration_of_video = 30 # sec
number_of_time_steps = frames_per_second*duration_of_video
t = np.linspace(0, number_of_revolutions*earth.revolution_time_period, number_of_time_steps) 

#------------------------------------------------------------------------------------------------------------------------#
# when venus completes one revolution, join earth's current postion with its previous position where it was, #
# when venus begun its revolution. #
#------------------------------------------------------------------------------------------------------------------------#
count = 0
stoppage_timetamps_list = []
stop_wrt_planet = venus
stop_planet = earth
stop_planet_rev_x, stop_planet_rev_y = stop_planet.get_rev_xy_coordinates(t)
while count*stop_wrt_planet.revolution_time_period < number_of_revolutions*earth.revolution_time_period: 
    foo = count*stop_wrt_planet.revolution_time_period
    stoppage_timetamps_list.append(t[np.argmin(abs(t-foo))])
    count = count+1

#--------------------------------------------------#
# setting up figure and axis to plot each planet #
# sun at center #
#--------------------------------------------------#
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)
ax.set_aspect('equal')
xy_limit_max = mars.orbital_distance

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

for a_planet in planet_list:
    x, y = a_planet.get_rev_xy_coordinates(t)
    a_planet.draw_orbit(ax, 0.5, '-', 'None', 1.5)

#--------------------------------------------------------------------#
# Animating the planet motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
with writer.saving(fig, "dance_of_venus_earth_2.mp4", dpi=200):
    for i, t_item in enumerate(t):
        fig.suptitle('{} earth years'.format(round(t_item/365.25, 1)), fontsize=12, color=earth.color)
        planet_me = mercury.draw_planet(ax, mercury_rev_x[i], mercury_rev_y[i])
        planet_v = venus.draw_planet(ax, venus_rev_x[i], venus_rev_y[i])
        planet_e = earth.draw_planet(ax, earth_rev_x[i], earth_rev_y[i])
        planet_ma = mars.draw_planet(ax, mars_rev_x[i], mars_rev_y[i])

        if t_item in stoppage_timetamps_list:
            if t_item != 0:
                plt.plot([temp_x, stop_planet_rev_x[i]], [temp_y, stop_planet_rev_y[i]], color=stop_planet.color, linewidth=1.0)
            temp_x = stop_planet_rev_x[i]
            temp_y = stop_planet_rev_y[i]
        
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