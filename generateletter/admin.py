from django.contrib import admin
from django.contrib.auth.models import Group
from generateletter.models import Visaletters, Organization, CustomUserM
import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Excel"

# Register your models here.
class VisalettersAdmin(admin.ModelAdmin,ExportCsvMixin):

    search_fields = ["Visa_Letter_Number","Organization_Details", "Date_of_letter"]
    list_filter = ["Organization_Details", "Payment_status"]
    list_display = [
        "Visa_Letter_Number",
        "Date_of_letter",
        "entry_from",
        "departure_to",
        "Routes_and_Places",
        "no_passengers",
        "Organization_Details",
        "Payment_status",
    ]


    list_editable = ["Payment_status"]
    actions = ["export_as_csv"]

class OrganizationAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = [
        "Name_of_Organization",
        "Address",
    ]
    actions = ["export_as_csv"]
admin.site.register(Visaletters, VisalettersAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(CustomUserM)
admin.site.unregister(Group)
