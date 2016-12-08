__author__ = 'Tommy'
import os
import sys
import cv2
import numpy as np
import math
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager as ftm
from matplotlib.mlab import PCA
from matplotlib import animation
import copy
import struct

from mpl_toolkits.mplot3d import Axes3D
from Homography import *
import six

col_rgb = {
    'snow': (250, 250, 255),
    'snow_2': (233, 233, 238),
    'snow_3': (201, 201, 205),
    'snow_4': (137, 137, 139),
    'ghost_white': (255, 248, 248),
    'white_smoke': (245, 245, 245),
    'gainsboro': (220, 220, 220),
    'floral_white': (240, 250, 255),
    'old_lace': (230, 245, 253),
    'linen': (230, 240, 240),
    'antique_white': (215, 235, 250),
    'antique_white_2': (204, 223, 238),
    'antique_white_3': (176, 192, 205),
    'antique_white_4': (120, 131, 139),
    'papaya_whip': (213, 239, 255),
    'blanched_almond': (205, 235, 255),
    'bisque': (196, 228, 255),
    'bisque_2': (183, 213, 238),
    'bisque_3': (158, 183, 205),
    'bisque_4': (107, 125, 139),
    'peach_puff': (185, 218, 255),
    'peach_puff_2': (173, 203, 238),
    'peach_puff_3': (149, 175, 205),
    'peach_puff_4': (101, 119, 139),
    'navajo_white': (173, 222, 255),
    'moccasin': (181, 228, 255),
    'cornsilk': (220, 248, 255),
    'cornsilk_2': (205, 232, 238),
    'cornsilk_3': (177, 200, 205),
    'cornsilk_4': (120, 136, 139),
    'ivory': (240, 255, 255),
    'ivory_2': (224, 238, 238),
    'ivory_3': (193, 205, 205),
    'ivory_4': (131, 139, 139),
    'lemon_chiffon': (205, 250, 255),
    'seashell': (238, 245, 255),
    'seashell_2': (222, 229, 238),
    'seashell_3': (191, 197, 205),
    'seashell_4': (130, 134, 139),
    'honeydew': (240, 255, 240),
    'honeydew_2': (224, 238, 244),
    'honeydew_3': (193, 205, 193),
    'honeydew_4': (131, 139, 131),
    'mint_cream': (250, 255, 245),
    'azure': (255, 255, 240),
    'alice_blue': (255, 248, 240),
    'lavender': (250, 230, 230),
    'lavender_blush': (245, 240, 255),
    'misty_rose': (225, 228, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'dark_slate_gray': (79, 79, 49),
    'dim_gray': (105, 105, 105),
    'slate_gray': (144, 138, 112),
    'light_slate_gray': (153, 136, 119),
    'gray': (190, 190, 190),
    'light_gray': (211, 211, 211),
    'midnight_blue': (112, 25, 25),
    'navy': (128, 0, 0),
    'cornflower_blue': (237, 149, 100),
    'dark_slate_blue': (139, 61, 72),
    'slate_blue': (205, 90, 106),
    'medium_slate_blue': (238, 104, 123),
    'light_slate_blue': (255, 112, 132),
    'medium_blue': (205, 0, 0),
    'royal_blue': (225, 105, 65),
    'blue': (255, 0, 0),
    'dodger_blue': (255, 144, 30),
    'deep_sky_blue': (255, 191, 0),
    'sky_blue': (250, 206, 135),
    'light_sky_blue': (250, 206, 135),
    'steel_blue': (180, 130, 70),
    'light_steel_blue': (222, 196, 176),
    'light_blue': (230, 216, 173),
    'powder_blue': (230, 224, 176),
    'pale_turquoise': (238, 238, 175),
    'dark_turquoise': (209, 206, 0),
    'medium_turquoise': (204, 209, 72),
    'turquoise': (208, 224, 64),
    'cyan': (255, 255, 0),
    'light_cyan': (255, 255, 224),
    'cadet_blue': (160, 158, 95),
    'medium_aquamarine': (170, 205, 102),
    'aquamarine': (212, 255, 127),
    'dark_green': (0, 100, 0),
    'dark_olive_green': (47, 107, 85),
    'dark_sea_green': (143, 188, 143),
    'sea_green': (87, 139, 46),
    'medium_sea_green': (113, 179, 60),
    'light_sea_green': (170, 178, 32),
    'pale_green': (152, 251, 152),
    'spring_green': (127, 255, 0),
    'lawn_green': (0, 252, 124),
    'chartreuse': (0, 255, 127),
    'medium_spring_green': (154, 250, 0),
    'green_yellow': (47, 255, 173),
    'lime_green': (50, 205, 50),
    'yellow_green': (50, 205, 154),
    'forest_green': (34, 139, 34),
    'olive_drab': (35, 142, 107),
    'dark_khaki': (107, 183, 189),
    'khaki': (140, 230, 240),
    'pale_goldenrod': (170, 232, 238),
    'light_goldenrod_yellow': (210, 250, 250),
    'light_yellow': (224, 255, 255),
    'yellow': (0, 255, 255),
    'gold': (0, 215, 255),
    'light_goldenrod': (130, 221, 238),
    'goldenrod': (32, 165, 218),
    'dark_goldenrod': (11, 134, 184),
    'rosy_brown': (143, 143, 188),
    'indian_red': (92, 92, 205),
    'saddle_brown': (19, 69, 139),
    'sienna': (45, 82, 160),
    'peru': (63, 133, 205),
    'burlywood': (135, 184, 222),
    'beige': (220, 245, 245),
    'wheat': (179, 222, 245),
    'sandy_brown': (96, 164, 244),
    'tan': (140, 180, 210),
    'chocolate': (30, 105, 210),
    'firebrick': (34, 34, 178),
    'brown': (42, 42, 165),
    'dark_salmon': (122, 150, 233),
    'salmon': (114, 128, 250),
    'light_salmon': (122, 160, 255),
    'orange': (0, 165, 255),
    'dark_orange': (0, 140, 255),
    'coral': (80, 127, 255),
    'light_coral': (128, 128, 240),
    'tomato': (71, 99, 255),
    'orange_red': (0, 69, 255),
    'red': (0, 0, 255),
    'hot_pink': (180, 105, 255),
    'deep_pink': (147, 20, 255),
    'pink': (203, 192, 255),
    'light_pink': (193, 182, 255),
    'pale_violet_red': (147, 112, 219),
    'maroon': (96, 48, 176),
    'medium_violet_red': (133, 21, 199),
    'violet_red': (144, 32, 208),
    'violet': (238, 130, 238),
    'plum': (221, 160, 221),
    'orchid': (214, 112, 218),
    'medium_orchid': (211, 85, 186),
    'dark_orchid': (204, 50, 153),
    'dark_violet': (211, 0, 148),
    'blue_violet': (226, 43, 138),
    'purple': (240, 32, 160),
    'medium_purple': (219, 112, 147),
    'thistle': (216, 191, 216),
    'green': (0, 255, 0),
    'magenta': (255, 0, 255)
}


def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def printMatrixToFile(mat, mat_name, fname, fmt='{:15.9f}', mode='w', sep='\t'):
    fid = open(fname, mode)
    fid.write('{:s}:\n'.format(mat_name))
    for i in xrange(mat.shape[0]):
        for j in xrange(mat.shape[1]):
            fid.write(fmt.format(mat[i, j]) + sep)
        fid.write('\n')
    fid.write('\n\n')
    fid.close()


def printVectorFile(mat, mat_name, fname, fmt='{:15.9f}', mode='w', sep='\t'):
    fid = open(fname, mode)
    # print 'mat before: ', mat
    mat = mat.squeeze()
    # mat = mat.squeeze()
    # if len(mat.shape) > 1:
    # print 'here we are outside'
    # mat = mat[0, 0]
    #
    # print 'mat: ', mat
    # print 'mat.size: ', mat.size
    # print 'mat.shape: ', mat.shape
    fid.write('{:s}:\n'.format(mat_name))
    for i in xrange(mat.size):
        val = mat[i]
        # print 'type( val ): ', type( val )
        # if not isinstance(val, (int, long, float)) or type( val )=='numpy.float64':
        # print 'here we are'
        # val = mat[0, i]
        # print 'val: ', val
        fid.write(fmt.format(val) + sep)
    fid.write('\n')
    fid.write('\n\n')
    fid.close()


def printScalarToFile(scalar_val, scalar_name,
                      fname, fmt='{:15.9f}', mode='w'):
    fid = open(fname, mode)
    fid.write('{:s}:\t'.format(scalar_name))
    fid.write(fmt.format(scalar_val))
    fid.write('\n\n')
    fid.close()


def getTrackingObject(img, col=(0, 0, 255), title=None):
    annotated_img = img.copy()
    temp_img = img.copy()
    if title is None:
        title = 'Select the object to track'
    cv2.namedWindow(title)
    cv2.imshow(title, annotated_img)
    pts = []

    def drawLines(img, hover_pt=None):
        if len(pts) == 0:
            cv2.imshow(title, img)
            return
        for i in xrange(len(pts) - 1):
            cv2.line(img, pts[i], pts[i + 1], col, 1)
        if hover_pt is None:
            return
        cv2.line(img, pts[-1], hover_pt, col, 1)
        if len(pts) == 3:
            cv2.line(img, pts[0], hover_pt, col, 1)
        elif len(pts) == 4:
            return
        cv2.imshow(title, img)

    def mouseHandler(event, x, y, flags=None, param=None):
        if len(pts) >= 4:
            return
        if event == cv2.EVENT_LBUTTONDOWN:
            pts.append((x, y))
            temp_img = annotated_img.copy()
            drawLines(temp_img)
        elif event == cv2.EVENT_LBUTTONUP:
            pass
        elif event == cv2.EVENT_RBUTTONDOWN:
            if len(pts) > 0:
                print 'Removing last point'
                del (pts[-1])
            temp_img = annotated_img.copy()
            drawLines(temp_img)
        elif event == cv2.EVENT_RBUTTONUP:
            pass
        elif event == cv2.EVENT_MBUTTONDOWN:
            pass
        elif event == cv2.EVENT_MOUSEMOVE:
            # if len(pts) == 0:
            # return
            temp_img = annotated_img.copy()
            drawLines(temp_img, (x, y))

    cv2.setMouseCallback(title, mouseHandler, param=[annotated_img, temp_img, pts])
    while len(pts) < 4:
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.waitKey(250)
    cv2.destroyWindow(title)
    drawLines(annotated_img, pts[0])
    return pts, annotated_img


def getTrackingObject2(img, col=(0, 0, 255), title=None, line_thickness=1):
    annotated_img = img.copy()
    temp_img = img.copy()
    if title is None:
        title = 'Select the object to track'
    cv2.namedWindow(title)
    cv2.imshow(title, annotated_img)
    pts = []

    def drawLines(img, hover_pt=None):
        if len(pts) == 0:
            cv2.imshow(title, img)
            return
        for i in xrange(len(pts) - 1):
            cv2.line(img, pts[i], pts[i + 1], col, line_thickness)
        if hover_pt is None:
            return
        cv2.line(img, pts[-1], hover_pt, col, line_thickness)
        if len(pts) == 3:
            cv2.line(img, pts[0], hover_pt, col, line_thickness)
        elif len(pts) == 4:
            return
        cv2.imshow(title, img)

    def mouseHandler(event, x, y, flags=None, param=None):
        if len(pts) >= 4:
            return
        if event == cv2.EVENT_LBUTTONDOWN:
            pts.append((x, y))
            temp_img = annotated_img.copy()
            drawLines(temp_img)
        elif event == cv2.EVENT_LBUTTONUP:
            pass
        elif event == cv2.EVENT_RBUTTONDOWN:
            if len(pts) > 0:
                print 'Removing last point'
                del (pts[-1])
            temp_img = annotated_img.copy()
            drawLines(temp_img)
        elif event == cv2.EVENT_RBUTTONUP:
            pass
        elif event == cv2.EVENT_MBUTTONDOWN:
            pass
        elif event == cv2.EVENT_MOUSEMOVE:
            # if len(pts) == 0:
            # return
            temp_img = annotated_img.copy()
            drawLines(temp_img, (x, y))

    cv2.setMouseCallback(title, mouseHandler, param=[annotated_img, temp_img, pts])
    while len(pts) < 4:
        key = cv2.waitKey(1)
        if key == 27:
            sys.exit()
    cv2.waitKey(250)
    cv2.destroyWindow(title)
    drawLines(annotated_img, pts[0])
    return pts


def readTrackingData(filename, arch_fid=None):
    if arch_fid is not None:
        data_file = arch_fid.open(filename, 'r')
    else:
        if not os.path.isfile(filename):
            print "Tracking data file not found:\n ", filename
            return None
        data_file = open(filename, 'r')

    data_file.readline()
    lines = data_file.readlines()
    data_file.close()
    no_of_lines = len(lines)
    data_array = np.empty([no_of_lines, 8])
    line_id = 0
    for line in lines:
        # print(line)
        words = line.split()
        if len(words) != 9:
            msg = "Invalid formatting on line %d" % line_id + " in file %s" % filename + ":\n%s" % line
            raise SyntaxError(msg)
        words = words[1:]
        coordinates = []
        for word in words:
            coordinates.append(float(word))
        data_array[line_id, :] = coordinates
        # print words
        line_id += 1

    return data_array


# new version that supports reinit data as well as invalid tracker states
def readTrackingData2(tracker_path, n_frames, _arch_fid=None, _reinit_from_gt=0):
    print 'Reading tracking data from: {:s}...'.format(tracker_path)
    if _arch_fid is not None:
        tracking_data = _arch_fid.open(tracker_path, 'r').readlines()
    else:
        tracking_data = open(tracker_path, 'r').readlines()
    if len(tracking_data) < 2:
        print 'Tracking data file is invalid.'
        return None, None

    # remove the header
    del (tracking_data[0])
    n_lines = len(tracking_data)

    if not _reinit_from_gt and n_lines != n_frames:
        print "No. of frames in tracking result ({:d}) and the ground truth ({:d}) do not match".format(
            n_lines, n_frames)
        return None
    line_id = 1
    failure_count = 0
    invalid_tracker_state_found = False
    data_array = []
    while line_id < n_lines:
        tracking_data_line = tracking_data[line_id].strip().split()
        frame_fname = str(tracking_data_line[0])
        fname_len = len(frame_fname)
        frame_fname_1 = frame_fname[0:5]
        frame_fname_2 = frame_fname[- 4:]
        if frame_fname_1 != 'frame' or frame_fname_2 != '.jpg':
            print 'Invaid formatting on tracking data line {:d}: {:s}'.format(line_id + 1, tracking_data_line)
            print 'frame_fname: {:s} fname_len: {:d} frame_fname_1: {:s} frame_fname_2: {:s}'.format(
                frame_fname, fname_len, frame_fname_1, frame_fname_2)
            return None, None
        frame_id_str = frame_fname[5:-4]
        frame_num = int(frame_id_str)
        if len(tracking_data_line) != 9:
            if _reinit_from_gt and len(tracking_data_line) == 2 and tracking_data_line[1] == 'tracker_failed':
                print 'tracking failure detected in frame: {:d} at line {:d}'.format(frame_num, line_id + 1)
                failure_count += 1
                data_array.append('tracker_failed')
                line_id += 2
                continue
            elif len(tracking_data_line) == 2 and tracking_data_line[1] == 'invalid_tracker_state':
                if not invalid_tracker_state_found:
                    print 'invalid tracker state detected in frame: {:d} at line {:d}'.format(frame_num, line_id + 1)
                    invalid_tracker_state_found = True
                line_id += 1
                data_array.append('invalid_tracker_state')
                continue
            else:
                print 'Invalid formatting on line {:d}: {:s}'.format(line_id, tracking_data[line_id])
                return None, None
        data_array.append([float(tracking_data_line[1]), float(tracking_data_line[2]),
                           float(tracking_data_line[3]), float(tracking_data_line[4]),
                           float(tracking_data_line[5]), float(tracking_data_line[6]),
                           float(tracking_data_line[7]), float(tracking_data_line[8])])
    return data_array, failure_count


def readWarpData(filename):
    if not os.path.isfile(filename):
        print "Warp data file not found:\n ", filename
        sys.exit()

    data_file = open(filename, 'r')
    lines = data_file.readlines()
    lines = (line.rstrip() for line in lines)
    lines = list(line for line in lines if line)
    data_file.close()
    no_of_lines = len(lines)
    warps_array = np.zeros((no_of_lines, 9), dtype=np.float64)
    line_id = 0
    for line in lines:
        words = line.split()
        if len(words) != 9:
            msg = "Invalid formatting on line %d" % line_id + " in file %s" % filename + ":\n%s" % line
            raise SyntaxError(msg)
        curr_warp = []
        for word in words:
            curr_warp.append(float(word))
        warps_array[line_id, :] = curr_warp
        line_id += 1
    return warps_array


def getNormalizedUnitSquarePts(resx=100, resy=100, c=1.0):
    pts_arr = np.mat(np.zeros((2, resy * resx)))
    pt_id = 0
    for y in np.linspace(-c, c, resy):
        for x in np.linspace(-c, c, resx):
            pts_arr[0, pt_id] = x
            pts_arr[1, pt_id] = y
            pt_id += 1
    corners = np.mat([[-c, c, c, -c], [-c, -c, c, c]])
    return pts_arr, corners


def drawRegion(img, corners, color, thickness=1, annotate_corners=False,
               annotation_col=(0, 255, 0), annotation_font_size=1):
    for i in xrange(4):
        p1 = (int(corners[0, i]), int(corners[1, i]))
        p2 = (int(corners[0, (i + 1) % 4]), int(corners[1, (i + 1) % 4]))
        cv2.line(img, p1, p2, color, thickness, cv2.CV_AA)
        if annotate_corners:
            if annotation_col is None:
                annotation_col = color
            cv2.putText(img, '{:d}'.format(i + 1), p1, cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        annotation_font_size, annotation_col)


def getPixValsRGB(pts, img):
    try:
        n_channels = img.shape[2]
    except IndexError:
        n_channels = 1
    # print 'img: ', img
    n_pts = pts.shape[1]
    pix_vals = np.zeros((n_pts, n_channels), dtype=np.float64)
    for channel_id in xrange(n_channels):
        try:
            curr_channel = img[:, :, channel_id].astype(np.float64)
        except IndexError:
            curr_channel = img
        pix_vals[:, channel_id] = getPixVals(pts, curr_channel)
    return pix_vals


def getPixVals(pts, img):
    x = pts[0, :]
    y = pts[1, :]

    n_rows, n_cols = img.shape
    x[x < 0] = 0
    y[y < 0] = 0
    x[x > n_cols - 1] = n_cols - 1
    y[y > n_rows - 1] = n_rows - 1

    lx = np.floor(x).astype(np.uint16)
    ux = np.ceil(x).astype(np.uint16)
    ly = np.floor(y).astype(np.uint16)
    uy = np.ceil(y).astype(np.uint16)

    dx = x - lx
    dy = y - ly

    ll = np.multiply((1 - dx), (1 - dy))
    lu = np.multiply(dx, (1 - dy))
    ul = np.multiply((1 - dx), dy)
    uu = np.multiply(dx, dy)

    # n_rows, n_cols = img.shape
    # lx[lx < 0] = 0
    # lx[lx >= n_cols] = n_cols - 1
    # ux[ux < 0] = 0
    # ly[ly < 0] = 0
    # ly[ly >= n_rows] = n_rows - 1
    # uy[uy < 0] = 0
    # ux[ux >= n_cols] = n_cols - 1
    # uy[uy >= n_rows] = n_rows - 1

    return np.multiply(img[ly, lx], ll) + np.multiply(img[ly, ux], lu) + \
           np.multiply(img[uy, lx], ul) + np.multiply(img[uy, ux], uu)


def drawGrid(img, pts, res_x, res_y, color, thickness=1):
    # draw vertical lines
    for x_id in xrange(res_x):
        for y_id in xrange(res_y - 1):
            pt_id1 = y_id * res_x + x_id
            pt_id2 = (y_id + 1) * res_x + x_id
            p1 = (int(pts[0, pt_id1]), int(pts[1, pt_id1]))
            p2 = (int(pts[0, pt_id2]), int(pts[1, pt_id2]))
            cv2.line(img, p1, p2, color, thickness, cv2.CV_AA)

    # draw horizontal lines
    for y_id in xrange(res_y):
        for x_id in xrange(res_x - 1):
            pt_id1 = y_id * res_x + x_id
            pt_id2 = y_id * res_x + x_id + 1
            p1 = (int(pts[0, pt_id1]), int(pts[1, pt_id1]))
            p2 = (int(pts[0, pt_id2]), int(pts[1, pt_id2]))
            cv2.line(img, p1, p2, color, thickness)


def writeCorners(file_id, corners, frame_id=-1, write_header=0):
    if write_header:
        file_id.write('frame   ulx     uly     urx     ury     lrx     lry     llx     lly     \n')
    corner_str = ''
    for i in xrange(4):
        corner_str = corner_str + '{:5.2f}\t{:5.2f}\t'.format(corners[0, i], corners[1, i])
    if frame_id > 0:
        file_id.write('frame{:05d}.jpg\t'.format(frame_id))
    file_id.write(corner_str + '\n')


def writeCorners2(file_name, corners, frame_id=-1, write_header=0):
    if write_header:
        file_id = open(file_name, 'w')
        file_id.write('frame   ulx     uly     urx     ury     lrx     lry     llx     lly     \n')
    else:
        file_id = open(file_name, 'a')
    corner_str = ''
    for i in xrange(4):
        corner_str = corner_str + '{:5.2f}\t{:5.2f}\t'.format(corners[0, i], corners[1, i])
    if frame_id > 0:
        file_id.write('frame{:05d}.jpg\t'.format(frame_id))
    file_id.write(corner_str + '\n')
    file_id.close()


def getError(actual_corners, tracked_corners):
    curr_error = math.sqrt(np.sum(np.square(actual_corners - tracked_corners)) / 4)
    return curr_error

    # print 'inbuilt error: ', self.curr_error
    # self.curr_error=0
    # for i in xrange(actual_corners.shape[0]):
    # for j in xrange(actual_corners.shape[1]):
    # self.curr_error += math.pow(actual_corners[i, j] - tracked_corners[i, j], 2)
    # self.curr_error = math.sqrt(self.curr_error / 4)
    # print 'explicit error: ', self.curr_error


def getGroundTruthUpdates(filename):
    ground_truth = readTrackingData(filename)
    no_of_frames = ground_truth.shape[0]
    unit_square = np.array([[-.5, -.5], [.5, -.5], [.5, .5], [-.5, .5]]).T
    last_corners = unit_square
    current_corners = None
    update_array = None
    updates = []
    update_filename = 'updates.txt'
    if os.path.exists(update_filename):
        os.remove(update_filename)
    update_file = open(update_filename, 'a')
    for i in xrange(no_of_frames):
        if current_corners is not None:
            last_corners = current_corners.copy()
        current_corners = np.array([ground_truth[i - 1, 0:2].tolist(),
                                    ground_truth[i - 1, 2:4].tolist(),
                                    ground_truth[i - 1, 4:6].tolist(),
                                    ground_truth[i - 1, 6:8].tolist()]).T
        update = compute_homography(last_corners, current_corners)
        # apply_to_pts(update, unit_square)
        # update.tofile(update_file)


        update = update.reshape((1, -1))
        update = np.delete(update, [8])
        # print 'update:\n', update
        np.savetxt(update_file, update, fmt='%12.8f', delimiter='\t')
        if update_array is None:
            if i > 0:
                update_array = np.asarray(update)
        else:
            update_array = np.append(update_array, update, axis=0)
        updates.append(update)
        # update_file.write('\n')
    # print 'updates:\n', updates
    update_file.close()
    # print 'update_array:\n', update_array
    np.savetxt('update_array.txt', update_array, fmt='%12.8f', delimiter='\t')
    # plotPCA(update_array)
    plotSuccessiveEuclideanDistance(update_array)
    return updates


def plotPCA(data):
    # construct your numpy array of data
    result = PCA(np.array(data))
    x = []
    y = []
    z = []
    for item in result.Y:
        x.append(item[0])
        y.append(item[1])
        z.append(item[2])

    plt.close('all')  # close all latent plotting windows
    fig1 = plt.figure()  # Make a plotting figure
    ax = Axes3D(fig1)  # use the plotting figure to create a Axis3D object.
    pltData = [x, y, z]
    ax.scatter(pltData[0], pltData[1], pltData[2], 'ko')  # make a scatter plot of blue dots from the data
    # ax.plot_wireframe(pltData[0], pltData[1], pltData[2]) # make a scatter plot of blue dots from the data
    # make simple, bare axis lines through space:
    xAxisLine = ((min(pltData[0]), max(pltData[0])), (0, 0),
                 (0, 0))  # 2 points make the x-axis line at the data extrema along x-axis
    ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')  # make a red line for the x-axis.
    yAxisLine = ((0, 0), (min(pltData[1]), max(pltData[1])),
                 (0, 0))  # 2 points make the y-axis line at the data extrema along y-axis
    ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'g')  # make a green line for the y-axis.
    zAxisLine = ((0, 0), (0, 0),
                 (min(pltData[2]), max(pltData[2])))  # 2 points make the z-axis line at the data extrema along z-axis
    ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'b')  # make a blue line for the z-axis.

    # label the axes
    ax.set_xlabel("x-axis label")
    ax.set_ylabel("y-axis label")
    ax.set_zlabel("y-axis label")
    ax.set_title("The title of the plot")
    plt.show()  # show the plot


