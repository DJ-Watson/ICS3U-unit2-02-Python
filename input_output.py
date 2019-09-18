#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: September 2019
# This program calculates area and perimeter of a rectangle
# with user input


def main():
    # calculates area and perimeter
    # input code
    length = int(input("Enter rectangle length (mm): "))
    width = int(input("Enter rectangle width (mm): "))
    # process
    area = length*width
    perimeter = 2*(length+width)
    # output code
    print("")
    print("Area is {}mm2".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
