
import cv2
import numpy as np

ball_coords = [np.array([3, 16],dtype=float ), np.array([225, 357],dtype=float )]
key = ' '
speed = [ np.array([4, -4]), np.array([5, -5])]

backgroud_image = cv2.imread('background.jpg')
height, width, channels = backgroud_image.shape

color = [(100, 0, 100), (200, 222, 45)]  # BGR
wall_coords_TL = np.array([200, 100])
wall_coords_BR = np.array([300, 400])
wall_color = (100, 100, 0)

wall_coords_TL_r = np.array([900, 100])
wall_coords_BR_r = np.array([1000, 400])
wall_color_r = (111, 233, 100)
score1 = 0
score2 = 0
boom="yes"
#def dist_vec=np.linalg.norm(ball_coords[0]-ball_coords[1])
dist_vec=np.linalg.norm(ball_coords[0]-ball_coords[1])
score_pos = np.array([width/2, 50])
score_pos = np.array([width/2, 50])

def is_in_rect(p, TL, BR):
    if (p[1] >= TL[1] and p[1] <= BR[1]):

        if (p[0] >= TL[0] and p[0] <= BR[0]):
            return True
        return False

radious = 25

while key != ord('q'):
    bkg_copy = backgroud_image.copy()

    for i in range(len(ball_coords)):
        #ball_coords[i][0] += speed[i][0]
        #ball_coords[i][1] += speed[i][1]
        ball_coords[i] += speed[i]
        c_right = np.array([ball_coords[i][0] + radious, ball_coords[i][1]])
        c_left = np.array([ball_coords[i][0] - radious, ball_coords[i][1]])
        c_top = np.array([ball_coords[i][0], ball_coords[i][1] + radious])
        c_bottom = np.array([ball_coords[i][0], ball_coords[i][1] - radious])
        if is_in_rect(c_right, wall_coords_TL, wall_coords_BR):
            speed[i][0] = -speed[i][0]
        dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])
        if dist_vec <= 2*radious:
            boom="yes"
        else:
            boom="no"

        if is_in_rect(c_left, wall_coords_TL, wall_coords_BR):
            speed[i][0] = -speed[i][0]
            #dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])
        if is_in_rect(c_top, wall_coords_TL, wall_coords_BR):
            speed[i][1] = -speed[i][1]
            #dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])
        if is_in_rect(c_bottom, wall_coords_TL, wall_coords_BR):
            speed[i][1] = -speed[i][1]
            #dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])


        if is_in_rect(c_right, wall_coords_TL_r, wall_coords_BR_r):
            speed[i][0] = -speed[i][0]
            #dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])

        if is_in_rect(c_left, wall_coords_TL_r, wall_coords_BR_r):
            speed[i][0] = -speed[i][0]
            #dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])

        if is_in_rect(c_top, wall_coords_TL_r, wall_coords_BR_r):
            speed[i][1] = -speed[i][1]
            #dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])

        if is_in_rect(c_bottom, wall_coords_TL_r, wall_coords_BR_r):
            speed[i][1] = -speed[i][1]
            #dist_vec = np.linalg.norm(ball_coords[0] - ball_coords[1])

        cv2.circle(bkg_copy, ball_coords[i].astype(int), 25, color[i], -1)
        cv2.rectangle(bkg_copy, wall_coords_TL, wall_coords_BR, wall_color, -1)
        cv2.rectangle(bkg_copy, wall_coords_TL_r, wall_coords_BR_r, wall_color_r, -1)
        cv2.putText(bkg_copy, str(score1), (300, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (111, 233, 100), 3, cv2.LINE_AA)
        cv2.putText(bkg_copy, str(score2), (1000, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (100, 100, 0), 3, cv2.LINE_AA)
        cv2.putText(bkg_copy, str(dist_vec), (400, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (100, 100, 0), 3, cv2.LINE_AA)

        cv2.putText(bkg_copy, str(boom), (550, 90), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (100, 100, 0), 3, cv2.LINE_AA)






        if key == ord('a'):
            if wall_coords_TL[0] > 10:
                wall_coords_TL[0] = wall_coords_TL[0] - 10
                wall_coords_BR[0] = wall_coords_BR[0] - 10
        elif key == ord('d'):
            if wall_coords_BR[0] < width - 10:
                wall_coords_TL[0] = wall_coords_TL[0] + 10
                wall_coords_BR[0] = wall_coords_BR[0] + 10
        if key == ord('w'):
            if wall_coords_TL[1] > 10:
                wall_coords_TL[1] = wall_coords_TL[1] - 10
                wall_coords_BR[1] = wall_coords_BR[1] - 10
        elif key == ord('s'):
            if wall_coords_BR[1] < height - 10:
                wall_coords_TL[1] = wall_coords_TL[1] + 10
                wall_coords_BR[1] = wall_coords_BR[1] + 10

        if key == ord('4'):
            if wall_coords_TL_r[0] > 10:
                wall_coords_TL_r[0] = wall_coords_TL_r[0] - 10
                wall_coords_BR_r[0] = wall_coords_BR_r[0] - 10
        elif key == ord('6'):
            if wall_coords_BR_r[0] < width - 10:
                wall_coords_TL_r[0] = wall_coords_TL_r[0] + 10
                wall_coords_BR_r[0] = wall_coords_BR_r[0] + 10
        if key == ord('8'):
            if wall_coords_TL_r[1] > 10:
                wall_coords_TL_r[1] = wall_coords_TL_r[1] - 10
                wall_coords_BR_r[1] = wall_coords_BR_r[1] - 10
        elif key == ord('2'):
            if wall_coords_BR_r[1] < height - 10:
                wall_coords_TL_r[1] = wall_coords_TL_r[1] + 10
                wall_coords_BR_r[1] = wall_coords_BR_r[1] + 10

        if (ball_coords[i][0] >= width and speed[i][0] > 0):
            speed[i][0] = -speed[i][0]
            score1 = score1 + 1
        if (ball_coords[i][0] <= 0 and speed[i][0] < 0):
            speed[i][0] = -speed[i][0]
            score2 = score2 + 1


        if (ball_coords[i][1] >= height and speed[i][1] > 0):
            speed[i][1] = -speed[i][1]


        if (ball_coords[i][1] <= 0 and speed[i][1] < 0):
            speed[i][1] = -speed[i][1]


        if key == ord('U'):
            speed[i]=speed[i]*1.1
        if key == ord('L'):
            speed[i] = speed[i] * 0.9
        if key == ord('I'):
                speed[i] = -speed[i]

    cv2.imshow('ball game', bkg_copy)
    key = cv2.waitKey(10)
    #print(f"Pressed key: {key}")

# your turn
# 1. move up and down (y coordinate goes from 0 to height and back)
# 2. move in both x and y directions, speed = np.array([x_speed, y_speed]) , and "bump" into the "walls":
#       when reaching x boundery, x_speed flips, and same for y.
#       start from speed = (10,-10)
# 3. have a list of balls that move. (list of balls and list of speeds and list of colors)
# 4. Add collisions between balls (if distance is less than 2*raduis)
#
# 5. Allow moving the wall TL and BR with the "arrow keys" 'a'=left, 'd'=right, 's'=down, 'w'=up.
#   Do not allow to move the wall out of the screen!
#
# 6. Add another wall, with a different color, that moves with keys '8'=up,'2'=down,'4'=left,'6'=right
#    (use the numbers on the numpad on the right of the keyboard!)
#    Make the ball collide with this new wall as well.
#
#
# 7. Here is how the game works:
#   Player 1 uses the WASD keys to move her wall.
#   Player 2 uses the 8462 keys to move her wall.
#   Every player "protects" his side of the board.
#   Each time the ball hits the LEFT border of the screen, player #2 (8462) gets a point
#   Each time the ball hits the RIGHT border of the screen, player #1 (WASD) gets a point
#   Show the points on the screen using cv2.putText


