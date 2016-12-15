import cv2
import numpy
import math
import sys
import os
import fnmatch

def line_deg_angle(x1, y1, x2, y2):
    return math.atan2(y2-y1, x2-x1)*(180/math.pi)

def has_vertical_lanes(lines):
    if lines == None:
        return False
    for items in lines:
        x1, y1, x2, y2 = items[0]
        if abs(line_deg_angle(x1, y1, x2, y2)) >= 50:
            return True
    return False


def has_horizontal_lanes(lines):
    if lines == None:
        return False
    for items in lines:
        x1, y1, x2, y2 = items[0]
        if abs(line_deg_angle(x1, y1, x2, y2)) <= 40:
            return True
    return False

def has_lane_intersections(lines):
    if has_horizontal_lanes(lines) and has_vertical_lanes(lines):
        return True
    return False

def has_left_end_lane(lines):
    if lines == None:
        return False
    for items in lines:
        x1, y1, x2, y2 = items[0]
        if abs(line_deg_angle(x1, y1, x2, y2)) == 0:
            return True
    return False

def has_right_end_lane(lines):
    if lines == None:
        return False
    for items in lines:
        x1, y1, x2, y2 = items[0]
        if abs(line_deg_angle(x1, y1, x2, y2)) == 0:
            return True
    return False

def get_key(line_key):
    return line_key[0][0]

def sort_lines(lines):
    return sorted(lines, key=get_key)

def process_image(image):
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## grayscale
    blurred_gray = cv2.GaussianBlur(gray, (33, 33), 0)
    thresh = cv2.threshold(blurred_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    edges = cv2.Canny(thresh, 50, 100, apertureSize=3) ## detect edges
    lines = cv2.HoughLinesP(edges, 1, numpy.pi/180, 100, 20, 10) ## detect hough lines
    return (gray, edges, lines,)

def slice_left_end(image):
    # global test_index
    height, width = image.shape
    x_end = int(width * .33)
    crop_img = image[0:height, 0:x_end]
    cropped_lines = cv2.HoughLinesP(crop_img, 1, numpy.pi/180, 100, 20, 10)
    # cv2.imwrite('cropped{}.png'.format(test_index), crop_img)
    return has_horizontal_lanes(cropped_lines)

def slice_right_end(image):
    # global test_index
    height, width = image.shape
    x_end = int(width * .33)
    crop_img = image[0:height, x_end:width]
    cropped_lines = cv2.HoughLinesP(crop_img, 1, numpy.pi/180, 100, 20, 10)
    # cv2.imwrite('cropped{}.png'.format(test_index), crop_img)
    return has_horizontal_lanes(cropped_lines)

test_index = 0
def output_edges(edges, name):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(edges,name,(10,500), font, 1,(255,255,255),2)
    cv2.imwrite('testedge{}.png'.format(test_index), edges)

def classify_shape(image_path):
    global test_index
    test_index = test_index + 1
    image = cv2.imread(image_path) ## read the image
    gray, edges, lines = process_image(image)
    if lines is None:
        return False
    if has_lane_intersections(lines):
        # output_edges(edges, 'lane intersections')
        print('%s\t%s' % (image_path, 'lane intersections'))
    elif has_horizontal_lanes(lines):
        if not slice_left_end(edges):
            # output_edges(edges, 'north end')
            print('%s\t%s' % (image_path, 'north end'))
        elif not slice_right_end(edges):
            # output_edges(edges, 'north end')
            print('%s\t%s' % (image_path, 'south end'))
        else:
            # output_edges(edges, 'horizontal lanes')
            print('%s\t%s' % (image_path, 'horizontal lanes'))
    elif has_vertical_lanes(lines):
        # output_edges(edges, 'virtical lanes')
        print('%s\t%s' % (image_path, 'vertical lanes'))
    else:
        # output_edges(edges, 'no lanes')
        print('%s\t%s' % (test_index, 'no lanes'))

def classify_shapes_in_dir(imgdir, filepat):
    # import ipdb; ipdb.set_trace()
    for path, dirlist, filelist in os.walk(imgdir):
        for filename in fnmatch.filter(filelist, filepat):
            fp = os.path.join(path, filename)
            # print('fp', fp)
            classify_shape(fp)

def classify_shapes_unit_test(imgdir, filepat):
    classify_shapes_in_dir(imgdir, filepat)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    classify_shapes_in_dir('{}/images'.format(dir_path), '*.png')
