#!/bin/python3
from PIL import Image, ImageDraw
from logger import Logger
from star_painter import StarPainter
from argument_parser import ArgumentParser
from sys import argv
from random import sample, randint, seed

# Set up logging
logger = Logger()

# Parse arguments
argument_parser = ArgumentParser()

# List of ['argument-name', 'default-value']
POSSIBLE_ARGUMENTS = {'pixels-x': 526, 'pixels-y': 726, 'seed': 6}

# Parse the arguments
arguments = argument_parser.parse(POSSIBLE_ARGUMENTS, argv)
pixels_x = int(arguments['pixels-x'])
pixels_y = int(arguments['pixels-y'])
# Seed PRNG
seed(int(arguments['seed']))

image = Image.new("RGB", (pixels_x, pixels_y), (255,255,255))
draw = ImageDraw.Draw(image)

# Draw some stars
star_painter = StarPainter(image)
star_painter.paint_stars(5, 30, 250, (255,0,0), (255,255,255))

# Draw main diamond
DIAMOND_SIZE = 400
star_painter.paint_star(pixels_x//2, pixels_y//2, DIAMOND_SIZE, (255,0,0), 10)

image.save(f"./output/art.png")
logger.log("painted!")
