"""                             DES and AES with GUI
authors: Alvarez Alejandro
         Tovar Brisa
version 1.0
march 2020
"""

from tkinter import *
from Crypto.Cipher import DES

images = ["herz.bmp", "flower.bmp"]

#PADDING
def pad(s):
    return s + b"\0" * (DES.block_size - len(s) % DES.block_size)



#------------Encrypt--------------------------
def encryptDES(file_in,key,cipher,fileDES):

        file_Ciphered=fileDES

        #open file and read bytes
        with open(file_in, 'rb') as fbytes:
                Header= fbytes.read(54)
                fbytes.seek(54, 0)
                Btext = fbytes.read()
        Btext = pad(Btext)
        #cipher and write
        cipheredBytes =cipher.encrypt(Btext)
        with open(file_Ciphered, 'wb') as fo:
                fo.write(Header)
                fo.seek(54, 0)
                fo.write(cipheredBytes)
        print("file has been encrypted as: "+file_Ciphered)
        return file_Ciphered

#------------Decrypt--------------------------

def decrypt(cipheredFile,key,cipher):

        file_decrypted = cipheredFile.split(".")[0]+"Decrypted.bmp"

        #open file and read bytes
        with open(cipheredFile, 'rb') as fbytes:
                Header= fbytes.read(54)
                fbytes.seek(54, 0)
                Btext = fbytes.read()
        #decrypt and write
        cipheredBytes = cipher.decrypt(Btext)
        with open(file_decrypted, 'wb') as fo:
                fo.write(Header)
                fo.seek(54, 0)
                fo.write(cipheredBytes)
        print("file has been decrypted as: " + file_decrypted)
        return file_decrypted


def start():
    encr = int(enDe.get())
    method = enMeth.get()
    mode = opMode.get()
    key = eKey.get().encode()
    indexImg = img.get()
    # if mode == 'ECB':
    #     vector = ''.encode()
    # else:
    vector = eIV.get().encode()

    #--------------------------ECB-----------------------------
    #create instance of ECB
    if mode == 'ECB':
        if method == 'DES':
            cipher = DES.new(key, DES.MODE_ECB)
            fileName = images[indexImg].split(".")[0]+"_ECB.bmp"
        # else:
        #     HERE AES
    #--------------------------CBC-----------------------------
    #create instance of CBC
    elif mode == 'CBC':
        if method == 'DES':
            cipher = DES.new(key, DES.MODE_CBC, vector)
            fileName = images[indexImg].split(".")[0]+"_CBC.bmp"
        # else:
        #     HERE AES
    #--------------------------CFB-----------------------------
    #create instance of CFB
    elif mode == 'CFB':
        if method == 'DES':
            cipher = DES.new(key, DES.MODE_CFB, vector)
            fileName = images[indexImg].split(".")[0]+"_CFB.bmp"
        # else:
        #     HERE AES
    #--------------------------OFB-----------------------------
    #create instance of OFB
    elif mode == 'OFB':
        if method == 'DES':
            cipher = DES.new(key, DES.MODE_OFB, vector)
            fileName = images[indexImg].split(".")[0]+"_OFB.bmp"
            #decrypt JUST for OFB
            if encr == 1:
                cipher = DES.new(key, DES.MODE_OFB, vector[:DES.block_size])
        # else:
        #     HERE AES

    #ENCRYPT or DECRYPT
    if encr == 0:
        #open file instance and send it to enctypt
        encryptedImage = encryptDES(images[indexImg],key,cipher,fileName)
    else:
        decryptedImage= decrypt(fileName,key,cipher)
#start---------------------------------------------------------------------

#create the GUI
root=Tk()
root.title("AES and DES")
opMode = StringVar()
enMeth = StringVar()
img = IntVar()
enDe = IntVar()

yRbModes = 100
yRbMethod = 225
yRbImg = 350
yKIV = 415
yEncDecr = 485
yStart = 540

#root.geometry("800x600")
frame = Frame(root,width="800", height="600" )
frame.pack(anchor="n")
frame.config(bg="gray65")

lb=Label(frame, text="Select operation mode", fg="black", font=(18), bg="white")
lb.place(x=315, y=50)

rECB = Radiobutton(frame)
rECB.config(text="ECB", variable = opMode, value = 'ECB')
rECB.place(x = 150, y = yRbModes)

rCBC = Radiobutton(frame)
rCBC.config(text="CBC", variable = opMode, value = 'CBC')
rCBC.place(x = 300, y = yRbModes)

rCFB = Radiobutton(frame)
rCFB.config(text="CFB", variable = opMode, value = 'CFB')
rCFB.place(x = 450, y = yRbModes)

rOFB = Radiobutton(frame)
rOFB.config(text="OFB", variable = opMode, value = 'OFB')
rOFB.place(x = 600, y = yRbModes)

lb=Label(frame, text="Select Method", fg="black", font=(18), bg="white")
lb.place(x=350, y=175)

rAES = Radiobutton(frame)
rAES.config(text="AES", variable = enMeth, value = 'AES')
rAES.place(x = 300, y = yRbMethod)

rDES = Radiobutton(frame)
rDES.config(text="DES", variable = enMeth, value = 'DES')
rDES.place(x = 450, y = yRbMethod)

lb=Label(frame, text="Select Image", fg="black", font=(18), bg="white")
lb.place(x=350, y=300)

rAES = Radiobutton(frame)
rAES.config(text="HERZ", variable = img, value = 0)
rAES.place(x = 300, y = yRbImg)

rDES = Radiobutton(frame)
rDES.config(text="FLOWER", variable = img, value = 1)
rDES.place(x = 450, y = yRbImg)

lKey = Label(frame)
lKey.config(text = "KEY", font=(18))
lKey.place(x = 215, y = yKIV)
eKey = Entry(frame)
eKey.config(width=10, font=(18))
eKey.place(x = 255, y = yKIV)

lIV = Label(frame)
lIV.config(text = "IV", font=(18))
lIV.place(x = 455, y = yKIV)
eIV = Entry(frame)
eIV.config(width=10, font=(18))
eIV.place(x = 480, y = yKIV)

rEnc = Radiobutton(frame)
rEnc.config(text="Ecnrypt", variable = enDe, value = 0)
rEnc.place(x = 300, y = yEncDecr)

rDES = Radiobutton(frame)
rDES.config(text="Decrypt", variable = enDe, value = 1)
rDES.place(x = 450, y = yEncDecr)

encBtn=Button(frame)
encBtn.config(text="ENTER", bg="green", fg="white", width=10,command = start)
encBtn.place(x=350, y=yStart)



root.mainloop()
