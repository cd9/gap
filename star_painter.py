from random import randint, sample

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

X_OFFSET = 1
Y_OFFSET = 1
MIN_NUM = 0.001

class StarPainter():

    def __init__(self, image, tail_factor, base_color):
        self.image = image
        self.tail_factor = tail_factor
        self.base_color = base_color

    def paint_star(self, center_x, center_y, width):
        height = width

        # Top to bottom
        for i in range(1,height):
            y = max(int(abs(i - height/2)),MIN_NUM)
            threshold = (self.tail_factor/y) * (width/2) - X_OFFSET

            # Left to right
            for j in range(1,width):
                x = max(int(abs(j - width/2)),MIN_NUM)
                # Apply the function to check if we should fill in this pixel
                if x < threshold:
                    self.image.putpixel((i+center_x,j+center_y), self.base_color)

    def paint_stars(self, pixels_x, pixels_y, min_width, max_width):
        all_points = set()
        for i in range(pixels_x-100):
            for j in range(pixels_y-100):
                all_points.add((i,j))

        sampled_points = sample(all_points, 20)
        for point in sampled_points:
            self.paint_star(point[0], point[1], randint(min_width,max_width))
