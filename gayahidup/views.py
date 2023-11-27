from django.shortcuts import render
import pandas as pd

# import pickle
import joblib

# Create your views here.
# rfmodel = pickle.load(open("randomforest.pkl", "rb"))
rfmodel = joblib.load("./gayahidup/randomforest.pkl")
# with open("randomforest.pkl", "rb") as model:
#     rfmodel = pickle.load(model)


# Ubah data kategorikal menjadi numerik
def categoric(value):
    # Ubah yg termasuk data input saja
    sarapan_map = {"Iya": 0, "Tidak": 1}

    if "Melewatkan Sarapan" in value:
        return sarapan_map.get(value["Melewatkan Sarapan"], None)
    else:
        return None


def index(request):
    if request.method == "POST":
        # Ambil semua data dari form
        nama = request.POST.get("name")
        usia = request.POST.get("usia")
        jeniskelamin = request.POST.get("jeniskelamin")
        jumlahmakan = request.POST.get("jumlahmakan")
        sarapan = request.POST.get("sarapan")
        olahraga = request.POST.get("olahraga")

        # Pilih data input yang telah diubah jadi numerik
        input_data = {
            "Melewatkan Sarapan": categoric({"Melewatkan Sarapan": sarapan}),
            "Jumlah Makan Sehari": jumlahmakan,
            "Total Olahraga Seminggu": olahraga,
        }

        input_data_frame = pd.DataFrame([input_data])

        klasifikasi = rfmodel.predict(input_data_frame)

        # if klasifikasi == 0:
        #     jenis_klasifikasi = "Kingpling"
        # elif klasifikasi == 1:
        #     jenis_klasifikasi = "Hampir Kingpling"
        # elif klasifikasi == 2:
        #     jenis_klasifikasi = "Tidak Kingpling"
        # else:
        #     jenis_klasifikasi = "Bebas Kingpling"

        return render(
            request,
            "gayahidup/result.html",
            {
                "hasil_klasifikasi": klasifikasi,
                #  "jenis_klasifikasi": jenis_klasifikasi
            }
            # hasil_klasifikasi="{}".format(klasifikasi),
            # jenis_klasifikasi="{}".format(jenis_klasifikasi),
        )
    return render(request, "gayahidup/index.html")
