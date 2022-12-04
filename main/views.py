from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import pdf_reader
from pymongo import MongoClient
# Create your views here.

def filters(text):
    data = {}
    text = text.split('\n')
    for i in text:
        if ":" in i:
            i = i.split(":")
            data[i[0].strip(" ")] = i[1]
    return data


def index(request):
    if request.method == "POST":
        if request.FILES['file'] != '':
            file = request.FILES['file']
            print(file)
            fs = FileSystemStorage()
            fs.save('uploads/'+file.name, file)
            text = pdf_reader.pdfTotext('uploads/',file.name)
            data = filters(text)
            cluster = MongoClient("localhost:27017")
            db = cluster['static_data']
            collection = db['resume']
            collection.insert_one(data)
            return render(request, "index.html", data)
        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")
