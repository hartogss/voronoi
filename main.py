# Requirements for voronoi program

# define metric
# define image size
# define points
# for each pixel, compute nearest point and color them accordingly
import math
import random
from PIL import Image, ImageDraw

size = (750, 750)

# control points
point_size = 5
points = [(250, 300), (128, 128), (200, 66), (500, 500), (50, 450), (250, 550)]


def random_voronoi_point(limits):
    return VoronoiPoint((random.randint(0, limits[0]), random.randint(0, limits[1])))


class VoronoiPoint:
    location = (0, 0)
    dot_color = (0, 0, 0)
    cell_color = (128, 128, 128)

    def __init__(self, location):
        self.location = location
        self.randomize_color()

    def dump(self):
        print(self.location)

    def randomize_color(self):
        self.cell_color = (random.randint(128, 255),
                           random.randint(128, 255),
                           random.randint(128, 255))



def draw_control_points(draw, nodes):
    for node in nodes:
        draw.ellipse([node.location[0]-point_size, node.location[1]-point_size,
                      node.location[0]+point_size, node.location[1]+point_size], fill=0)


# def distance(point_a, point_b):
#     return math.sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)

def distance(point_a, point_b):
    return (math.fabs(point_a[0]-point_b[0])+ math.fabs(point_a[1]-point_b[1]))

# def distance(point_a, point_b):
    # return math.pow((point_a[0]-point_b[0])**4 + (point_a[1]-point_b[1])**4, 1/4)

def create_nodes(num):
    res = []
    for i in range(0, num):
        res.append(random_voronoi_point(size))
    return res

def check_closest(nodes):
    res = dict()
    num_nodes = len(nodes)
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            coords = (x, y)
            smallest_distance = max(size)
            smallest_index = 0 # should be set to 'no value'
            index = 0
            while index < num_nodes:
                distance1 = distance(coords, nodes[index].location)
                if distance1 < smallest_distance:
                    smallest_index = index
                    smallest_distance = distance1
                index = index+1
            res[coords] = nodes[smallest_index]
    return res

def draw_colors(closest, draw):
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            draw.point([x, y], fill=closest[(x, y)].cell_color)


def main():

    im = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(im)
    nodes = create_nodes(6)
    closest = check_closest(nodes)
    # print(closest)
    draw_colors(closest, draw)
    draw_control_points(draw, nodes)
    im.save('test.jpeg')


if __name__ == '__main__':
    main()
