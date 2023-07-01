import numpy as np

# Archimedean spiral
class ArchimedeanSpiral():

    def __init__(self, a, b, n, d):
        # n -> number of spiral turns
        # d -> number of points in which curve is discretized
        # a -> changing a moves the centerpoint of spiral outward from the origin
        # b -> controls the distance between the loops
        self.a = a
        self.b = b
        self.n = n
        self.d = d

    def xy_archimedean_spiral(self):
        phi = np.linspace(0, self.n*np.pi, self.n*self.d)
        r = self.a + self.b*phi
        x = np.multiply(r, np.cos(phi))
        y = np.multiply(r, np.sin(phi))
        return x, y
    
    def rotation(self, theta, orientation):
        x, y = self.xy_archimedean_spiral()
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        xy_array = np.array([x, y])
        if orientation == 'anti-clockwise':
            rotated_spiral = np.dot(rotation_matrix, xy_array)
            x = rotated_spiral[0, :]
            y = rotated_spiral[1, :]
        elif orientation == 'clockwise':
            rotated_spiral = np.dot(np.transpose(xy_array), rotation_matrix)
            x = rotated_spiral[:, 0]
            y = rotated_spiral[:, 1]
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
