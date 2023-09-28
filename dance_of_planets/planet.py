import numpy as np

class Planet():
    def __init__(self, planet_radius, orbital_distance, revolution_time_period, color):
        self.planet_radius = planet_radius #km
        self.orbital_distance = orbital_distance #AU
        self.revolution_time_period = revolution_time_period #days
        self.color = color

    def get_angular_speed(self):
        angular_speed = 2*np.pi/self.revolution_time_period #radians/day
        return angular_speed

    def get_rev_xy_coordinates(self, t):
        theta = self.get_angular_speed()*t
        x = self.orbital_distance*np.cos(theta)
        y = self.orbital_distance*np.sin(theta)    
        return x, y
    
    def draw_orbit(self, axes_object, lw, ls, m, ms):
        theta = self.get_angular_speed()*np.linspace(0, self.revolution_time_period, 90)
        x = self.orbital_distance*np.cos(theta)
        y = self.orbital_distance*np.sin(theta)
        axes_object.plot(x, y, linewidth=lw, 
                         linestyle=ls, 
                         marker=m, 
                         markersize = ms,
                         color=self.color)
    
    def draw_planet(self, axes_object, x, y):
        theta = np.linspace(0, 2*np.pi, 40)
        x_circle = x + self.planet_radius*np.cos(theta)
        y_circle = y + self.planet_radius*np.sin(theta)
        planet, = axes_object.fill(x_circle, y_circle, color=self.color)
        return planet
    
def convert_data_relative_earth(earth, other_planet_list, planet_radius_scale_factor=1, orbital_raidus_scale_factor=1):
    for other_planet in other_planet_list:
        radius_ratio = other_planet.planet_radius/earth.planet_radius
        orbital_distance_ratio = other_planet.orbital_distance/earth.orbital_distance
        # If earth's values are considered 1 
        other_planet.planet_radius = radius_ratio/planet_radius_scale_factor
        other_planet.orbital_distance = orbital_distance_ratio*orbital_raidus_scale_factor
    # Earth's values
    earth.planet_radius = 1/planet_radius_scale_factor
    earth.orbital_distance = 1*orbital_raidus_scale_factor