def plotSuccessiveEuclideanDistance(data):
    print 'data.shape=', data.shape
    no_of_items = data.shape[0]
    data_dim = data.shape[1]

    # data1 = data[1:no_of_items - 1, :]
    # data2 = data[2:no_of_items, :]
    # euc_dist = np.sqrt(np.square(data1 - data2))

    x = range(no_of_items - 1)
    y = np.empty((no_of_items - 1, 1))

    for i in xrange(no_of_items - 1):
        y[i] = math.sqrt(np.sum(np.square(data[i + 1, :] - data[i, :])) / data_dim)

    plt.close('all')
    plt.figure()
    plt.plot(x, y)
    plt.show()


def getTrackingError(ground_truth_path, result_path, dataset, tracker_id):
    ground_truth_filename = ground_truth_path + '/' + dataset + '.txt'
    ground_truth_data = readTrackingData(ground_truth_filename)
    result_filename = result_path + '/' + dataset + '_res_%s.txt' % tracker_id

    result_data = readTrackingData(result_filename)
    [no_of_frames, no_of_pts] = ground_truth_data.shape
    error = np.zeros([no_of_frames, 1])
    # print "no_of_frames=", no_of_frames
    # print "no_of_pts=", no_of_pts
    if result_data.shape[0] != no_of_frames or result_data.shape[1] != no_of_pts:
        # print "no_of_frames 2=", result_data.shape[0]
        # print "no_of_pts 2=", result_data.shape[1]
        raise SyntaxError("Mismatch between ground truth and tracking result")

    error_filename = result_path + '/' + dataset + '_res_%s_error.txt' % tracker_id
    error_file = open(error_filename, 'w')
    for i in xrange(no_of_frames):
        data1 = ground_truth_data[i, :]
        data2 = result_data[i, :]
        for j in xrange(no_of_pts):
            error[i] += math.pow(data1[j] - data2[j], 2)
        error[i] = math.sqrt(error[i] / 4)
        error_file.write("%f\n" % error[i])
    error_file.close()
    return error


