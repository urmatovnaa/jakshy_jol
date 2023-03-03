from django.contrib import admin

from django.contrib.admin import TabularInline

from apps.test_pdd.models import Test, Answer


class AnswerAdminInLine(TabularInline):
    extra = 1
    model = Answer
    max_num = 4


@admin.register(Test)
class AnswerAdmin(admin.ModelAdmin):
    inlines = (AnswerAdminInLine,)
    list_display = ('id',)


