from django.contrib import admin


from .models import applists, csvs, customer
admin.site.register(applists)
admin.site.register(customer)
admin.site.register(csvs)