import cv2
import glob


images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    resized_img = cv2.resize(img, (1000, 1000))
    cv2.imshow("img", resized_img)
    cv2.imwrite("Resized_" + image, resized_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

