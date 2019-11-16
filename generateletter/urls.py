from django.urls import include, path, re_path
from django.contrib import admin
from generateletter import views

app_name = 'generateletter'

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

    #Generate Visa letter form Url
    path("visa_letter_form_submit", views.visa_letter_form_submit, name="visa_letter_form_submit"),

    #Dictionary Passed of Oraganization Url
    path("generate_visa_letter", views.visagenerateform, name="generate_visa_letter"),

    #Genarate Russian Visa letter withpout stamp Url
    re_path(r'^gen_rus_visa/(?P<visa_letter_id>\d+)/$',views.visa_letter_no_stamp,name='visa_letter_no_stamp'),

    #Genearate Russian Voucher Url
    path("gen_rus_voucher/<int:pk>", views.visa_voucher_detail, name="gen_rus_voucher"),

    #Generate Engllish Visa Url
    path("english_visa/<int:pk>", views.gen_eng_visa.as_view(), name="gen_eng_visa"),

    #Generate English visa with stamp Url
    path("English_stamp_visa/<int:pk>", views.Eng_stamp_visa.as_view(), name="English_stamp_visa"),

    #Geerate Russian stamp visa letter Url
    path("RussianStampVisaLetter/<int:pk>", views.RussianStampVisaLetter.as_view(), name="RussianStampVisaLetter"),

    #Generate English Voucher Url
    path("english_voucher/<int:pk>", views.gen_eng_voucher.as_view(), name="gen_eng_voucher"),
     
    re_path(r'^visa_letters/(?P<visa_letter_id>\d+)/$',views.visa_letter_detail,name='visa'),

    re_path(r'^visa_vouchers/(?P<visa_voucher_id>\d+)/$',views.visa_voucher_detail,name='visa_voucher_detail'),

    #Display all visa letters Url
    path("AllVisaDoc", views.AllVisaDoc, name="AllVisaDoc"),

    #Display mumbai visa letters Url
    path("MumbaiVisa", views.MumbaiVisa, name="MumbaiVisa"),

    #Display Delhi visa letters Url
    path("DelhiVisa", views.DelhiVisa, name="DelhiVisa"),

    #Display Russian visa letters Url
    path("RussiaVisa", views.RussiaVisa, name="RussiaVisa"),

    #Login Url
    path("Login", views.Login, name="Login"),

    #register Url
    path("Signup", views.Signup, name="Signup"),

    #Terms and Conditions Url
    path("terms_cond", views.terms_cond, name="terms_cond"),

    #Add user BSMODAL url
    path('add_users/',views.Add_UsersView.as_view(),name='add_users'),

    #Update user BSMODAL url
    path('userupdate/<int:pk>',views.UserUpdateView.as_view(),name='userupdate'),

    #Delete user BSMODAL url
    path('userdelete/<int:pk>',views.UserDeleteView.as_view(),name='userdelete'),

    #Add Organization BSMODAL url
    path('Add_org/',views.Add_org.as_view(),name='Add_org'),

    #Update payment status BSMODAL URL
    path('Payment_status/<int:pk>',views.Payment_status.as_view(),name='paymentstatus'),

]

admin.site.index_title = "Welcome, Lets Manage Visa Letters and Vouchers With Ease"
admin.site.site_header = "Volshebny Admin"
admin.site.site_title = "Volshebny Admin Portal"