import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep

global kisi_say
global kisi
global kisi_path
global foto_path

kisi_listesi = []
kisi_say = []



class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


def klasor_olustur(kisi_path):
    if not os.path.exists("Katalog"):
        os.system("mkdir Katalog")
        os.system("mkdir Katalog/Unknown")
        os.system("mkdir Katalog/Ortak")
        os.system("mkdir Katalog/Manzara")
    
    print(bcolors.RED + bcolors.GREEN,end='')
    print("------------------------")
    print("Klasörler oluşturuluyor!")
    print("------------------------")
    print(bcolors.RED + bcolors.BOLD)
    for dirpath, dnames, fnames in os.walk("./"+kisi_path):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".JPG"):
                kisi_listesi.append(f.split(".")[0])
                kisi_say.append(0)
                if not os.path.exists("Katalog/"+f.split(".")[0]):
                    print("==> Klasör",f.split(".")[0],"oluşturuluyor!")
                    sleep(1)
                    os.system("mkdir Katalog/" + f.split(".")[0])
                else:
                    print("==> Klasör",f.split(".")[0],"zaten mevcut!")
                    sleep(1)

    print(bcolors.RED + bcolors.GREEN)
    print("-----------------------------------------------")
    print("Klasörler oluşturuldu! - Dosyalar Kopyalanıyor!")
    print("-----------------------------------------------")
    print(bcolors.ENDC)

def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}
    try:
        for dirpath, dnames, fnames in os.walk("./"+kisi_path):
            for f in fnames:
                if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".JPG"):
                    face = fr.load_image_file(kisi_path+r'/' + f)
                    encoding = fr.face_encodings(face)[0]
                    encoded[f.split(".")[0]] = encoding

        return encoded
    except(IndexError):
        print(IndexError)
        pass
def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file(kisi_path + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]

    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)

    # Display the resulting image
   
    return face_names

def gez_ve_gonder(foto_path):
    global manzara
    global ortak_say
    global unknown
    global durum
    durum = 0
    unknown = 0
    ortak_say = 0
    manzara = 0
    for dirpath, dnames, fnames in os.walk("./"+foto_path):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".JPG"):
                
                kisi = classify_face(foto_path+r'/'+f)

                if len(kisi)>1 and kisi.count("Unknown") == len(kisi):
                    durum+=1
                    os.system("cp "+foto_path+"//"+f+" "+"Katalog//Unknown//")
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("==> "+f+" Dosyası ",end='') 
                    print(bcolors.ENDC,end='') 
                    print("Katalog/Unknown ",end='')
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("konumuna kopyalandı - ["+str((durum))+"/"+str(ytoplam)+"]")
                    unknown+=1

                
                elif len(kisi) > 1:
                    durum+=1
                    os.system("cp "+foto_path+"//"+f+" "+"Katalog//Ortak//")
                    ortak_say+=1
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("==> "+f+" Dosyası ",end='') 
                    print(bcolors.ENDC,end='') 
                    print("Katalog/Ortak ",end='')
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("konumuna kopyalandı - ["+str((durum))+"/"+str(ytoplam)+"]")
                    

                elif len(kisi)==0:
                    durum+=1
                    os.system("cp "+foto_path+"//"+f+" "+"Katalog//Manzara//")
                    manzara+=1
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("==> "+f+" Dosyası ",end='')
                    print(bcolors.ENDC,end='') 
                    print("Katalog/Manzara ",end='')
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("konumuna kopyalandı - ["+str((durum))+"/"+str(ytoplam)+"]")
                
                
                elif len(kisi)==1 and kisi[0]=="Unknown":
                    durum+=1
                    os.system("cp "+foto_path+"//"+f+" "+"Katalog//Unknown//")
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("==> "+f+" Dosyası ",end='') 
                    print(bcolors.ENDC,end='') 
                    print("Katalog/Unknown ",end='')
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("konumuna kopyalandı - ["+str((durum))+"/"+str(ytoplam)+"]")
                    unknown+=1

                else:
                    durum+=1
                    os.system("cp "+foto_path+"//"+f+" "+"Katalog//"+kisi[0]+"//")
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print("==> "+f+" Dosyası ",end='') 
                    print(bcolors.ENDC,end='') 
                    print("Katalog/"+kisi[0],end='')
                    print(bcolors.RED + bcolors.BOLD,end='')
                    print(" konumuna kopyalandı - ["+str((durum))+"/"+str(ytoplam)+"]")
                    indis = kisi_listesi.index(kisi[0])
                    kisi_say[indis] += 1
                    

def yuzdelik():
    global ytoplam
    ytoplam=0
    for dirpath, dnames, fnames in os.walk("./"+foto_path):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".JPG"):
                ytoplam+=1


def boslari_topla():

    for i in range(len(kisi_listesi)):
        if kisi_say[i] == 0:
            os.system("rmdir Katalog/"+kisi_listesi[i])

def logo():
    os.system("clear")
    print(bcolors.BLUE)
    print("  ___   __ _           _               ___ ____ ")
    print(" / _ \ / _| |__   __ _| |__   __ _ _ _|_ _/ ___|")
    print("| | | | |_| '_ \ / _` | '_ \ / _` | '__| | |    ")
    print("| |_| |  _| |_) | (_| | | | | (_| | |  | | |___ ")
    print(" \___/|_| |_.__/ \__,_|_| |_|\__,_|_| |___\____|")
    print("   v1.0 - Ofbahar | https://github.com/ofbahar")
    print(bcolors.ENDC)

def rapor():
    sleep(2)
    toplam=0
    print(bcolors.RED + bcolors.GREEN)
    print("--------------------------")
    print("Rapor\n")
    print("==> Kişiler : ")
    for i in range(len(kisi_say)):
        print(str(i)+") "+kisi_listesi[i]+" - "+str(kisi_say[i])+" Fotoğraf")
        toplam+=kisi_say[i]
    
    print("\n==> Manzara - "+str(manzara)+" Fotoğraf")
    print("==> Ortak - "+str(ortak_say)+" Fotoğraf")
    print("==> Bilinmeyen - "+str(unknown)+" Fotoğraf")
    print("\nToplam : ",manzara+ortak_say+unknown+toplam)
    print("--------------------------")
    print(bcolors.ENDC)


def cikis():
    print(bcolors.RED + bcolors.GREEN)
    print("----------------------------------")
    print("İslem Bitti! - ",end='')
    print(bcolors.RED + bcolors.BOLD,end='')
    print("Ofbahar",end='')
    print(bcolors.RED + bcolors.GREEN,end='')
    print(" - Güle Güle")
    print("----------------------------------")
    print(bcolors.ENDC)

logo()
print(bcolors.GREEN + bcolors.BOLD)
kisi_path = input("Kişiler klasörünün yolunu giriniz : ")
foto_path = input("Fotoğraf klasörünün yolunu giriniz : ")
print(bcolors.ENDC)
klasor_olustur(kisi_path)
yuzdelik()
try:
    gez_ve_gonder(foto_path)
except KeyboardInterrupt:
    print(bcolors.BLUE+"\nProgramdan Çıkılıyor!\nCtrl+C Algılandı..."+bcolors.ENDC)
rapor()
boslari_topla()
cikis()
                                        



