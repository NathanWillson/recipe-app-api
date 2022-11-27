# from django.contrib import admin  # noqa
"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    # 56
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)

# underscore.
# And basically what this does is it integrates with the Django translation
# system.So if you do change the language of Django and you want to change it
# for everywhere in your project, then you can do it in the configuration and
# it means any way you use this translation shortcut here,
# it's going to automatically translate the text, which is really useful and
# this is just best practice.
# We're not actually going to be implementing any translation in our code, but
# it's always best practice to do this just in case you do need to integrate
# translation later on in the project. Okay, so the reason we're integrating
# the translation here is because we want to translate the values
# that we're putting in.
# So here when we have non we're just not paying a title bar in this one,
# we are actually going to put a title.
# So I'll take underscore which kind of calls this get lazy function here.
# We name it as underscore.
# This is just the standard convention that Django uses.
# You could name this as translate or something.
# That just means that you need to type, translate or type the function name
# every time you want to call it.
