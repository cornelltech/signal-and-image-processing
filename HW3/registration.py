import cv2

# translates im2 by (x, y) and overlays the result over im1
def overlay(im1, im2, x, y):
    result = im1.copy()
    lbx = 0
    ubx = im1.shape[0] - x
    if x < 0:
        lbx = -x
        ubx = im1.shape[0]
    lby = 0
    uby = im1.shape[1] - y
    if y < 0:
        lby = -y
        uby = im1.shape[1]
    result[lbx+x:ubx+x,lby+y:uby+y] = 0.5*im1[lbx+x:ubx+x,lby+y:uby+y] \
        + 0.5*im2[lbx:ubx,lby:uby]
    return result

if __name__ == '__main__':
# read image pair, as grayscale (argument 0 to imread)
    im1 = cv2.imread('reg-1-1.jpg', 0)
    im2 = cv2.imread('reg-1-2.jpg', 0)

# Compute edge map
    e1 = cv2.Canny(im1, 100, 200)
    e2 = cv2.Canny(im2, 100, 200)

    cv2.imshow('imshow', e1)
    cv2.waitKey(0)
    cv2.imshow('imshow', e2)
    cv2.waitKey(0)

    color1 = cv2.imread('reg-1-1.jpg')
    color2 = cv2.imread('reg-1-2.jpg')
    out = overlay(color1, color2, 0, 0)
    cv2.imshow('imshow', out)
    cv2.waitKey(0)
    cv2.imwrite('reg-1.jpg', out)
