import cv2
import numpy
import math
import sys
import os
import fnmatch
from BTNode import BTNode

############################################
## CS 3430: Fall 2016: Coding Exam 2
## Your Name Bryant Oblad
## Your A# 01770171
############################################

## ============ Problem 1 ==================

def get_close_enough(point1, point2):
    if point1 + 5 > point2 and point1 - 5 < point2:
        return True
    return False

def line_deg_angle(x1, y1, x2, y2):
    return math.atan2(y2-y1, x2-x1)*(180/math.pi)

def has_vertical_lanes(lines):
    try:
        vertical_1 = lines[0][0][1]
        vertical_2 = lines[0][0][3]
        # print('vertical_1', vertical_1)
        # print('vertical_2', vertical_2)
        try:
            for ln in lines:
                x1, y1, x2, y2 = ln[0]
                # print(x1, y1, x2, y2)
                if get_close_enough(vertical_1, y1) == False or get_close_enough(vertical_2, y2) == False:
                    return False
        except Exception as e:
            print(str(e))
        return True
    except Exception as e:
        print(str(e))
        return False


def has_horizontal_lanes(lines):
    try:
        horizontal_1 = lines[0][0][0]
        horizontal_2 = lines[0][0][2]
        # print('horizontal_1', horizontal_1)
        # print('horizontal_2', horizontal_2)
        try:
            for ln in lines:
                x1, y1, x2, y2 = ln[0]
                # print(x1, y1, x2, y2)
                if get_close_enough(horizontal_1, x1) == False or get_close_enough(horizontal_2, x2) == False:
                    return False
            return True
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
    return True

def has_lane_intersections(lines):
    if has_horizontal_lanes(lines) == True and has_vertical_lanes(lines) == True:
        return True
    return False


def classify_shape(image_path):
    image = cv2.imread(image_path) ## read the image
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## grayscale
    edges = cv2.Canny(gray, 50, 150, apertureSize=3) ## detect edges
    lines = cv2.HoughLinesP(edges, 1, numpy.pi/180, 100, 20, 10) ## detect hough lines
    if has_lane_intersections(lines):
        print('%s\t%s' % (image_path, 'lane intersections'))
    elif has_horizontal_lanes(lines):
        print('%s\t%s' % (image_path, 'horizontal lanes'))
    elif has_vertical_lanes(lines):
        print('%s\t%s' % (image_path, 'vertical lanes'))
    else:
        print('%s\t%s' % (image_path, 'no lanes'))

def classify_shapes_in_dir(imgdir, filepat):
    for path, dirlist, filelist in os.walk(imgdir):
        for filename in fnmatch.filter(filelist, filepat):
            fp = os.path.join(path, filename)
            classify_shape(fp)

def classify_shapes_unit_test(imgdir, filepat):
    classify_shapes_in_dir(imgdir, filepat)

## ========== Problem 2 ================

def display_binary_tree_list(root):
    if root is None:
        print('')
    elif root.getLeftChild() is None and root.getRightChild() is None:
        print('.\n')
    elif not root.getLeftChild() is None:
        print('L')
        display_binary_tree_list(root.getLeftChild())
    elif not root.getRightChild() is None:
        print('R')
        display_binary_tree_list(root.getRightChild())

def generate_binary_tree_lists(h):
    index = 0
    if h == 0:
        yield BTNode(0)
    # if we no its not the root
    root = BtNode()
    root.setKey(h)
    for x in range(h + 1):
        for y in range(x + 1):
            node = BTNode(x):
            if node.getLeftChild() == False || node.getLeftChild() == None:
                node.setLeftChild(node)
            else if  node.getRightChild() == False || node.getRightChild() == None:
                pass
    yield root
    # ran out of time but we need to follow left node all the way down h times,
    # I didnt implement it this way but we need a recursive strategy to build out any possibility
    # of a tree that goes, it will always follow the same pattern, I did a loop because I wasnt



def gen_binary_tree_list_unit_test(h):
    tlsts = [tl for tl in generate_binary_tree_lists(h)]
    print(tlsts)
    print('number of tree lists of depth %d is %d' % (h, len(tlsts)))
    for n, tl in zip(range(1, len(tlsts)+1), tlsts):
        print(n, ')')
        display_binary_tree_list(tl)

## sys.argv[1] is the image directory;
## sys.argv[2] is the file pattern like img.*png
if __name__ == '__main__':
    # uncomment the line below to run your solution to problem 1
    # classify_shapes_unit_test(sys.argv[1], sys.argv[2])

    ## uncomment these two lines after implementing generate_binary_tree_lists(h) for problem 2
    # for h in range(5):
    #    gen_binary_tree_list_unit_test(h)
    # pass