def extractColumn(filepath, filename, column, header_size=2):
    # print 'filepath=', filepath
    # print 'filename=', filename
    data_file = open(filepath + '/' + filename + '.txt', 'r')
    # remove header
    # read headersf
    for i in xrange(header_size):
        data_file.readline()
    lines = data_file.readlines()
    column_array = []
    line_id = 0
    for line in lines:
        # print(line)
        words = line.split()
        if (len(words) != 4):
            msg = "Invalid formatting on line %d" % line_id + " in file %s" % filename + ":\n%s" % line
            raise SyntaxError(msg)
        current_val = float(words[column])
        column_array.append(current_val)
        line_id += 1
    data_file.close()
    # print 'column_array=', column_array
    return column_array


def getThresholdRate(val_array, threshold, cmp_type):
    no_of_frames = len(val_array)
    if no_of_frames < 1:
        raise SystemExit('Error array is empty')
    thresh_count = 0
    for val in val_array:
        if cmp_type == 'less':
            if val <= threshold:
                thresh_count += 1
        elif cmp_type == 'more':
            if val >= threshold:
                thresh_count += 1

    rate = float(thresh_count) / float(no_of_frames) * 100
    return rate


def getThresholdVariations(res_dir, filename, val_type, show_plot=False,
                           min_thresh=0, diff=1, max_thresh=100, max_rate=100, agg_filename=None):
    print 'Getting threshold variations for', val_type
    if val_type == 'error':
        cmp_type = 'less'
        column = 2
    elif val_type == 'fps':
        cmp_type = 'more'
        column = 0
    else:
        raise SystemExit('Invalid value type')
    val_array = extractColumn(res_dir, filename, column)
    rates = []
    thresholds = []
    threshold = min_thresh
    const_count = 0
    rate = getThresholdRate(val_array, threshold, cmp_type)
    rates.append(rate)
    thresholds.append(threshold)
    while True:
        threshold += diff
        last_rate = rate
        rate = getThresholdRate(val_array, threshold, cmp_type)
        rates.append(rate)
        thresholds.append(threshold)
        if rate == last_rate:
            const_count += 1
        else:
            const_count = 0
        # print 'rate=', rate
        # if rate>=max_rate or const_count>=max_const or threshold>=max_thresh:
        # break
        if threshold >= max_thresh:
            break
    outfile = val_type + '_' + filename + '_' + str(min_thresh) + '_' + str(diff) + '_' + str(max_rate)
    data_array = np.array([thresholds, rates])
    full_name = res_dir + '/' + outfile + '.txt'
    np.savetxt(full_name, data_array.T, delimiter='\t', fmt='%11.5f')
    if agg_filename is not None:
        agg_filename = val_type + '_' + agg_filename
        agg_file = open('Results/' + agg_filename + '.txt', 'a')
        agg_file.write(full_name + '\n')
        agg_file.close()
    combined_fig = plt.figure()
    plt.plot(thresholds, rates, 'r-')
    plt.xlabel(threshold)
    plt.ylabel('Rate')
    # plt.title(plot_fname)
    plot_dir = res_dir + '/plots'
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)
    combined_fig.savefig(plot_dir + '/' + outfile, ext='png', bbox_inches='tight')

    if show_plot:
        plt.show()

    return rates, outfile


def aggregateDataFromFiles(list_filename, plot_filename, header_size=0):
    print 'Aggregating data from ', list_filename, '...'
    line_styles = ['-', '--', '-.', ':', '+', '*', 'D', 'x', 's', 'p', 'o', 'v', '^']
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    # no_of_colors=32
    # colors=getRGBColors(no_of_colors)
    line_style_count = len(line_styles)
    color_count = len(colors)
    list_file = open('Results/' + list_filename + '.txt', 'r')
    header = list_file.readline()
    legend = header.split()
    filenames = list_file.readlines()
    list_file.close()
    # no_of_files=len(files)
    combined_fig = plt.figure()

    col_index = 0
    line_style_index = 0
    plot_lines = []
    for filename in filenames:
        filename = filename.rstrip()
        if not filename:
            continue
        # print 'filename=', filename
        data_file = open(filename, 'r')
        for i in xrange(header_size):
            data_file.readline()
        lines = data_file.readlines()
        data_file.close()
        os.remove(filename)
        # print 'data_str before =', data_str
        # data_str=np.asarray(data_str)
        # print 'data_str after =', data_str
        # if (len(data_str.shape) != 2):
        # print 'data_str.shape=', data_str.shape
        # raise SystemError('Error in aggregateDataFromFiles:\nInvalid syntax detected')
        thresholds = []
        rate_data = []
        for line in lines:
            words = line.split()
            threshold = float(words[0])
            rate = float(words[1])
            thresholds.append(threshold)
            rate_data.append(rate)
        # data_float=float(data_str)
        # thresholds=data_float[:, 0]
        # rate_data=data_float[:, 1]
        if col_index == color_count:
            col_index = 0
            line_style_index += 1
        if line_style_index == line_style_count:
            line_style_index = 0
        # plt.plot(thresholds, rate_data, color=colors[col_index], linestyle=line_styles[line_style_index])
        plt.plot(thresholds, rate_data, colors[col_index] + line_styles[line_style_index])
        col_index += 1
        # plot_lines.append(plot_line)
        # data_array=np.asarray([thresholds, rate_data])
        # combined_data.append()

    # plt.show()
    plt.xlabel('thresholds')
    plt.ylabel('rate')
    legend_dir = 'Results/legend'
    if not os.path.isdir(legend_dir):
        os.makedirs(legend_dir)
    # plt.title(plot_fname)
    fontP = ftm.FontProperties()
    fontP.set_size('small')
    combined_fig.savefig('Results/' + plot_filename, ext='png')
    plt.legend(legend, prop=fontP)
    combined_fig.savefig(legend_dir + '/' + plot_filename, ext='png')
    # plt.show()


def plotThresholdVariationsFromFile(filename, plot_fname):
    data_file = open('Results/' + filename, 'r')
    header = data_file.readline()
    header_words = header.split()
    lines = data_file.readlines()
    # print 'header_words=', header_words

    header_count = len(header_words)
    line_count = len(lines)

    data_array = np.empty((line_count, header_count))
    for i in xrange(line_count):
        # print(line)
        words = lines[i].split()
        if (len(words) != header_count):
            msg = "Invalid formatting on line %d" % i + " in file %s" % filename + ":\n%s" % lines[i]
            raise SyntaxError(msg)
        for j in xrange(header_count):
            data_array[i, j] = float(words[j])
    thresholds = data_array[:, 0]
    combined_fig = plt.figure(0)
    for i in xrange(1, header_count):
        rate_data = data_array[:, i]
        plt.plot(thresholds, rate_data)

    plt.xlabel(header_words[0])
    plt.ylabel('Success Rate')
    # plt.title(plot_fname)
    combined_fig.savefig('Results/' + plot_fname, ext='png', bbox_inches='tight')
    plt.legend(header_words[1:])
    combined_fig.savefig('Results/legend/' + plot_fname, ext='png', bbox_inches='tight')
    plt.show()


