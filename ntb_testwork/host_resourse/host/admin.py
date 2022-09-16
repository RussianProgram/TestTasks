from django.contrib import admin
from .models import Host

class HostAdmin(admin.ModelAdmin):
    list_display = ['ip',
                    'port',
                    'get_owners',
                    'created_at',
                    'updated_at',
                    'resource']

    fields = ('ip',
              'port',
              'owners',
              'resource')



admin.site.register(Host, HostAdmin)
