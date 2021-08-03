from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('note/', views.new_note_page, name="index"),
    path('note/<int:id>/', views.note_page, name="index"),
    path('note/newnote/', views.new_note_page, name="index"),
    path('contacts/', views.contacts_page, name="index"),
    path('calender/', views.calender_page, name="index"),
    path('documents/', views.documents_page, name="index"),
    path('documents/upload/', views.document_upload_page, name="index"),
    path('documents/<str:file>/', views.pdf_view, name="index"),
]
