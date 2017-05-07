import os
from pathlib import Path

import exifread

import subprocess

from fractions import Fraction


import zipfile


def save_file(f, name, user):

    print("Utilisateur : " + name)

    with open('save/' + user + '/' + name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    print("Copie Finie : " + name)

    pwd = os.getcwd()

    print(pwd)


    with zipfile.ZipFile('save/' + user + '/' + name, "r") as zip_ref:
        zip_ref.extractall('save/' + user + '/' + name + "_dir")


    first = os.listdir('save/' + user + '/' + name + "_dir")[0]

    f = open('save/' + user + '/' + name + "_dir/" + first, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)

    print(tags['EXIF FocalLength'],tags['Image Model'])

    print(str(tags['Image Model']) + ";" + str(float(sum(Fraction(s) for s in str(tags['EXIF FocalLength']).split()))))

    with open("sensor_width_camera_database.txt", "a") as myfile:
        myfile.write("\n" + str(tags['Image Model']) + ";" + str(float(sum(Fraction(s) for s in str(tags['EXIF FocalLength']).split())))
)


    print("#Lancement")
    os.system("python ../openMVGMVS.py save/" + user + '/' + name + "_dir save/" + user + "/" + name + "_res")


    os.system("zip save/" + user + "/"+ name + "_final.zip"
              + " save/" + user + "/" + name + "_res/mvs/scene_dense_mesh_refine_texture.mtl"
              + " save/" + user + "/" + name + "_res/mvs/scene_dense_mesh_refine_texture.obj"
              + " save/" + user + "/" + name + "_res/mvs/scene_dense_mesh_refine_texture_material_0_map_Kd.jpg"
              )

    return "save/" + user + "/"+ name + "_final.zip"