def getRGBColors(no_of_colors):
    channel_div = 0
    while no_of_colors > (channel_div ** 3):
        channel_div += 1
    colors = []
    if channel_div == 0:
        return colors
    base_factor = float(1.0 / float(channel_div))
    for i in xrange(channel_div):
        red = base_factor * i
        for j in xrange(channel_div):
            green = base_factor * j
            for k in xrange(channel_div):
                blue = base_factor * k
                col = (red, green, blue)
                colors.append(col)
    return colors


def readPerformanceSummary(filename, root_dir=None):
    # print 'filename=', filename
    if root_dir is None:
        root_dir = 'Results'
    data_file = open(root_dir + '/' + filename.rstrip() + '.txt', 'r')
    header = data_file.readline().split()
    success_rate_list = []
    avg_fps_list = []
    avg_drift_list = []
    parameters_list = []
    line_count = 0
    for line in data_file.readlines():
        line_count += 1
        words = line.split()
        success_rate = float(words[header.index('success_rate')])
        avg_fps = float(words[header.index('avg_fps')])
        avg_drift = float(words[header.index('avg_drift')])
        parameters = words[header.index('parameters')]

        success_rate_list.append(success_rate)
        avg_fps_list.append(avg_fps)
        avg_drift_list.append(avg_drift)
        parameters_list.append(parameters)
    data = {
        'parameters': parameters_list,
        'success_rate': success_rate_list,
        'avg_fps': avg_fps_list,
        'avg_drift': avg_drift_list
    }
    return header, data, line_count


def splitFiles(fname, keywords, root_dir=None, plot=False):
    if root_dir is None:
        root_dir = 'Results'
    list_file = open(root_dir + '/' + fname + '.txt')
    plot_fname = list_file.readline().rstrip()
    filenames = list_file.readlines()
    for keyword in keywords:
        new_list_filename = fname + '_' + keyword
        new_list_file = open(root_dir + '/' + new_list_filename + '.txt', 'w')
        new_list_file.write(plot_fname + '_' + keyword + '\n')
        for filename in filenames:
            filename = filename.rstrip()
            header, data, data_count = readPerformanceSummary(filename, root_dir)
            parameters = data['parameters']
            success_rate = data['success_rate']
            avg_fps = data['avg_fps']
            avg_drift = data['avg_drift']
            split_filename = filename + '_' + keyword
            split_file = open(root_dir + '/' + split_filename + '.txt', 'w')
            new_list_file.write(filename + '_' + keyword + '\n')
            for title in header:
                split_file.write(title + '\t')
            split_file.write('\n')
            for i in xrange(data_count):
                if keyword in parameters[i]:
                    split_file.write(parameters[i] + '\t')
                    split_file.write(str(success_rate[i]) + '\t')
                    split_file.write(str(avg_fps[i]) + '\t')
                    split_file.write(str(avg_drift[i]) + '\n')
            split_file.close()
        new_list_file.close()
        if plot:
            getPointPlot(root_dir=root_dir, file=new_list_filename, show_plot=True)


def getPointPlot(root_dir=None, filenames=None, plot_fname=None,
                 file=None, use_sep_fig=True, show_plot=False, legend=None, xticks=None,
                 title='', plot_drift=True):
    font = {'weight': 'bold',
            'size': 14}
    matplotlib.rc('font', **font)

    if root_dir is None:
        root_dir = 'Results'
    if show_plot:
        plt.close('all')
    if filenames is None:
        if file is None:
            return
        list_file = open(root_dir + '/' + file + '.txt')
        plot_fname = list_file.readline().rstrip()
        filenames = list_file.readlines()

    if title is None:
        title = plot_fname
    line_styles = ['-', '--', '-.', ':']
    markers = ['+', 'o', 'D', 'x', 's', 'p', '*', 'v', '^']
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

    fontP = ftm.FontProperties()
    fontP.set_size('small')

    if plot_drift:
        sub_plot_count = 3
    else:
        sub_plot_count = 2

    # ----------------------initializing success rate plot---------------------- #
    fig = plt.figure(0)
    fig.canvas.set_window_title('Success Rate')
    if not use_sep_fig:
        plt.subplot(sub_plot_count, 1, 1)
    plt.title(title + ' Success Rate')


    # ----------------------initializing fps plot---------------------- #
    # plt.legend(filenames)
    if use_sep_fig:
        fig = plt.figure(1)
        fig.canvas.set_window_title('Average FPS')
    else:
        plt.subplot(sub_plot_count, 1, 2)
    plt.title(title + ' Average FPS')

    # ----------------------initializing drift plot---------------------- #
    if plot_drift:
        # plt.legend(filenames)
        if use_sep_fig:
            fig = plt.figure(2)
            fig.canvas.set_window_title('Average Drift')
        else:
            plt.subplot(sub_plot_count, 1, 3)
        plt.title(title + ' Average Drift')
    # plt.legend(filenames)

    # annotate_text_list=None
    linestyle_id = 0
    marker_id = 0
    color_id = 0
    success_rate_y = range(0, 200, 5)
    avg_fps_y = range(0, 100, 5)
    print 'success_rate_y=', success_rate_y
    print 'avg_fps_y=', avg_fps_y

    for filename in filenames:
        print 'filename=', filename
        header, data, data_count = readPerformanceSummary(filename, root_dir=root_dir)
        # parameters=data['parameters']
        success_rate = data['success_rate']
        avg_fps = data['avg_fps']
        avg_drift = data['avg_drift']

        x = range(0, data_count)

        # ----------------------updating success rate plot---------------------- #
        if use_sep_fig:
            plt.figure(0, figsize=(1920 / 96, 1080 / 96), dpi=96)
        else:
            plt.subplot(sub_plot_count, 1, 1)
        if xticks is None:
            plt.xticks(x, map(str, x))
        else:
            plt.xticks(x, xticks)
        plt.yticks(success_rate_y)
        plt.plot(x, success_rate,
                 colors[color_id] + markers[marker_id] + line_styles[linestyle_id])

        # ----------------------updating fps plot---------------------- #
        if use_sep_fig:
            plt.figure(1)
        else:
            plt.subplot(sub_plot_count, 1, 2)
        if xticks is None:
            plt.xticks(x, map(str, x))
        else:
            plt.xticks(x, xticks)
        plt.yticks(avg_fps_y)
        plt.plot(x, avg_fps,
                 colors[color_id] + markers[marker_id] + line_styles[linestyle_id])

        # ----------------------updating drift plot---------------------- #
        if plot_drift:
            if use_sep_fig:
                plt.figure(2)
            else:
                plt.subplot(sub_plot_count, 1, 3)
            if xticks is None:
                plt.xticks(x, map(str, x))
            else:
                plt.xticks(x, xticks)
            plt.plot(x, avg_drift,
                     colors[color_id] + markers[marker_id] + line_styles[linestyle_id])

        color_id = (color_id + 1) % len(colors)
        marker_id = (marker_id + 1) % len(markers)
        linestyle_id = (linestyle_id + 1) % len(line_styles)
        # annotate_text_list=parameters
    # annotate_text=''
    # print 'annotate_text_list:\n', annotate_text_list
    # for i in xrange(len(annotate_text_list)):
    # annotate_text=annotate_text+str(i)+': '+annotate_text_list[i]+'\n'
    #
    # print 'annotate_text=\n', annotate_text

    # ----------------------saving success rate plot---------------------- #
    if use_sep_fig:
        plt.figure(0)
    else:
        plt.subplot(sub_plot_count, 1, 1)
    ax = plt.gca()
    # for tick in ax.xaxis.get_major_ticks():
    # tick.label.set_fontsize(12)
    # specify integer or one of preset strings, e.g.
    # tick.label.set_fontsize('x-small')
    # tick.label.set_rotation('vertical')
    if legend is None:
        plt.legend(filenames, prop=fontP)
    else:
        plt.legend(legend, prop=fontP)
    plt.grid(True)
    # plt.figtext(0.01,0.01, annotate_text, fontsize=9)
    if use_sep_fig and plot_fname is not None:
        plt.savefig(root_dir + '/' + plot_fname + '_success_rate', dpi=96, ext='png')

    # ----------------------saving fps plot---------------------- #
    if use_sep_fig:
        plt.figure(1)
    else:
        plt.subplot(sub_plot_count, 1, 2)

    if legend is None:
        plt.legend(filenames, prop=fontP)
    else:
        plt.legend(legend, prop=fontP)
    plt.grid(True)
    if use_sep_fig and plot_fname is not None:
        plt.savefig(root_dir + '/' + plot_fname + '_avg_fps', dpi=96, ext='png')

    # ----------------------saving drift plot---------------------- #
    if plot_drift:
        if use_sep_fig:
            plt.figure(2)
        else:
            plt.subplot(sub_plot_count, 1, 3)
        if legend is None:
            plt.legend(filenames, prop=fontP)
        else:
            plt.legend(legend, prop=fontP)
        plt.grid(True)
        if use_sep_fig and plot_fname is not None:
            plt.savefig(root_dir + '/' + plot_fname + '_avg_drft', dpi=96, ext='png')

    # ----------------------saving combined plot---------------------- #
    if not use_sep_fig and plot_fname is not None:
        plt.savefig(root_dir + '/' + plot_fname, dpi=96, ext='png')

    if show_plot:
        plt.show()


