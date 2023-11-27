from django.db import models
from django.urls import reverse
from uuid import uuid4


class DataInput(models.Model):
    input_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    usia = models.CharField(max_length=255)

    JENIS_MAKANAN = [
        ("sehat", "Sehat"),
        ("cepatsaji", "Cepat Saji"),
    ]
    jenis_makanan = models.EmailField(max_length=254, choices=JENIS_MAKANAN)

    ALERGI_MAKANAN = [
        ("tidak", "Tidak"),
        ("iya", "Iya"),
    ]
    alergi_makanan = models.CharField(max_length=255, choices=ALERGI_MAKANAN)

    MELEWATKAN_SARAPAN = [
        ("iya", "Iya"),
        ("tidak", "Tidak"),
    ]
    melewatkan_sarapan = models.CharField(max_length=255, choices=MELEWATKAN_SARAPAN)

    makan_sehari = models.CharField(max_length=255)

    MAKAN_TERATUR = [
        ("iya", "Iya"),
        ("tidak", "Tidak"),
    ]
    makan_teratur = models.CharField(max_length=255, choices=MAKAN_TERATUR)

    TINGKAT_PENTING_PILIH_MAKANAN = [
        ("sangatpenting", "Sangat Penting"),
        ("penting", "Penting"),
        ("kurangpenting", "Kurang Penting"),
        ("tidakpenting", "Tidak Penting"),
    ]
    tingkat_penting_pilih_makanan = models.CharField(
        max_length=255, choices=TINGKAT_PENTING_PILIH_MAKANAN
    )

    olahraga_seminggu = models.CharField(max_length=255)

    class Meta:
        verbose_name = "DataInput"
        verbose_name_plural = "DataInputs"

    def __str__(self):
        return self.jenis_makanan

    def get_absolute_url(self):
        return reverse("DataInput_detail", kwargs={"pk": self.pk})
