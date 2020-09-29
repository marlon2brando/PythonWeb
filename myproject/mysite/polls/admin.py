from django.contrib import admin

from .models import Question, Choice, SurveyPage

class ChoiceInline(admin.TabularInline):
    model = Choice
    fieldsets = (
        (None, {
            "fields": ['choice_text'],
        }),
    )
    
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ("Question Title", {
    #         "fields": ['question_text'],
    #     }),
    #     ('Date information',{'fields':['pub_date']}
    #     )
    # )
    # inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
    # fields = ['pub_date', 'question_text']


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 4

class SuerveypageAdmin(admin.ModelAdmin):
    model = SurveyPage
    fieldsets = (
        (None, {
            "fields": ['title','question']
        }),
    )
    
    # inlines = [QuestionInline]


# Register your models here.
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(SurveyPage,SuerveypageAdmin)
