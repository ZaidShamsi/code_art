import numpy as np

# Logarithmic spiral
class LogarithmicSpiral():
    def __init__(self, a, b, k, n, d):
        # a -> controls the distance from the origin along the x-Axis
        # b -> changes the starting value of the spiral along the x-Axis
        # k -> controls the tightness of the successive rotations
        # n -> number of spiral turns
        # d -> number of points in which curve is discretized
        self.a = a
        self.b = b
        self.k = k
        self.n = n
        self.d = d
        
    def xy_logarithmic_spiral(self):
        phi = np.linspace(0, self.n*np.pi, self.n*self.d)
        r = self.a*np.exp(self.k*phi)+self.b
        x = r*np.cos(phi)
        y = r*np.sin(phi)
        return x, y
    
    def rotation(self, theta, orientation):
        x, y = self.xy_logarithmic_spiral()
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        xy_array = np.array([x, y])
        if orientation == 'anti-clockwise':
            rotated_square = np.dot(rotation_matrix, xy_array)
            x = rotated_square[0, :]
            y = rotated_square[1, :]
        elif orientation == 'clockwise':
            rotated_square = np.dot(np.transpose(xy_array), rotation_matrix)
            x = rotated_square[:, 0]
            y = rotated_square[:, 1]
        return x, y
    
    def reflection(self, theta, orientation):
        # reflection about a line at an angle
        x, y = self.rotation(theta, orientation)
        reflection_matrix = np.array([[np.cos(2*theta), np.sin(2*theta)], [np.sin(2*theta), -np.cos(2*theta)]])
        xy_array = np.array([x, y])
        if orientation == 'anti-clockwise':
            reflected_spiral = np.dot(reflection_matrix, xy_array)
            x = reflected_spiral[0, :]
            y = reflected_spiral[1, :]
        elif orientation == 'clockwise':
            reflected_spiral = np.dot(np.transpose(xy_array), reflection_matrix)
            x = reflected_spiral[:, 0]
            y = reflected_spiral[:, 1]
        return x, y
    

def intertwine_two_vectors(vector1, vector2):
    intertwined_vector = [None]*(len(vector1)+len(vector2))
    intertwined_vector[::2] = vector1
    intertwined_vector[1::2] = vector2
    return intertwined_vector