class InteractivePlot:
    def __init__(self, root_dir=None, filenames=None, plot_fname=None,
                 file=None, legend=None, title=None, xticks=None, y_tick_count=10):
        plt.close('all')

        font = {'weight': 'bold',
                'size': 14}
        matplotlib.rc('font', **font)

        if root_dir is None:
            root_dir = 'Results'

        if filenames is None:
            if file is None:
                return
            list_file = open(root_dir + '/' + file + '.txt')
            plot_fname = list_file.readline().rstrip()
            filenames = list_file.readlines()

        if legend is None:
            legend = filenames

        if title is None:
            title = plot_fname

        self.legend = legend
        self.title = title.replace('_', ' ').title()

        # plotting state variables
        self.plot_types = ['success_rate', 'avg_fps', 'avg_drift']
        self.plot_id = 0
        self.active_line = 0
        self.plot_all_lines = True
        self.exit_event = False
        self.no_of_lines = len(filenames)
        self.y_tick_count = y_tick_count
        self.show_lines = [1] * self.no_of_lines

        line_styles = ['-', '--', '-.', ':']
        markers = ['o', 'D', '+', 'x', 's', 'p', '*', 'v', '^']
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
        linestyle_id = 0
        marker_id = 0
        color_id = 0

        self.fontP = ftm.FontProperties()
        self.fontP.set_size('small')

        self.fig = plt.figure(0)
        # self.fig.canvas.set_window_title('Success Rate')
        cid = self.fig.canvas.mpl_connect('key_press_event', self.onKeyPress)
        self.ax = plt.axes()
        # plt.ylabel('Run')
        plt.grid(True)
        # plt.show()

        self.plot_lines = []
        self.plot_data = []
        self.line_patterns = []

        num_keys = [str(i) for i in range(0, 10)]
        ctrl_keys = ['ctrl+' + str(i) for i in range(0, 10)]
        alt_keys = ['alt+' + str(i) for i in range(0, 10)]
        ctrl_alt_keys = ['ctrl+alt+' + str(i) for i in range(0, 10)]
        # print 'ctrl_keys=', ctrl_keys
        self.ctrl_keys = dict(zip(num_keys + alt_keys + ctrl_keys + ctrl_alt_keys,
                                  range(0, 10) * 2 + range(10, 20) * 2))

        file_id = 0
        for filename in filenames:
            # print 'filename=', filename
            header, data, data_count = readPerformanceSummary(filename, root_dir=root_dir)
            self.legend[file_id] = str(file_id) + ': ' + self.legend[file_id].rstrip()
            # parameters=data['parameters']
            self.plot_data.append(data)

            # ----------------------initializing plot---------------------- #
            self.x_data = range(0, data_count)
            y_data = data[self.plot_types[self.plot_id]]
            # print 'y_data=', y_data
            line_pattern = colors[color_id] + markers[marker_id] + line_styles[linestyle_id]
            self.line_patterns.append(line_pattern)
            line, = self.ax.plot(self.x_data, y_data, line_pattern, label=self.legend[file_id])
            self.plot_lines.append(line)

            color_id += 1
            if color_id >= len(colors):
                color_id = 0
                linestyle_id = (linestyle_id + 1) % len(line_styles)
                marker_id = (marker_id + 1) % len(markers)
            file_id += 1

        if xticks is None:
            plt.xticks(self.x_data, map(str, self.x_data))
        else:
            plt.xticks(self.x_data, xticks)

        # self.ax.legend(self.legend, prop=self.fontP)
        self.ax.legend(prop=self.fontP)
        anim = animation.FuncAnimation(self.fig, self.animate, self.simData, init_func=self.initPlot)

        # fig_drift.canvas.draw()
        plt.show()

    def onKeyPress(self, event):
        print 'key pressed=', event.key
        if event.key == "escape" or event.key == "alt+escape":
            self.exit_event = True
            sys.exit()
        elif event.key == "down" or event.key == "alt+down":
            if self.plot_all_lines:
                self.plot_all_lines = False
                return
            self.active_line = (self.active_line + 1) % self.no_of_lines
        elif event.key == "up" or event.key == "alt+up":
            if self.plot_all_lines:
                self.plot_all_lines = False
                return
            self.active_line -= 1
            if self.active_line < 0:
                self.active_line = self.no_of_lines - 1
        elif event.key == "shift" or event.key == "alt+shift":
            self.plot_all_lines = not self.plot_all_lines
        elif event.key == "right" or event.key == "alt+right":
            self.plot_id = (self.plot_id + 1) % len(self.plot_types)
        elif event.key == "left" or event.key == "alt+left":
            self.plot_id -= 1
            if self.plot_id < 0:
                self.plot_id = len(self.plot_types) - 1
        elif event.key in self.ctrl_keys.keys():
            if not self.plot_all_lines:
                return
            key_id = self.ctrl_keys[event.key]
            if key_id < self.no_of_lines:
                self.show_lines[key_id] = 1 - self.show_lines[key_id]
                if not self.show_lines[key_id]:
                    print 'Removing line for', self.legend[key_id]
                else:
                    print 'Restoring line for', self.legend[key_id]
        elif event.key == "i" or event.key == "alt+i":
            self.show_lines = [1 - x for x in self.show_lines]
        elif event.key == "r" or event.key == "alt+r":
            self.show_lines = [1] * self.no_of_lines

    def simData(self):
        yield 1

    def initPlot(self):
        return self.plot_lines

    def animate(self, i):
        if self.exit_event:
            sys.exit()
        plot_title = self.plot_types[self.plot_id].replace('_', ' ').title()

        plot_empty = True
        max_y = 0
        if self.plot_all_lines:
            for i in xrange(self.no_of_lines):
                y_data = self.plot_data[i][self.plot_types[self.plot_id]]
                curr_y_max = max(y_data)
                if max_y < curr_y_max:
                    max_y = curr_y_max
                # print 'y_data=', y_data
                if self.show_lines[i]:
                    plot_empty = False
                    self.plot_lines[i].set_data(self.x_data, y_data)
                    self.plot_lines[i].set_label(self.legend[i])
                else:
                    self.plot_lines[i].set_data([], [])
                    self.plot_lines[i].set_label('_' + self.legend[i])
                    # self.ax.legend((lines, legend), prop=self.fontP)
                    # self.ax.get_legend().set_visible(True)
        else:
            plot_empty = False
            for i in xrange(self.no_of_lines):
                self.plot_lines[i].set_data([], [])
                self.plot_lines[i].set_label('_' + self.legend[i])
            y_data = self.plot_data[self.active_line][self.plot_types[self.plot_id]]
            # print 'y_data=', y_data
            self.plot_lines[self.active_line].set_data(self.x_data, y_data)
            self.plot_lines[self.active_line].set_label(self.legend[self.active_line])
            max_y = max(y_data)
            # plot_title = plot_title + '_' + self.legend[self.active_line]
            # self.ax.get_legend().set_visible(False)

        if plot_empty:
            self.ax.get_legend().set_visible(False)
        else:
            self.ax.legend(prop=self.fontP)
        plot_title = plot_title + ' for ' + self.title
        self.fig.canvas.set_window_title(plot_title)
        plt.title(plot_title)
        self.ax.set_ylim(0, max_y)
        y_diff = int(math.ceil(max_y / self.y_tick_count))
        y_ticks = range(0, y_diff * self.y_tick_count + 1, y_diff)
        # print 'max_y=', max_y
        # print 'y_diff=', y_diff
        # print 'y_ticks=', y_ticks
        plt.yticks(y_ticks, map(str, y_ticks))

        plt.draw()
        return self.plot_lines


def lineIntersection(line1, line2):
    r1 = line1[0]
    theta1 = line1[1]
    r2 = line2[0]
    theta2 = line2[1]

    if theta1 == theta2:
        raise StandardError('Lines are parallel')
    elif theta1 == 0:
        x = r1
        y = -x * (math.cos(theta2) / math.sin(theta2)) + (r2 / math.sin(theta2))
    elif theta2 == 0:
        x = r2
        y = -x * (math.cos(theta1) / math.sin(theta1)) + (r1 / math.sin(theta1))
    else:
        sin_theta1 = math.sin(theta1)
        cos_theta1 = math.cos(theta1)
        sin_theta2 = math.sin(theta2)
        cos_theta2 = math.cos(theta2)

        m1 = -cos_theta1 / sin_theta1
        c1 = r1 / sin_theta1
        m2 = -cos_theta2 / sin_theta2
        c2 = r2 / sin_theta2

        x = (c1 - c2) / (m2 - m1)
        y = m1 * x + c1
        # print 'r1: ', r1, 'theta1: ', theta1
        # print 'r2: ', r2, 'theta2: ', theta2
        # print 'sin_theta1: ', sin_theta1, 'cos_theta1: ', cos_theta1
        # print 'sin_theta2: ', sin_theta2, 'cos_theta2: ', cos_theta2
        # print 'm1: ', m1, 'c1: ', c1
        # print 'm2: ', m2, 'c2: ', c2
        # print 'x: ', x, 'y: ', y
        # print '\n'
    return x, y


def getIntersectionPoints(lines_arr):
    no_of_lines = len(lines_arr)
    if no_of_lines != 4:
        raise StandardError('Invalid number of lines provided: ' + str(no_of_lines))
    # line1 = lines_arr[0, :]
    # theta_diff = np.fabs(line1[1] - lines_arr[:, 1])

    pi = cv2.cv.CV_PI
    pi_2 = cv2.cv.CV_PI / 2.0

    min_theta_diff = np.inf
    min_i = 0
    min_j = 0
    for i in xrange(4):
        theta1 = lines_arr[i, 1]
        # if theta1 > pi_2 and lines_arr[i, 0] < 0:
        # theta1 = pi - theta1
        for j in xrange(i + 1, 4):
            theta2 = lines_arr[j, 1]
            # if theta2 > pi_2 and lines_arr[j, 0] < 0:
            # theta2 = pi - theta2
            theta_diff = math.fabs(theta1 - theta2)
            if theta_diff < min_theta_diff:
                min_theta_diff = theta_diff
                min_i = i
                min_j = j
    line1 = lines_arr[min_i, :]
    line2 = lines_arr[min_j, :]

    print 'before: lines_arr:\n', lines_arr
    print 'min_i: ', min_i
    print 'min_j: ', min_j
    print 'line1: ', line1
    print 'line2: ', line2

    pts = []
    for i in xrange(4):
        if i != min_i and i != min_j:
            print 'getting intersection between lines {:d} and {:d}'.format(min_i, i)
            pt = lineIntersection(line1, lines_arr[i, :])
            print 'intersection pt: ', pt
            pts.append(pt)
            print 'getting intersection between lines {:d} and {:d}'.format(min_j, i)
            pt = lineIntersection(line2, lines_arr[i, :])
            print 'intersection pt: ', pt
            pts.append(pt)
    pt_arr = np.array(pts)

    # print 'theta_diff: \n', theta_diff


    # sort params by theta_diff
    # lines_arr = lines_arr[theta_diff.argsort()]
    # print 'after: lines_arr:\n', lines_arr
    # pt1 = lineIntersection(lines_arr[0, :], lines_arr[2, :])
    # pt2 = lineIntersection(lines_arr[0, :], lines_arr[3, :])
    # pt3 = lineIntersection(lines_arr[1, :], lines_arr[2, :])
    # pt4 = lineIntersection(lines_arr[1, :], lines_arr[3, :])

    # pt_arr = np.array([pt1, pt2, pt3, pt4])
    # print 'pt_arr:\n', pt_arr
    pt_arr_sorted = pt_arr[pt_arr[:, 0].argsort()]
    # print 'pt_arr_sorted:\n', pt_arr_sorted

    if pt_arr_sorted[0, 1] < pt_arr_sorted[1, 1]:
        ulx, uly = pt_arr_sorted[0, :]
        urx, ury = pt_arr_sorted[1, :]
    else:
        ulx, uly = pt_arr_sorted[1, :]
        urx, ury = pt_arr_sorted[0, :]

    if pt_arr_sorted[2, 1] < pt_arr_sorted[3, 1]:
        llx, lly = pt_arr_sorted[2, :]
        lrx, lry = pt_arr_sorted[3, :]
    else:
        llx, lly = pt_arr_sorted[3, :]
        lrx, lry = pt_arr_sorted[2, :]

    return ulx, uly, urx, ury, lrx, lry, llx, lly


def refineCorners(corners, curr_img_gs):
    ulx, uly = corners[:, 0]
    urx, ury = corners[:, 1]
    lrx, lry = corners[:, 2]
    llx, lly = corners[:, 3]

    return corners


def readMetaioInitData(init_file):
    gt_corners = []

    init_fid = open(init_file, 'r')
    lines = init_fid.readlines()
    init_fid.close()

    curr_corners = [0] * 8
    gt_id = 0
    for line in lines:
        words = line.split()
        if words is None or len(words) <= 1:
            continue
        if isNumber(words[0]):
            curr_corners[gt_id] = float(words[0])
            curr_corners[gt_id + 1] = float(words[1])
            gt_id += 2
        elif gt_id > 0:
            gt_corners.append(copy.deepcopy(curr_corners))
            gt_id = 0

    gt_corners.append(copy.deepcopy(curr_corners))
    gt_corners_array = np.array(gt_corners, dtype=np.float64)
    # print 'gt_corners: ', gt_corners
    # print 'gt_corners_array: ', gt_corners_array
    return gt_corners_array


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def getLinearInterpolatedImages(init_img, final_img, count):
    interpolated_images = []
    for i in xrange(count):
        alpha = float(i + 1) / float(count + 1)
        curr_img = alpha * final_img + (1.0 - alpha) * init_img
        interpolated_images.append(np.copy(curr_img.astype(np.float64)))

    return interpolated_images


