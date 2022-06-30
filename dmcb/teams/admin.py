from django.contrib import admin
from teams.models import Team, Participant


class ParticipantInline(admin.TabularInline):
    model = Participant


class TeamAdmin(admin.ModelAdmin):
    inlines = [
        ParticipantInline,
     ]


admin.site.register(Team, TeamAdmin)
admin.site.register(Participant)
