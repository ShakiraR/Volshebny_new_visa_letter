from django.urls import include, path, re_path
from django.contrib import admin
from generateletter import views

app_name = 'Volshebny_visa_letter'

urlpatterns = [
    #Index Page Url
    path("abc", views.index, name="index"),    
    #View Visa letter Url
    path("", views.list_view.as_view(), name="view_visa_letter"),
    path("list_copy", views.list_view_copy.as_view(), name="listcopy"),
    #Profile Url
    path("Myprofile", views.Myprofile, name="Myprofile"),
    #Display list of oraganization Url 
    path("Organisation", views.Oraganisation, name="Organisation"),
    #Display list of Users Url 
    path("users", views.users, name="users"),
    #Display Reports Url
    path("reports", views.reports, name="reports"),
    #Generate Visa letter form
    path("visa_letter_form_submit", views.visa_letter_form_submit, name="visa_letter_form_submit"),
    #Dictionary Passed of Oraganization
    path("generate_visa_letter", views.visagenerateform, name="generate_visa_letter"),
    #Genarate Russian Visa letter withpout stamp
    re_path(r'^gen_rus_visa/(?P<visa_letter_id>\d+)/$',views.visa_letter_no_stamp,name='visa_letter_no_stamp'),
    #Genearate Russian Voucher
    path("gen_rus_voucher/<int:pk>", views.visa_voucher_detail, name="gen_rus_voucher"),
    #Generate Engllish Visa
    path("english_visa/<int:pk>", views.gen_eng_visa.as_view(), name="gen_eng_visa"),
    #Generate English visa with stamp
    path("English_stamp_visa/<int:pk>", views.Eng_stamp_visa.as_view(), name="English_stamp_visa"),
    #Geerate Russian stamp visa letter
    path("RussianStampVisaLetter/<int:pk>", views.RussianStampVisaLetter.as_view(), name="RussianStampVisaLetter"),
    #Generate English Voucher
    path("english_voucher/<int:pk>", views.gen_eng_voucher.as_view(), name="gen_eng_voucher"),
     
    re_path(r'^visa_letters/(?P<visa_letter_id>\d+)/$',views.visa_letter_detail,name='visa'),

    re_path(r'^visa_vouchers/(?P<visa_voucher_id>\d+)/$',views.visa_voucher_detail,name='visa_voucher_detail'),
    path("AllVisaDoc", views.AllVisaDoc, name="AllVisaDoc"),
    path("MumbaiVisa", views.MumbaiVisa, name="MumbaiVisa"),
    path("DelhiVisa", views.DelhiVisa, name="DelhiVisa"),
    path("RussiaVisa", views.RussiaVisa, name="RussiaVisa"),
    path("Login", views.Login, name="Login"),
    path("Signup", views.Signup, name="Signup"),
    path("terms_cond", views.terms_cond, name="terms_cond"),
]

admin.site.index_title = "Welcome, Lets Manage Visa Letters and Vouchers With Ease"
admin.site.site_header = "Volshebny Admin"
admin.site.site_title = "Volshebny Admin Portal"