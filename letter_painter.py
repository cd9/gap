
# Letter bank
A = [[1, 1, 1, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 0, 1, 1]]

LETTER_MAP = {'A': A}

class LetterPainter():
    def __init__(self, image):
        self.image = image

    def paint_letter(self, xy, letter, scale, color, flip=False):
        # TODO check if letter in map
        letter_array = LETTER_MAP[letter]
        if flip:
            letter_array = letter_array[::-1]
        y = xy[1] - (scale*len(letter_array))//2
        for row in letter_array:
            for _ in range(scale):
                x = xy[0] - (scale*len(row))//2
                for col in row:
                    for _ in range(scale):
                        x += 1
                        # Paint
                        if col == 1:
                            self.image.putpixel((x, y), color)
                y += 1
