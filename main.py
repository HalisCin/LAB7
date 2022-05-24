import cv2

path=r'C:\Users\halis\Desktop\Klarnet calan batman.jpg'
img=cv2.imread(path)
cv2.imshow('image',img)


(B,G,R)=cv2.split(img)
cv2.imshow("Model blue image",B)
cv2.imshow("Model red image",R)
cv2.imshow("Model green image",G)


print(img.shape)
for i in range(0,1024):
    for a in range(0,768):
        if R[i,a] > 100:
            R[i,a] = 10

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

cv2.waitKey(0)




