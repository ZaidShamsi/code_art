from matplotlib import pyplot as plt
import numpy as np

print('Hello!')


class Circle:

    def __init__(self, x_center_location, y_center_location, radius, points_on_circle):
        self.x_center_location = x_center_location
        self.y_center_location = y_center_location
        self.radius = radius
        self.points_on_circle = points_on_circle
        self.theta = np.linspace(0, 2 * np.pi, self.points_on_circle)

    def x_coordinates(self):
        x_circle = self.x_center_location + self.radius * np.cos(self.theta)
        return x_circle

    def y_coordinates(self):
        y_circle = self.y_center_location + self.radius * np.sin(self.theta)
        return y_circle


class Square:

    def __init__(self, x_center_location, y_center_location, diagonal_length, points_on_each_side):
        self.x_center_location = x_center_location
        self.y_center_location = y_center_location
        self.diagonal_length = diagonal_length
        self.points_on_each_side = points_on_each_side

    def x_coordinates(self):
        side_1 = np.linspace(0.5 * self.diagonal_length, self.x_center_location, self.points_on_each_side,
                             endpoint=False)
        side_2 = np.linspace(self.x_center_location, -0.5 * self.diagonal_length, self.points_on_each_side,
                             endpoint=False)
        side_3 = np.linspace(-0.5 * self.diagonal_length, self.x_center_location, self.points_on_each_side,
                             endpoint=False)
        side_4 = np.linspace(self.x_center_location, 0.5 * self.diagonal_length, self.points_on_each_side+1,
                             endpoint=True)
        x_square = list(side_1) + list(side_2) + list(side_3) + list(side_4)
        return x_square

    def y_coordinates(self):
        side_1 = np.linspace(self.y_center_location, 0.5 * self.diagonal_length, self.points_on_each_side,
                             endpoint=False)
        side_2 = np.linspace(0.5 * self.diagonal_length, self.y_center_location, self.points_on_each_side,
                             endpoint=False)
        side_3 = np.linspace(self.y_center_location, -0.5 * self.diagonal_length, self.points_on_each_side,
                             endpoint=False)
        side_4 = np.linspace(-0.5 * self.diagonal_length, self.y_center_location, self.points_on_each_side+1,
                             endpoint=True)
        y_square = list(side_1) + list(side_2) + list(side_3) + list(side_4)
        return y_square

    def rotation(self, theta, orientation):
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        xy_square = np.array([self.x_coordinates(), self.y_coordinates()])
        if orientation == 'anti-clockwise':
            rotated_square = np.dot(rotation_matrix, xy_square)
            x = rotated_square[0, :]
            y = rotated_square[1, :]
        elif orientation == 'clockwise':
            rotated_square = np.dot(np.transpose(xy_square), rotation_matrix)
            x = rotated_square[:, 0]
            y = rotated_square[:, 1]
        return x, y


outer_circle = Circle(0, 0, 1, 21)
square_1 = Square(0, 0, 2, 5)
square_2 = Square(0, 0, 4, 5)
square_3 = Square(0, 0, 6, 5)

plt.axis('equal')
plt.axis('off')

square_obj_list = [square_1, square_2]
orientation_list = ['clockwise', 'anti-clockwise']

square_obj_list.append(square_3)
orientation_list.append('clockwise')

# helper function for base_image function (a square and circle pair is drawn)
def draw_circle_square_line_segments(sqr_obj, theta, orientation):
    x_sqr_obj, y_sqr_obj = sqr_obj.rotation(theta=theta, orientation=orientation)
    x_zip = zip(outer_circle.x_coordinates(), x_sqr_obj)
    y_zip = zip(outer_circle.y_coordinates(), y_sqr_obj)
    l2d_obj_list = []
    for xy in zip(x_zip, y_zip):
        l2d_obj, = plt.plot(xy[0], xy[1])
        l2d_obj_list.append(l2d_obj)
    return l2d_obj_list


# helper function for animate function (all square and circle pairs are drawn)
def base_image(theta, is_marker):
    marker_properties = ['marker', 'o', 'markersize', 2, 'markerfacecolor', 'black']
    line_properties = ['linestyle', '-', 'linewidth', 1.0, 'alpha', 1.0]
    if is_marker == 'yes':
        line_properties.extend(marker_properties)
    elif is_marker == 'no':
        pass

    l2d_list = []
    for sqr_obj, orientation in zip(square_obj_list, orientation_list):
        square_circle_line2d_list = draw_circle_square_line_segments(sqr_obj, theta, orientation)
        l2d_list.extend(square_circle_line2d_list)

    plt.setp(l2d_list, *line_properties)
    return l2d_list


def animate(number_of_frames):
    theta_vec = np.linspace(0, 2*np.pi, number_of_frames)
    for index, theta_val in enumerate(theta_vec):
        if index == 0:
            all_line2D_obj_on_each_frame = base_image(theta_val, is_marker='yes')
        else:
            all_line2D_obj_on_each_frame = base_image(theta_val, is_marker='yes')
        plt.pause(0.01)
        if index != len(theta_vec)-1:
            all_line2D_obj_on_each_frame[:] = [l2d.remove() for l2d in all_line2D_obj_on_each_frame]


animate(number_of_frames=91)
plt.show()