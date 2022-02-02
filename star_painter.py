from random import randint, sample, uniform
from helpers import lerp

# A class to paint stars all over the canvas.
# A star is something that looks like this:
#
#         #
#         #
#        ###
#       #####
#     #########
#   #############
#     #########
#       #####
#        ###
#         #
#         #
#
# i.e, that "tails out" towards the edges.
# i.e, the graph of y=a/x but mirrored for each quadrant.

MARGIN_FACTOR = 1
X_OFFSET = 0
MIN_NUM = 0.001

class StarPainter():

    def __init__(self, image):
        self.image = image

    def paint_star(self, center_x, center_y, width, color, tail_factor):
        if width%2==0:
            width += 1
        height = int(width*1.25)
        if height%2==0:
            height += 1

        # Left to right
        for i in range(1,width):
            y = max(abs(i - width/2),MIN_NUM)
            threshold = (tail_factor/y) * (width/2) - X_OFFSET

            # Top to bottom
            for j in range(1,height):
                x = max(abs(j - height/2),MIN_NUM)
                # Apply the function to check if we should fill in this pixel
                if x < threshold:
                    self.image.putpixel((i + center_x - width//2, j + center_y - height//2), color)

    def paint_stars(self, min_width, max_width, num_stars, min_color, max_color, tail_factor=1):
        pixels_x = self.image.size[0]
        pixels_y = self.image.size[1]

        # Get possible points
        all_points = set()
        margin = int(MARGIN_FACTOR*max_width)
        for i in range(margin, pixels_x-margin, margin//4):
            for j in range(margin, pixels_y-margin, margin//4):
                offset_x = randint(-10,10)
                offset_y = randint(-10,10)
                all_points.add((i+offset_x,j+offset_y))

        sampled_points = sample(all_points, num_stars)
        for point in sampled_points:
            shade  = uniform(0,1)
            color = tuple(int(lerp(min_color[x], max_color[x], shade)) for x in [0,1,2])
            self.paint_star(point[0], point[1], randint(min_width,max_width), color, tail_factor)
