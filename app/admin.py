# from django.contrib import admin
# from app.models import Category, Food

from django.contrib import admin, messages
from django.contrib.auth.models import Group, User
from django.forms import ModelForm
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin

# admin.site.register(Category)
# admin.site.register(Food)


from app.forms import FoodModelForm, ChefModelForm
from app.models import Category, Food, Chef
from django.contrib.admin import AdminSite, ModelAdmin

admin.site.site_header = "Panda"
admin.site.site_title = "Admin"
admin.site.index_title = "H_O_M_E"


# ---------------------------------------------------------------------

class FoodAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"


product_admin_site = FoodAdminSite(name='product_admin')
product_admin_site.register(Food)


# --------------------------------------------------------------------

class ChefAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"


product_admin_site = ChefAdminSite(name='chef_admin')
product_admin_site.register(Chef)

# -------------------------------------------------------------------

admin.site.unregister(Group)


# --------------------------------------------------------------------

class FoodModelForm1(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodModelForm1, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Food image'
        self.fields['title'].help_text = 'Food title'
        self.fields['text'].help_text = 'Food description'
        self.fields['price'].help_text = 'Food price'
        self.fields['category'].help_text = 'Food category'

    class Meta:
        model = Food
        exclude = ()


# --------------------------------------------------------------------

class ChefModelForm1(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChefModelForm1, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Chef image'
        self.fields['name'].help_text = 'Chef name'
        self.fields['job'].help_text = 'Chef job'
        self.fields['text'].help_text = 'Chef text'

    class Meta:
        model = Chef
        exclude = ()


# --------------------------------------------------------------------

MAX_OBJECTS = 4


@admin.register(Food)
class FoodAdmin(ModelAdmin):
    form = FoodModelForm
    list_display = ('image_tag', 'title', 'price', 'category')  # table kurinishida chiqarish
    # list_filter = ('title', 'price', 'text')              # filter qilish
    list_per_page = 8  # pagenation qilish
    """readonly_fields --> da berilgan fieldlar adminda ishlamaydi"""
    """ style="max-height: 100px; max-width: 100px;" />' """
    # readonly_fields = ['title', 'price']
    search_fields = ('title',)  # search qilish
    ordering = ('title',)  # order by
    autocomplete_fields = ['category', ]  # Category buyicha search qilish

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-height: 70px; max-width: 70px;" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return True
        return super().has_add_permission(request)


# -----------------------------------------------------------------------------

@admin.register(Chef)
class ChefAdmin(ModelAdmin):
    form = ChefModelForm
    list_display = ('image_tag', 'name', 'job', 'text')  # table kurinishida chiqarish
    list_per_page = 5
    # search_fields = ('title',)  # search qilish
    # ordering = ('title',)  # order by

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-height: 70px; max-width: 70px;" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return True
        return super().has_add_permission(request)


# --------------------------------------------------------------------

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