def readDistGridParams(filename='distanceGridParams.txt'):
    dicts_from_file = {}
    with open(filename, 'r') as param_file:
        for line in param_file:
            words = line.split()
            dicts_from_file[words[0]] = int(words[1])
    return dicts_from_file


def readGT(gt_path):
    gt_data = open(gt_path, 'r').readlines()
    if len(gt_data) < 2:
        print 'Tracking data file is invalid'
        return None, None
    del (gt_data[0])
    n_lines = len(gt_data)
    gt = []
    line_id = 0
    while line_id < n_lines:
        gt_line = gt_data[line_id].strip().split()
        gt_frame_fname = gt_line[0]
        gt_frame_num = int(gt_frame_fname[5:-4])
        gt_frame_fname_1 = gt_frame_fname[0:5]
        gt_frame_fname_2 = gt_frame_fname[- 4:]
        if len(
                gt_line) != 9 or gt_frame_fname_1 != 'frame' or gt_frame_fname_2 != '.jpg' or gt_frame_num != line_id + 1:
            print 'Invaid formatting on GT data line {:d}: {:s}'.format(line_id + 1, gt_line)
            print 'gt_frame_fname_1: {:s}'.format(gt_frame_fname_1)
            print 'gt_frame_fname_2: {:s}'.format(gt_frame_fname_2)
            print 'gt_frame_num: {:d}'.format(gt_frame_num)
            return None, None
        gt.append([float(gt_line[1]), float(gt_line[2]), float(gt_line[3]), float(gt_line[4]),
                   float(gt_line[5]), float(gt_line[6]), float(gt_line[7]), float(gt_line[8])])
        line_id += 1

    return n_lines, gt


def readReinitGT(gt_path, reinit_frame_id):
    gt_fid = open(gt_path, 'rb')
    try:
        n_gt_frames = struct.unpack('i', gt_fid.read(4))[0]
    except struct.error:
        gt_fid.close()
        raise StandardError("Reinit GT file is invalid")
    print 'Reading reinit gt for frame {:d}'.format(reinit_frame_id + 1)
    start_pos = reinit_frame_id * (2 * n_gt_frames - reinit_frame_id + 1) * 4 * 8 + 4
    gt_fid.seek(start_pos)
    reinit_gt = []
    for frame_id in xrange(reinit_frame_id, n_gt_frames):
        try:
            curr_gt = struct.unpack('dddddddd', gt_fid.read(64))
        except struct.error:
            gt_fid.close()
            raise StandardError("Reinit GT file is invalid")
        reinit_gt.append([
            curr_gt[0], curr_gt[4],
            curr_gt[1], curr_gt[5],
            curr_gt[2], curr_gt[6],
            curr_gt[3], curr_gt[7]
        ])
    gt_fid.close()
    return n_gt_frames, reinit_gt


def arrangeCorners(orig_corners):
    # print 'orig_corners:\n', orig_corners
    # print 'orig_corners.shape:\n', orig_corners.shape

    new_corners = np.zeros((2, 4), dtype=np.float64)
    sorted_x_id = np.argsort(orig_corners[0, :])

    # print 'new_corners.shape:\n', new_corners.shape
    # print 'sorted_x_id:\n', sorted_x_id

    if orig_corners[1, sorted_x_id[0]] < orig_corners[1, sorted_x_id[1]]:
        new_corners[:, 0] = orig_corners[:, sorted_x_id[0]]
        new_corners[:, 3] = orig_corners[:, sorted_x_id[1]]
    else:
        new_corners[:, 0] = orig_corners[:, sorted_x_id[1]]
        new_corners[:, 3] = orig_corners[:, sorted_x_id[0]]

    if orig_corners[1, sorted_x_id[2]] < orig_corners[1, sorted_x_id[3]]:
        new_corners[:, 1] = orig_corners[:, sorted_x_id[2]]
        new_corners[:, 2] = orig_corners[:, sorted_x_id[3]]
    else:
        new_corners[:, 1] = orig_corners[:, sorted_x_id[3]]
        new_corners[:, 2] = orig_corners[:, sorted_x_id[2]]
    return new_corners


def parseValue(old_val, new_val, arg_name=None):
    if type(old_val) is str:
        return new_val
    elif type(old_val) is int:
        return int(new_val)
    elif type(old_val) is float:
        return float(new_val)
    elif type(old_val) is tuple or type(old_val) is list:
        arg_list = new_val.split(',')
        if len(arg_list) != len(old_val):
            print 'arg_list: ', arg_list
            if arg_name is not None:
                raise SyntaxError('Invalid size for parameter {:s}: {:d}: '.format(
                    arg_name, len(arg_list)))
            else:
                raise SyntaxError('Invalid size for parameter: {:s}: '.format(len(arg_list)))
        for i in xrange(len(arg_list)):
            arg_list[i] = parseValue(old_val[i], arg_list[i])
        if type(old_val) is tuple:
            return tuple(arg_list)
        else:
            return arg_list


def parseArguments(args, params):
    print 'args: \n', args
    if (len(args) - 1) % 2 != 0:
        print 'args: \n', args
        raise SyntaxError('Command line arguments must be specified in pairs')
    arg_id = 1
    while arg_id < len(args):
        arg_name = args[arg_id]
        if not arg_name in params.keys():
            raise SyntaxError('Invalid command line argument: {:s}'.format(arg_name))
        params[arg_name] = parseValue(params[arg_name], args[arg_id + 1], arg_name)
        print 'Setting ', arg_name, ' to ', params[arg_name]
        arg_id += 2
    return params


def arrangeCornersWithIDs(orig_corners):
    # print 'orig_corners:\n', orig_corners
    # print 'orig_corners.shape:\n', orig_corners.shape

    new_corners = np.zeros((2, 4), dtype=np.float64)
    sorted_x_id = np.argsort(orig_corners[0, :])

    rearrangement_ids = np.array([0, 1, 2, 3], dtype=np.uint32)

    # print 'new_corners.shape:\n', new_corners.shape
    print 'sorted_x_id:\n', sorted_x_id

    if orig_corners[1, sorted_x_id[0]] < orig_corners[1, sorted_x_id[1]]:
        new_corners[:, 0] = orig_corners[:, sorted_x_id[0]]
        new_corners[:, 3] = orig_corners[:, sorted_x_id[1]]
        rearrangement_ids[0] = sorted_x_id[0]
        rearrangement_ids[3] = sorted_x_id[1]
    else:
        new_corners[:, 0] = orig_corners[:, sorted_x_id[1]]
        new_corners[:, 3] = orig_corners[:, sorted_x_id[0]]
        rearrangement_ids[0] = sorted_x_id[1]
        rearrangement_ids[3] = sorted_x_id[0]

    if orig_corners[1, sorted_x_id[2]] < orig_corners[1, sorted_x_id[3]]:
        new_corners[:, 1] = orig_corners[:, sorted_x_id[2]]
        new_corners[:, 2] = orig_corners[:, sorted_x_id[3]]
        rearrangement_ids[1] = sorted_x_id[2]
        rearrangement_ids[2] = sorted_x_id[3]
    else:
        new_corners[:, 1] = orig_corners[:, sorted_x_id[3]]
        new_corners[:, 2] = orig_corners[:, sorted_x_id[2]]
        rearrangement_ids[1] = sorted_x_id[3]
        rearrangement_ids[2] = sorted_x_id[2]
    return new_corners, rearrangement_ids


def getSyntheticSeqSuffix(syn_ssm, syn_ssm_sigma_id, syn_ilm='0',
                        syn_am_sigma_id=0, syn_add_noise=0,
                        syn_noise_mean=0, syn_noise_sigma=10):
    syn_out_suffix = 'warped_{:s}_s{:d}'.format(syn_ssm, syn_ssm_sigma_id)
    if syn_ilm != "0":
        syn_out_suffix = '{:s}_{:s}_s{:d}'.format(syn_out_suffix,
                                                  syn_ilm, syn_am_sigma_id)
    if syn_add_noise:
        syn_out_suffix = '{:s}_gauss_{:4.2f}_{:4.2f}'.format(syn_out_suffix,
                                                             syn_noise_mean, syn_noise_sigma)
    return syn_out_suffix


def getSyntheticSeqName(source_name, syn_ssm, syn_ssm_sigma_id, syn_ilm='0',
                        syn_am_sigma_id=0, syn_frame_id=0, syn_add_noise=0,
                        syn_noise_mean=0, syn_noise_sigma=10, syn_out_suffix=None):
    if syn_out_suffix is None:
        syn_out_suffix = getSyntheticSeqSuffix(syn_ssm, syn_ssm_sigma_id, syn_ilm,
                                               syn_am_sigma_id, syn_add_noise, syn_noise_mean, syn_noise_sigma)

    return '{:s}_{:d}_{:s}'.format(source_name, syn_frame_id, syn_out_suffix)


