from django.contrib import admin

from models import Project, ProjectPhase, Ticket

for m in [Project, ProjectPhase, Ticket]:
    admin.site.register(m)
