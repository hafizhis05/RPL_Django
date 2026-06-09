from django.shortcuts import render, redirect, get_object_or_404
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'mahasiswa/index.html')


@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})


@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    error = ''
    nim = ''
    nama = ''
    programstudi = ''
    angkatan = ''

    if request.method == 'POST':
        nim = request.POST.get('nim', '').strip()
        nama = request.POST.get('nama', '').strip()
        programstudi = request.POST.get('programstudi', '').strip()
        angkatan = request.POST.get('angkatan', '').strip()

        if not nim or not nama or not programstudi or not angkatan:
            error = 'Semua field wajib diisi.'
        else:
            Mahasiswa.objects.create(nim=nim, nama=nama, programstudi=programstudi, angkatan=angkatan)
            return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/tambah.html', {
        'error': error,
        'nim': nim,
        'nama': nama,
        'programstudi': programstudi,
        'angkatan': angkatan,
    })


@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    error = ''

    if request.method == 'POST':
        nim = request.POST.get('nim', '').strip()
        nama = request.POST.get('nama', '').strip()
        programstudi = request.POST.get('programstudi', '').strip()
        angkatan = request.POST.get('angkatan', '').strip()

        if not nim or not nama or not programstudi or not angkatan:
            error = 'Semua field wajib diisi.'
        else:
            mhs.nim = nim
            mhs.nama = nama
            mhs.programstudi = programstudi
            mhs.angkatan = angkatan
            mhs.save()
            return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/edit.html', {
        'mhs': mhs,
        'error': error,
    })


@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    mhs.delete()
    return redirect('daftar_mahasiswa')

