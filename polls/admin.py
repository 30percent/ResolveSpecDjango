from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # included tables for editing. (Req Foreign Key)
    list_display = ('question', 'pub_date', "was_published_recently") #decides what's display in admin list view
    list_filter = ['pub_date']
admin.site.register(Poll, PollAdmin)