def getParamDict():
    tracker_types = {0: 'gt',
                     1: 'esm',
                     2: 'ic',
                     3: 'nnic',
                     4: 'pf',
                     5: 'pw',
                     6: 'ppw'
    }
    grid_types = {0: 'trans',
                  1: 'rs',
                  2: 'shear',
                  3: 'proj',
                  4: 'rtx',
                  5: 'rty',
                  6: 'stx',
                  7: 'sty',
                  8: 'trans2'
    }
    filter_types = {0: 'none',
                    1: 'gauss',
                    2: 'box',
                    3: 'norm_box',
                    4: 'bilateral',
                    5: 'median',
                    6: 'gabor',
                    7: 'sobel',
                    8: 'scharr',
                    9: 'LoG',
                    10: 'DoG',
                    11: 'laplacian',
                    12: 'canny'
    }
    inc_types = {0: 'fc',
                 1: 'ic',
                 2: 'fa',
                 3: 'ia'
    }
    appearance_models = {0: 'ssd',
                         1: 'scv',
                         2: 'ncc',
                         3: 'mi',
                         4: 'ccre',
                         5: 'hssd',
                         6: 'jht',
                         7: 'mi2',
                         8: 'ncc2',
                         9: 'scv2',
                         10: 'mi_old',
                         11: 'mssd',
                         12: 'bmssd',
                         13: 'bmi',
                         14: 'crv',
                         15: 'fkld',
                         16: 'ikld',
                         17: 'mkld',
                         18: 'chis',
                         19: 'ssim'
    }

    sequences_tmt = {
        0: 'nl_bookI_s3',
        1: 'nl_bookII_s3',
        2: 'nl_bookIII_s3',
        3: 'nl_cereal_s3',
        4: 'nl_juice_s3',
        5: 'nl_mugI_s3',
        6: 'nl_mugII_s3',
        7: 'nl_mugIII_s3',

        8: 'nl_bookI_s4',
        9: 'nl_bookII_s4',
        10: 'nl_bookIII_s4',
        11: 'nl_cereal_s4',
        12: 'nl_juice_s4',
        13: 'nl_mugI_s4',
        14: 'nl_mugII_s4',
        15: 'nl_mugIII_s4',

        16: 'nl_bus',
        17: 'nl_highlighting',
        18: 'nl_letter',
        19: 'nl_newspaper',

        20: 'nl_bookI_s1',
        21: 'nl_bookII_s1',
        22: 'nl_bookIII_s1',
        23: 'nl_cereal_s1',
        24: 'nl_juice_s1',
        25: 'nl_mugI_s1',
        26: 'nl_mugII_s1',
        27: 'nl_mugIII_s1',

        28: 'nl_bookI_s2',
        29: 'nl_bookII_s2',
        30: 'nl_bookIII_s2',
        31: 'nl_cereal_s2',
        32: 'nl_juice_s2',
        33: 'nl_mugI_s2',
        34: 'nl_mugII_s2',
        35: 'nl_mugIII_s2',

        36: 'nl_bookI_s5',
        37: 'nl_bookII_s5',
        38: 'nl_bookIII_s5',
        39: 'nl_cereal_s5',
        40: 'nl_juice_s5',
        41: 'nl_mugI_s5',
        42: 'nl_mugII_s5',
        43: 'nl_mugIII_s5',

        44: 'nl_bookI_si',
        45: 'nl_bookII_si',
        46: 'nl_cereal_si',
        47: 'nl_juice_si',
        48: 'nl_mugI_si',
        49: 'nl_mugIII_si',

        50: 'dl_bookI_s3',
        51: 'dl_bookII_s3',
        52: 'dl_bookIII_s3',
        53: 'dl_cereal_s3',
        54: 'dl_juice_s3',
        55: 'dl_mugI_s3',
        56: 'dl_mugII_s3',
        57: 'dl_mugIII_s3',

        58: 'dl_bookI_s4',
        59: 'dl_bookII_s4',
        60: 'dl_bookIII_s4',
        61: 'dl_cereal_s4',
        62: 'dl_juice_s4',
        63: 'dl_mugI_s4',
        64: 'dl_mugII_s4',
        65: 'dl_mugIII_s4',

        66: 'dl_bus',
        67: 'dl_highlighting',
        68: 'dl_letter',
        69: 'dl_newspaper',

        70: 'dl_bookI_s1',
        71: 'dl_bookII_s1',
        72: 'dl_bookIII_s1',
        73: 'dl_cereal_s1',
        74: 'dl_juice_s1',
        75: 'dl_mugI_s1',
        76: 'dl_mugII_s1',
        77: 'dl_mugIII_s1',

        78: 'dl_bookI_s2',
        79: 'dl_bookII_s2',
        80: 'dl_bookIII_s2',
        81: 'dl_cereal_s2',
        82: 'dl_juice_s2',
        83: 'dl_mugI_s2',
        84: 'dl_mugII_s2',
        85: 'dl_mugIII_s2',

        86: 'dl_bookI_s5',
        87: 'dl_bookII_s5',
        88: 'dl_bookIII_s5',
        89: 'dl_cereal_s5',
        90: 'dl_juice_s5',
        91: 'dl_mugI_s5',
        92: 'dl_mugIII_s5',

        93: 'dl_bookII_si',
        94: 'dl_cereal_si',
        95: 'dl_juice_si',
        96: 'dl_mugI_si',
        97: 'dl_mugIII_si',

        98: 'dl_mugII_si',
        99: 'dl_mugII_s5',
        100: 'nl_mugII_si',

        101: 'robot_bookI',
        102: 'robot_bookII',
        103: 'robot_bookIII',
        104: 'robot_cereal',
        105: 'robot_juice',
        106: 'robot_mugI',
        107: 'robot_mugII',
        108: 'robot_mugIII'
    }
    sequences_ucsb = {
        0: 'bricks_dynamic_lighting',
        1: 'bricks_motion1',
        2: 'bricks_motion2',
        3: 'bricks_motion3',
        4: 'bricks_motion4',
        5: 'bricks_motion5',
        6: 'bricks_motion6',
        7: 'bricks_motion7',
        8: 'bricks_motion8',
        9: 'bricks_motion9',
        10: 'bricks_panning',
        11: 'bricks_perspective',
        12: 'bricks_rotation',
        13: 'bricks_static_lighting',
        14: 'bricks_unconstrained',
        15: 'bricks_zoom',
        16: 'building_dynamic_lighting',
        17: 'building_motion1',
        18: 'building_motion2',
        19: 'building_motion3',
        20: 'building_motion4',
        21: 'building_motion5',
        22: 'building_motion6',
        23: 'building_motion7',
        24: 'building_motion8',
        25: 'building_motion9',
        26: 'building_panning',
        27: 'building_perspective',
        28: 'building_rotation',
        29: 'building_static_lighting',
        30: 'building_unconstrained',
        31: 'building_zoom',
        32: 'mission_dynamic_lighting',
        33: 'mission_motion1',
        34: 'mission_motion2',
        35: 'mission_motion3',
        36: 'mission_motion4',
        37: 'mission_motion5',
        38: 'mission_motion6',
        39: 'mission_motion7',
        40: 'mission_motion8',
        41: 'mission_motion9',
        42: 'mission_panning',
        43: 'mission_perspective',
        44: 'mission_rotation',
        45: 'mission_static_lighting',
        46: 'mission_unconstrained',
        47: 'mission_zoom',
        48: 'paris_dynamic_lighting',
        49: 'paris_motion1',
        50: 'paris_motion2',
        51: 'paris_motion3',
        52: 'paris_motion4',
        53: 'paris_motion5',
        54: 'paris_motion6',
        55: 'paris_motion7',
        56: 'paris_motion8',
        57: 'paris_motion9',
        58: 'paris_panning',
        59: 'paris_perspective',
        60: 'paris_rotation',
        61: 'paris_static_lighting',
        62: 'paris_unconstrained',
        63: 'paris_zoom',
        64: 'sunset_dynamic_lighting',
        65: 'sunset_motion1',
        66: 'sunset_motion2',
        67: 'sunset_motion3',
        68: 'sunset_motion4',
        69: 'sunset_motion5',
        70: 'sunset_motion6',
        71: 'sunset_motion7',
        72: 'sunset_motion8',
        73: 'sunset_motion9',
        74: 'sunset_panning',
        75: 'sunset_perspective',
        76: 'sunset_rotation',
        77: 'sunset_static_lighting',
        78: 'sunset_unconstrained',
        79: 'sunset_zoom',
        80: 'wood_dynamic_lighting',
        81: 'wood_motion1',
        82: 'wood_motion2',
        83: 'wood_motion3',
        84: 'wood_motion4',
        85: 'wood_motion5',
        86: 'wood_motion6',
        87: 'wood_motion7',
        88: 'wood_motion8',
        89: 'wood_motion9',
        90: 'wood_panning',
        91: 'wood_perspective',
        92: 'wood_rotation',
        93: 'wood_static_lighting',
        94: 'wood_unconstrained',
        95: 'wood_zoom'
    }
    sequences_lintrack = {
        0: 'mouse_pad',
        1: 'phone',
        2: 'towel',
    }
    sequences_lintrack_short = {
        0: 'mouse_pad_1',
        1: 'mouse_pad_2',
        2: 'mouse_pad_3',
        3: 'mouse_pad_4',
        4: 'mouse_pad_5',
        5: 'mouse_pad_6',
        6: 'mouse_pad_7',
        7: 'phone_1',
        8: 'phone_2',
        9: 'phone_3',
        10: 'towel_1',
        11: 'towel_2',
        12: 'towel_3',
        13: 'towel_4',
    }
    sequences_pami = {
        0: 'acronis',
        1: 'bass',
        2: 'bear',
        3: 'board_robot',
        4: 'board_robot_2',
        5: 'book1',
        6: 'book2',
        7: 'book3',
        8: 'book4',
        9: 'box',
        10: 'box_robot',
        11: 'cat_cylinder',
        12: 'cat_mask',
        13: 'cat_plane',
        14: 'compact_disc',
        15: 'cube',
        16: 'dft_atlas_moving',
        17: 'dft_atlas_still',
        18: 'dft_moving',
        19: 'dft_still',
        20: 'juice',
        21: 'lemming',
        22: 'mascot',
        23: 'omni_magazine',
        24: 'omni_obelix',
        25: 'sylvester',
        26: 'table_top',
        27: 'tea'
    }
    sequences_cmt = {
        0: 'board_robot',
        1: 'box_robot',
        2: 'cup_on_table',
        3: 'juice',
        4: 'lemming',
        5: 'liquor',
        6: 'sylvester',
        7: 'ball',
        8: 'car',
        9: 'car_2',
        10: 'carchase',
        11: 'dog1',
        12: 'gym',
        13: 'jumping',
        14: 'mountain_bike',
        15: 'person',
        16: 'person_crossing',
        17: 'person_partially_occluded',
        18: 'singer',
        19: 'track_running'
    }

    sequences_vivid = {
        0: 'redteam',
        1: 'egtest01',
        2: 'egtest02',
        3: 'egtest03',
        4: 'egtest04',
        5: 'egtest05',
        6: 'pktest01',
        7: 'pktest02',
        8: 'pktest03'
    }

    sequences_trakmark = {
        0: 'CV00_00',
        1: 'CV00_01',
        2: 'CV00_02',
        3: 'CV01_00',
        4: 'FS00_00',
        5: 'FS00_01',
        6: 'FS00_02',
        7: 'FS00_03',
        8: 'FS00_04',
        9: 'FS00_05',
        10: 'FS00_06',
        11: 'FS01_00',
        12: 'FS01_01',
        13: 'FS01_02',
        14: 'FS01_03',
        15: 'JR00_00',
        16: 'JR00_01',
        17: 'NC00_00',
        18: 'NC01_00',
        19: 'NH00_00',
        20: 'NH00_01'
    }

    sequences_vot = {
        0: 'woman',
        1: 'ball',
        2: 'basketball',
        3: 'bicycle',
        4: 'bolt',
        5: 'car',
        6: 'david',
        7: 'diving',
        8: 'drunk',
        9: 'fernando',
        10: 'fish1',
        11: 'fish2',
        12: 'gymnastics',
        13: 'hand1',
        14: 'hand2',
        15: 'jogging',
        16: 'motocross',
        17: 'polarbear',
        18: 'skating',
        19: 'sphere',
        20: 'sunshade',
        21: 'surfing',
        22: 'torus',
        23: 'trellis',
        24: 'tunnel'
    }

    sequences_vot16 = {
        0: 'bag',
        1: 'ball1',
        2: 'ball2',
        3: 'basketball',
        4: 'birds1',
        5: 'birds2',
        6: 'blanket',
        7: 'bmx',
        8: 'bolt1',
        9: 'bolt2',
        10: 'book',
        11: 'butterfly',
        12: 'car1',
        13: 'car2',
        14: 'crossing',
        15: 'dinosaur',
        16: 'fernando',
        17: 'fish1',
        18: 'fish2',
        19: 'fish3',
        20: 'fish4',
        21: 'girl',
        22: 'glove',
        23: 'godfather',
        24: 'graduate',
        25: 'gymnastics1',
        26: 'gymnastics2',
        27: 'gymnastics3',
        28: 'gymnastics4',
        29: 'hand',
        30: 'handball1',
        31: 'handball2',
        32: 'helicopter',
        33: 'iceskater1',
        34: 'iceskater2',
        35: 'leaves',
        36: 'marching',
        37: 'matrix',
        38: 'motocross1',
        39: 'motocross2',
        40: 'nature',
        41: 'octopus',
        42: 'pedestrian1',
        43: 'pedestrian2',
        44: 'rabbit',
        45: 'racing',
        46: 'road',
        47: 'shaking',
        48: 'sheep',
        49: 'singer1',
        50: 'singer2',
        51: 'singer3',
        52: 'soccer1',
        53: 'soccer2',
        54: 'soldier',
        55: 'sphere',
        56: 'tiger',
        57: 'traffic',
        58: 'tunnel',
        59: 'wiper'
    }

    sequences_vtb = {
        0: 'Basketball',
        1: 'Biker',
        2: 'Bird1',
        3: 'Bird2',
        4: 'BlurBody',
        5: 'BlurCar1',
        6: 'BlurCar2',
        7: 'BlurCar3',
        8: 'BlurCar4',
        9: 'BlurFace',
        10: 'BlurOwl',
        11: 'Board',
        12: 'Bolt',
        13: 'Bolt2',
        14: 'Box',
        15: 'Boy',
        16: 'Car1',
        17: 'Car2',
        18: 'Car4',
        19: 'Car24',
        20: 'CarDark',
        21: 'CarScale',
        22: 'ClifBar',
        23: 'Coke',
        24: 'Couple',
        25: 'Coupon',
        26: 'Crossing',
        27: 'Crowds',
        28: 'Dancer',
        29: 'Dancer2',
        30: 'David',
        31: 'David2',
        32: 'David3',
        33: 'Deer',
        34: 'Diving',
        35: 'Dog',
        36: 'Dog1',
        37: 'Doll',
        38: 'DragonBaby',
        39: 'Dudek',
        40: 'FaceOcc1',
        41: 'FaceOcc2',
        42: 'Fish',
        43: 'FleetFace',
        44: 'Football',
        45: 'Football1',
        46: 'Freeman1',
        47: 'Freeman3',
        48: 'Freeman4',
        49: 'Girl',
        50: 'Girl2',
        51: 'Gym',
        52: 'Human2',
        53: 'Human3',
        54: 'Human4',
        55: 'Human5',
        56: 'Human6',
        57: 'Human7',
        58: 'Human8',
        59: 'Human9',
        60: 'Ironman',
        61: 'Jogging',
        62: 'Jogging_2',
        63: 'Jump',
        64: 'Jumping',
        65: 'KiteSurf',
        66: 'Lemming',
        67: 'Liquor',
        68: 'Man',
        69: 'Matrix',
        70: 'Mhyang',
        71: 'MotorRolling',
        72: 'MountainBike',
        73: 'Panda',
        74: 'RedTeam',
        75: 'Rubik',
        76: 'Shaking',
        77: 'Singer1',
        78: 'Singer2',
        79: 'Skater',
        80: 'Skater2',
        81: 'Skating1',
        82: 'Skating2',
        83: 'Skating2_2',
        84: 'Skiing',
        85: 'Soccer',
        86: 'Subway',
        87: 'Surfer',
        88: 'Suv',
        89: 'Sylvester',
        90: 'Tiger1',
        91: 'Tiger2',
        92: 'Toy',
        93: 'Trans',
        94: 'Trellis',
        95: 'Twinnings',
        96: 'Vase',
        97: 'Walking',
        98: 'Walking2',
        99: 'Woman'
    }

    sequences_metaio = {
        0: 'bump_angle',
        1: 'bump_fast_close',
        2: 'bump_fast_far',
        3: 'bump_illumination',
        4: 'bump_range',
        5: 'grass_angle',
        6: 'grass_fast_close',
        7: 'grass_fast_far',
        8: 'grass_illumination',
        9: 'grass_range',
        10: 'isetta_angle',
        11: 'isetta_fast_close',
        12: 'isetta_fast_far',
        13: 'isetta_illumination',
        14: 'isetta_range',
        15: 'lucent_angle',
        16: 'lucent_fast_close',
        17: 'lucent_fast_far',
        18: 'lucent_illumination',
        19: 'lucent_range',
        20: 'macMini_angle',
        21: 'macMini_fast_close',
        22: 'macMini_fast_far',
        23: 'macMini_illumination',
        24: 'macMini_range',
        25: 'philadelphia_angle',
        26: 'philadelphia_fast_close',
        27: 'philadelphia_fast_far',
        28: 'philadelphia_illumination',
        29: 'philadelphia_range',
        30: 'stop_angle',
        31: 'stop_fast_close',
        32: 'stop_fast_far',
        33: 'stop_illumination',
        34: 'stop_range',
        35: 'wall_angle',
        36: 'wall_fast_close',
        37: 'wall_fast_far',
        38: 'wall_illumination',
        39: 'wall_range'
    }

    sequences_tmt_fine = {
        0: 'fish_lure_left',
        1: 'fish_lure_right',
        2: 'fish_lure_fast_left',
        3: 'fish_lure_fast_right',
        4: 'key_task_left',
        5: 'key_task_right',
        6: 'key_task_fast_left',
        7: 'key_task_fast_right',
        8: 'hexagon_task_left',
        9: 'hexagon_task_right',
        10: 'hexagon_task_fast_left',
        11: 'hexagon_task_fast_right'
    }

    sequences_tmt_fine_full = {
        0: 'fish_lure_left',
        1: 'fish_lure_right',
        2: 'fish_lure_fast_left',
        3: 'fish_lure_fast_right',
        4: 'key_task_left',
        5: 'key_task_right',
        6: 'key_task_fast_left',
        7: 'key_task_fast_right',
        8: 'hexagon_task_left',
        9: 'hexagon_task_right',
        10: 'hexagon_task_fast_left',
        11: 'hexagon_task_fast_right',
        12: 'fish_lure_cam1',
        13: 'fish_lure_cam2',
        14: 'fish_lure_fast_cam1',
        15: 'fish_lure_fast_cam2',
        16: 'key_task_cam1',
        17: 'key_task_cam2',
        18: 'key_task_fast_cam1',
        19: 'key_task_fast_cam2',
        20: 'hexagon_task_cam1',
        21: 'hexagon_task_cam2',
        22: 'hexagon_task_fast_cam1',
        23: 'hexagon_task_fast_cam2',
    }

    sequences_mosaic = {
        0: 'book_1',
        1: 'book_2',
        2: 'book_3',
        3: 'book_4',
        4: 'book_5',
        5: 'book_6',
        6: 'book_7',
        7: 'book_8',
        8: 'poster_1',
        9: 'poster_2',
        10: 'poster_3',
        11: 'poster_4',
        12: 'poster_5',
        13: 'poster_6',
        14: 'poster_7',
        15: 'poster_8',
        16: 'poster_9'
    }

    sequences_misc = {
        0: 'uav_sim',
        1: 'chess_board_1',
        2: 'chess_board_2',
        3: 'chess_board_3',
        4: 'chess_board_4'
    }
    sequences_synthetic = {
        0:	'bear',
        1:	'board_robot',
        2:	'book4',
        3:	'box',
        4:	'box_robot',
        5:	'building_dynamic_lighting',
        6:	'cat_cylinder',
        7:	'cube',
        8:	'dft_still',
        9:	'lemming',
        10:	'mission_dynamic_lighting',
        11:	'mouse_pad',
        12:	'nl_bookI_s3',
        13:	'nl_bus',
        14:	'nl_cereal_s3',
        15:	'nl_juice_s3',
        16:	'nl_letter',
        17:	'nl_mugI_s3',
        18:	'nl_newspaper',
        19:	'paris_dynamic_lighting',
        20:	'phone',
        21:	'sunset_dynamic_lighting',
        22:	'sylvester',
        23:	'towel',
        24:	'wood_dynamic_lighting'
    }

    sequences_live = {
        0: 'usb_cam',
        1: 'firewire_cam'
    }

    actors = {
        0: 'TMT',
        1: 'UCSB',
        2: 'LinTrack',
        3: 'PAMI',
        4: 'LinTrackShort',
        5: 'METAIO',
        6: 'CMT',
        7: 'VOT',
        8: 'VOT16',
        9: 'VTB',
        10: 'VIVID',
        11: 'TrakMark',
        12: 'TMT_FINE',
        13: 'Mosaic',
        14: 'Misc',
        15: 'Synthetic',
        16: 'Live'
    }
    challenges = {0: 'angle',
                  1: 'fast_close',
                  2: 'fast_far',
                  3: 'range',
                  4: 'illumination'
    }
    opt_types = {0: 'pre',
                 1: 'post',
                 2: 'ind'
    }
    mtf_sms = {0: 'esm',
               1: 'nesm',
               2: 'aesm',
               3: 'fclk',
               4: 'iclk',
               5: 'falk',
               6: 'ialk',
               7: 'nnic',
               8: 'casc',
               9: 'dsst',
               10: 'tld',
               11: 'kcf',
               12: 'pf'
    }
    mtf_ams = {0: 'ssd',
               1: 'ncc',
               2: 'scv',
               3: 'rscv',
               4: 'nssd',
               5: 'mi'
    }
    mtf_ssms = {0: '2',
                1: '3',
                2: '3s',
                3: '4',
                4: '6',
                5: '8',
                6: 'c8',
                7: 'l8'
    }
    opt_methods = {
        0: 'Newton-CG',
        1: 'CG',
        2: 'BFGS',
        3: 'Nelder-Mead',
        4: 'Powell',
        5: 'dogleg',
        6: 'trust-ncg',
        7: 'L-BFGS-B',
        8: 'TNC',
        9: 'COBYLA',
        10: 'SLSQP'
    }
    sequences = dict(zip([actors[i] for i in xrange(len(actors))],
                         [sequences_tmt,
                          sequences_ucsb,
                          sequences_lintrack,
                          sequences_pami,
                          sequences_lintrack_short,
                          sequences_metaio,
                          sequences_cmt,
                          sequences_vot,
                          sequences_vot16,
                          sequences_vtb,
                          sequences_vivid,
                          sequences_trakmark,
                          sequences_tmt_fine,
                          sequences_mosaic,
                          sequences_misc,
                          sequences_synthetic,
                          sequences_live]))

    params_dict = {'actors': actors,
                   'tracker_types': tracker_types,
                   'grid_types': grid_types,
                   'filter_types': filter_types,
                   'inc_types': inc_types,
                   'appearance_models': appearance_models,
                   'sequences': sequences,
                   'opt_types': opt_types,
                   'challenges': challenges,
                   'mtf_sms': mtf_sms,
                   'mtf_ams': mtf_ams,
                   'mtf_ssms': mtf_ssms,
                   'opt_methods': opt_methods,
    }
    return params_dict


def stackImages(img_list, stack_order=0):
    n_images = len(img_list)
    img_size = img_list[0].shape
    grid_size = int(np.ceil(np.sqrt(n_images)))
    # print 'img_size: ', img_size
    # print 'n_images: ', n_images
    # print 'grid_size: ', grid_size
    stacked_img = None
    list_ended = False
    inner_axis = 1 - stack_order
    for row_id in xrange(grid_size):
        start_id = grid_size * row_id
        curr_row = None
        for col_id in xrange(grid_size):
            img_id = start_id + col_id
            if img_id >= n_images:
                curr_img = np.zeros(img_size, dtype=np.uint8)
                list_ended = True
            else:
                curr_img = img_list[img_id]
                if img_id == n_images - 1:
                    list_ended = True
            if curr_row is None:
                curr_row = curr_img
            else:
                curr_row = np.concatenate((curr_row, curr_img), axis=inner_axis)
        if stacked_img is None:
            stacked_img = curr_row
        else:
            stacked_img = np.concatenate((stacked_img, curr_row), axis=stack_order)
        if list_ended:
            break
    return stacked_img



