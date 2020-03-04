from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Student, Parent
# Register your models here.

'''
The ModelAdmin class is a representation of user-defined models in the admin panel. 
It can be used to override various actions. 
There is a whole range of options opened with ModelAdmin Class.
'''
# Admin Action Functions


def change_rating(modeladmin, request, queryset):
    print(queryset)
    queryset.update(ratings='e')


def change_gender(modeladmin, request, queryset):
    print(queryset)
    queryset.update(gender='f')


# Action description
change_rating.short_description = "Mark Selected Products as Excellent"
change_gender.short_description = "Change gender to female if u want"


class StudentAdmin(admin.ModelAdmin):
    # fields = ('name', 'age')
    # exclude = ('gender',)
    list_display = ('name', 'cource', 'combine_name_and_cource', 'gender')
    list_filter = ('age',)
    actions = [change_rating, change_gender]
    list_display_links = ('name', 'cource',)
    list_editable = ('gender',)
    search_fields = ('name',)

    # date_hierarchy = 'age'
    def combine_name_and_cource(self, obj):
        return "{}-{}".format(obj.name, obj.cource)


'''
If you want to change that view you can set your own template modifying admin.site.index_template and admin.site.app_template.
If you want to just change the CSS what you can do is to specify here your own template and that template to extend the default one. 
Of course in your new template you would be adding your own CSS file.
'''

admin.site.site_header = 'Student Model Admin'
admin.site.site_title = 'My Product Inventory '
admin.site.index_title = "Model Adminstration"
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent)
admin.site.unregister(Group)
