import cv2
src=cv2.imread("image_resizer/ac_unity.jpg",cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)

scale_percent=50
new_width = int(src.shape[1]*scale_percent/100)
new_height = int(src.shape[0]*scale_percent/100)

dsize = (new_width,new_height)

output = cv2.resize(src,(dsize))

cv2.imwrite('image_resizer/newImage.png',output)

#shows the output result image(uncomment it if you want to show image)
# destination=cv2.imread("image_resizer/newImage.png",cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",destination)

cv2.waitKey(0)
