#!/bin/python3
from PIL import Image, ImageDraw
from logger import Logger
from star_painter import StarPainter
from letter_painter import LetterPainter
from argument_parser import ArgumentParser
from sys import argv
from random import sample, randint, seed

# Set up logging
logger = Logger()

# Parse arguments
argument_parser = ArgumentParser()

# List of ['argument-name', 'default-value']
POSSIBLE_ARGUMENTS = {'pixels-x': 526, 'pixels-y': 726, 'seed': 7}

# Parse the arguments
arguments = argument_parser.parse(POSSIBLE_ARGUMENTS, argv)
pixels_x = int(arguments['pixels-x'])
pixels_y = int(arguments['pixels-y'])
# Seed PRNG
seed(int(arguments['seed']))

image = Image.new("RGB", (pixels_x, pixels_y), (255,255,255))
draw = ImageDraw.Draw(image)
letter_painter = LetterPainter(image)

# Draw some stars
star_painter = StarPainter(image)
star_painter.paint_stars(5, 30, 250, (255,50,100), (255,255,255))

# Draw main diamond
star_painter.paint_star(pixels_x//2, pixels_y//2, 400, (255,0,0), 10)

RED = (255,0,0,255)
CORNER_DIAMOND_SIZE = 40
CORNER_DIAMOND_CURVE = 3
CORNER_MARGIN_V = 110
CORNER_MARGIN_H = 30
TEXT_MARGIN_V = 45
TEXT_MARGIN_H = 30

# Draw top-left diamond
star_painter.paint_star(CORNER_MARGIN_H, CORNER_MARGIN_V, CORNER_DIAMOND_SIZE, (255,0,0), CORNER_DIAMOND_CURVE)

# Draw bottom-right diamond
star_painter.paint_star(pixels_x - CORNER_MARGIN_H, pixels_y - CORNER_MARGIN_V, CORNER_DIAMOND_SIZE, (255,0,0), CORNER_DIAMOND_CURVE)

# Draw top-left 'A'
letter_painter.paint_letter((TEXT_MARGIN_H, TEXT_MARGIN_V), 'A', 6, RED)

# Draw bottom-right 'A'
letter_painter.paint_letter((pixels_x - TEXT_MARGIN_H, pixels_y - TEXT_MARGIN_V), 'A', 6, RED, True)

image.save(f"./output/art.png")
logger.log("painted!")
