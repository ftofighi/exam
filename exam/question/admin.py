from django.contrib import admin
from .models import Question, Option
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserChangeForm, CustomerUserCreationForm
from .models import User

class CustomerUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm

    model = User
    list_display = ('phone', 'is_staff', 'is_active')
    list_filter = ('phone',)

    fieldsets = (
        ('اطلاعات اولیه', {'fields': ('phone', 'password')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','password1', 'password2',)}
         ),
    )

    ordering = ('phone',)


class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        OptionInline
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, CustomerUserAdmin)

