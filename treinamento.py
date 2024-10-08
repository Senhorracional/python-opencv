import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagemComId():
    caminhos =  [os.path.join('fotos', f) for f in os.listdir('fotos')]
    print(caminhos)

getImagemComId() 