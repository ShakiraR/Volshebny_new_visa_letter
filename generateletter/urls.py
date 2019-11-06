from django.urls import include, path, re_path
from django.contrib import admin
from generateletter import views

app_name = 'Volshebny_visa_letter'

urlpatterns = [
    path("index", views.index, name="index"),    
    path("", views.list_view.as_view(), name="view_visa_letter"),
   # path("list", views.list_view.as_view(), name="list"),
    path("list_copy", views.list_view_copy.as_view(), name="listcopy"),
    path("Myprofile", views.Myprofile, name="Myprofile"),
    path("Organisation", views.Oraganisation, name="Organisation"),
    path("users", views.users, name="users"),
    path("reports", views.reports, name="reports"),
    path("visa_letter_form_submit", views.visa_letter_form_submit, name="visa_letter_form_submit"),
    path("generate_visa_letter", views.visagenerateform, name="generate_visa_letter"),
    re_path(r'^gen_rus_visa/(?P<visa_letter_id>\d+)/$',views.visa_letter_no_stamp,name='visa_letter_no_stamp'),
    path("gen_rus_voucher/<int:pk>", views.visa_voucher_detail, name="gen_rus_voucher"),
    path("english_visa/<int:pk>", views.gen_eng_visa.as_view(), name="gen_eng_visa"),
    path("English_stamp_visa/<int:pk>", views.Eng_stamp_visa.as_view(), name="English_stamp_visa"),
    path("RussianStampVisaLetter/<int:pk>", views.RussianStampVisaLetter.as_view(), name="RussianStampVisaLetter"),
    path("english_voucher/<int:pk>", views.gen_eng_voucher.as_view(), name="gen_eng_voucher"),
    re_path(r'^visa_letters/(?P<visa_letter_id>\d+)/$',views.visa_letter_detail,name='visa'),
    re_path(r'^visa_vouchers/(?P<visa_voucher_id>\d+)/$',views.visa_voucher_detail,name='visa_voucher_detail'),
    path("AllVisaDoc", views.AllVisaDoc, name="AllVisaDoc"),
    path("MumbaiVisa", views.MumbaiVisa, name="MumbaiVisa"),
    path("DelhiVisa", views.DelhiVisa, name="DelhiVisa"),
    path("RussiaVisa", views.RussiaVisa, name="RussiaVisa"),
    path("Login", views.Login, name="Login"),
    path("Signup", views.Signup, name="Signup"),
]

admin.site.index_title = "Welcome, Lets Manage Visa Letters and Vouchers With Ease"
admin.site.site_header = "Volshebny Admin"
admin.site.site_title = "Volshebny Admin Portal"