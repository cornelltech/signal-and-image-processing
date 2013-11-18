import cv2
import maxflow

# returns a 0/1 segmentation of a width*height image
# Unary costs are specified by unary0[i,j], unary1[i,j], the costs
# for pixel i being 0 or 1 respectively.
# smoothCost is the cost for a pair of neighboring pixels being different
def segmentImage(width, height, unary0, unary1, smoothCost):
    g = maxflow.Graph[float](width*height, width*height)
    nodeIds = g.add_grid_nodes((width, height))
    for i in xrange(width):
        for j in xrange(height):
            g.add_tedge(nodeIds[i,j], unary0[i,j], unary1[i,j])
    g.add_grid_edges(nodeIds, smoothCost)
    g.maxflow()
    return g.get_grid_segments(nodeIds).astype('uint8')


if __name__ == '__main__':
# load the images
    images = [cv2.imread('angiogram-' + str(i) + '.pgm', 0) for i in xrange(1,8)]

    for im in images:
# displays image, and waits for user to press key to continue
        cv2.imshow('imshow', im)
        cv2.waitKey(0)

# Set up a particularly dumb unary cost (is 1 if first image is nonzero)
    unary0 = (images[0] == 0).astype(int)
    unary1 = (images[0] > 0).astype(int)
    width = images[0].shape[0]
    height = images[0].shape[1]
    smoothCost = 2
    out = segmentImage(width, height, unary0, unary1, smoothCost)
    cv2.imshow('imshow', out*255)
    cv2.waitKey(0)
    cv2.imwrite('segmentation.pgm', out*255)
