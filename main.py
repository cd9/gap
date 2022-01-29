#!/bin/python3
from PIL import Image, ImageDraw
from logger import Logger
from argument_parser import ArgumentParser
from sys import argv

# Set up logging
logger = Logger()

# Parse arguments
argument_parser = ArgumentParser()

# List of ['argument-name', 'default-value']
POSSIBLE_ARGUMENTS = {'pixels-x': 2500, 'pixels-y': 3500}

# Parse the arguments
arguments = argument_parser.parse(POSSIBLE_ARGUMENTS, argv)
pixels_x = int(arguments['pixels-x'])
pixels_y = int(arguments['pixels-y'])

# Draw some lines
image = Image.new("RGB", (pixels_x, pixels_y))
draw = ImageDraw.Draw(image)
for i in range(0, pixels_x, 1):
    draw.line((0, i, i, 0), fill=(128,128,128))

image.save(f"./output/art.png")
