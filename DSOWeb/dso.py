import os
from pathlib import Path


def save_file_calib(f, name, user, phone, calib):

    if calib:
        os.system("mkdir " + 'save/' + user)
        print("Utilisateur : " + name)
        with open('save/' + user + '/calib_' + name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        print("Copie Finie : " + name)

        pwd = os.getcwd()

        os.chdir(pwd + "/save")

        os.system("PWD")

        print("Start search : " + name)

        os.system("mkdir " + user + '/calib_dir' + name)

        os.system("./run.sh video " + user + '/calib_' + name + " " + user + ' calib_dir' + name + " resize 640x480 search")

        print("Finish search : " + name)

        calib_file = open("save/camera.txt", "r")

        calib_phone = Path("phone_calib/" + phone)
        if calib_phone.exists():
            return "calibexist"
        else:
            with open('phone_calib/' + phone, 'wb+') as destination:
                for chunk in calib_file.chunks():
                    destination.write(chunk)

            return "calibcreated"

    else:
        os.system("mkdir " + 'save/' + user)
        print("Utilisateur : " + name)
        with open('save/' + user + '/' + name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        calib_phone = Path("phone_calib/" + phone)
        if calib_phone.exists():
            #dso
            pass
        else:
            return "caliberror"
