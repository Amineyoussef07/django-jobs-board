from django.contrib import admin
from .models import Job


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "salary", "job_type", "experience", "published_at"]
    list_display_links = ["title", "published_at"]
    list_editable = ["salary", "job_type"]
    search_fields = ["title", "experience"]
    list_filter = ["title", "salary"]


# -----------------------------------------------
admin.site.register(Job,ProductAdmin)
# -----------------------------------------------
admin.site.site_header = "Nouvil"
admin.site.site_title = "Nouvil"
