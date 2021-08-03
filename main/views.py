from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render


def pdf_view(response, location):
    with open(location, 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed



# Create your views here.

def index_page(response):
    return render(response, "main/index.html", 
    {
        "title": "index"
        }
        )

def note_page(response, id):
    if response.method == "POST":
        title = response.POST.get("title")
        content = response.POST.get("content")
        updated_note = notes(id=id,title=title,content=content)
        updated_note.save()

    return render(response, "main/note.html", 
        {
            "title": "notes",
            "all_notes": notes.objects.all().values,
            "note": notes.objects.get(id=id),
            "form": new_note_form(),
            }
            )

def calender_page(response):
    return render(response, "main/calender.html", 
    {
        "title": "calender"
        }
        )
    
def contacts_page(response):
    return render(response, "main/contacts.html", 
    {
        "title": "contacts"
        }
        )

def documents_page(response):
    return render(response, "main/documents.html", 
    {
        "title": "documents",
        "all_documents": documents.objects.all().values,
        }
        )

def document_upload_page(request):
    if request.method == 'POST':
        form = upload_document_form(request.POST, request.FILES)

        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            expiry_date = form.cleaned_data['expiry_date']
            author = User.objects.get(username=request.user.username)
            print(request.user.username)

            new_doc = documents(pdf_file=pdf_file, title=title, description=description, expiry_date=expiry_date, author=author)
            new_doc.save()
            pdf_view(pdf_file)

            return HttpResponseRedirect("/documents/")
        return HttpResponseRedirect("/documents/")
    else:
        return render(request, "main/upload_document.html", {
            "form": upload_document_form(),
        })            

def new_note_page(request):
    if request.method == "POST":
        form = new_note_form(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            new_note = notes(title=title,content=content,author=User.objects.get(username=request.user.username))
            new_note.save()
            return HttpResponseRedirect("../{}".format(new_note.id))


        return HttpResponseRedirect("../newnote/")

    else:
        return render(request, "main/newnote.html", {
            "all_notes": notes.objects.all().values,
            "form": new_note_form(),
            }
            )


def pdf_view(request, file):
    print(request.user.id)
    print(documents.objects.filter(author=User.objects.get(id=request.user.id)))
    if request.user.is_authenticated:
            return FileResponse(open('media/{}'.format(file), 'rb'), content_type='application/pdf')
    else:
            raise Http404()