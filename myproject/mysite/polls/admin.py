from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    fieldsets = (
        (None, {
            "fields": ['choice_text'],
        }),
    )
    
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Question Title", {
            "fields": ['question_text'],
        }),
        ('Date information',{'fields':['pub_date']}
        )
    )
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
    # fields = ['pub_date', 'question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
