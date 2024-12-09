from django.contrib import admin

from .models import *

admin.site.register(UserProfile)

@admin.register(MissingPersonReport)
class MissingPersonReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'date_of_disappearance', 'location_of_disappearance', 'created_at')
    search_fields = ('name', 'location_of_disappearance', 'contact_details')
    list_filter = ('gender', 'date_of_disappearance', 'created_at')


# Admin class for ContactDetails
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

# Admin class for FoundPerson
class FoundPersonAdmin(admin.ModelAdmin):
    list_display = ('your_name', 'phone_number', 'email', 'found_person_name', 'location', 'date_reported')
    search_fields = ('your_name', 'found_person_name', 'location')
    list_filter = ('date_reported',)

# Register the models with the custom admin
admin.site.register(ContactDetails, ContactDetailsAdmin)
admin.site.register(FoundPerson, FoundPersonAdmin)

