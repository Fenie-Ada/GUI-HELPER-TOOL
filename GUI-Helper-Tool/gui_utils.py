import cv2

class EdgeFinder:
    def __init__(self, image, filter_size=1, threshold1=0, threshold2=0):
        self.image = image
        self._filtersize = filter_size   # three settings the user is allowed to change later
        self._threshold1 = threshold1
        self._threshold2 = threshold2    # The _ is just a convention saying “these are internal values — please don’t touch them directly”

        def onchangeThreshold1(pos):
            self._threshold1 = pos
            self._update_pictures()

        def onchangeThreshold2(pos):
            self._threshold2 = pos
            self._update_pictures()

        def onchangeFilterSize(pos):
            self._filtersize = pos
            self._filtersize += (self._filtersize + 1) % 2    # ensures size is odd no.; (4 + 1) % 2 = 0  →  5 % 2 = 1  →  4 += 1 = 5
            self._update_pictures()

        cv2.namedWindow('edges')    # creates an empty window on the screen called “edges”. The edge image will be shown here later.

        cv2.createTrackbar('threshold1', 'edges', self._threshold1, 255, onchangeThreshold1)     # puts a slider inside the "edges window
        cv2.createTrackbar('threshold2', 'edges', self._threshold2, 255, onchangeThreshold2)     # ('name', 'window', currentvalue, limit, call when slider is moved)
        cv2.createTrackbar('filtersize', 'edges', self._filtersize, 20, onchangeFilterSize)

        self._update_pictures()         # Immediately show the image with the starting settings

        print ("Adjust the parameters as desired. Hit any key to close.")

        cv2.waitKey(0)

        cv2.destroyWindow('edges')
        cv2.destroyWindow('smoothed')

    def threshold1(self):
        return self._threshold1

    def threshold2(self):
        return self._threshold2

    def filterSize(self):
        return self._filtersize

    def edgeImage(self):
        return self._edge_img

    def smoothedImage(self):                 # the actual blurry photo inside the program
        return self._smoothed_img

    def _update_pictures(self):
        self._smoothed_img = cv2.GaussianBlur(self.image, (self._filtersize, self._filtersize), sigmaX=0, sigmaY=0)
        self._edge_img = cv2.Canny(self._smoothed_img, self._threshold1, self._threshold2)
        cv2.imshow('smoothed', self._smoothed_img)
        cv2.imshow('edges', self._edge_img)