import os
from pathlib import Path


def save_file_calib(f, name, user, phone, calib):
    files = ["calib", "camera_calibration.cpp", "default.xml", "run.sh", "images.sh", "createpoints.sh", "dso_dataset"]

    if calib:
        if not os.path.isdir('save/' + user):
            os.system("mkdir " + 'save/' + user)
            for x in files:
                os.system("cp " + 'save/' + x +' save/' + user + "/" + x)

            print("Dossier User créé")


        print("Utilisateur : " + name)
        with open('save/' + user + '/calib_' + name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        print("Copie Finie : " + name)

        pwd = os.getcwd()

        os.chdir(pwd + "/save/" + user)

        os.system("PWD")

        print("Start search : " + name)

        os.system("mkdir " + 'calib_dir' + name)

        os.system("./run.sh video " + 'calib_' + name + ' calib_dir' + name + " resize 640x480 search")

        print("Finish search : " + name)

        os.chdir(pwd)

        calib_phone = Path("phone_calib/" + phone)
        if calib_phone.exists():
            return "calibexist"
        else:
            os.system("cp save/" + user +"/camera.txt phone_calib/" + phone)

            return "calibcreated"

    else:
        calib_phone = Path("phone_calib/" + phone)

        ff = open("phone_calib/" + phone, "r")
        ff.readline()
        w,h = list(map(int, ff.readline().split()))

        print(w,h)

        if calib_phone.exists():
            if not os.path.isdir('save/' + user):
                os.system("mkdir " + 'save/' + user)
                for x in files:
                    os.system("cp " + 'save/' + x + ' save/' + user + "/" + x)

                print("Dossier User créé")

            print("Utilisateur : " + name)


            with open('save/' + user + '/' + name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            print("Copie Finie : " + name)

            pwd = os.getcwd()

            os.chdir(pwd + "/save/" + user)

            os.system("PWD")

            print("Start images : " + name)

            os.system("./images.sh " + name + " " + str(w) + "x" + str(h))

            print("Finish images : " + name)

            print("Start PointCloud : " + name)

            os.system("./createpoints.sh images_" + name + " " + phone)

            print("Finish PointCloud : " + name)

            os.chdir(pwd)

            return "model3dcreated"

        else:

            return "calibdontexist"




