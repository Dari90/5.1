from django.contrib import admin
from .models import Book, Author, Friend, Publishing_house

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author', )
    fields = ('ISBN', 'title',  'description', 'year_release', 'author', 'copy_count', 'price', 'publishing_house','friend')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')
    fields = ('full_name', 'birth_year', 'country')

@admin.register(Publishing_house)
class Publishing_houseAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
	pass

    

# Register your models here.
