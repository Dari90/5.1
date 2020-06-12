from django.db import models  

  
class Author(models.Model):  
    full_name = models.TextField(max_length=100, unique=True, verbose_name='Имя автора')  
    birth_year = models.SmallIntegerField(verbose_name='Дата рождения автора')  
    country = models.CharField(max_length=2, verbose_name='Страна автора')

    def __str__(self):
        return self.full_name

class Publishing_house(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование издательства', unique=True)
    

    def __str__(self):
        return self.name

class Friend(models.Model):
	friend_name = models.CharField(max_length=30, verbose_name='Имя друга')

	def __str__(self):
		return self.friend_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13, verbose_name='ISBN')  
    title = models.TextField(verbose_name='Наименование книги')  
    description = models.TextField(verbose_name='Описание книги')  
    year_release = models.SmallIntegerField(verbose_name='Год издания')  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    copy_count = models.IntegerField(default=1, verbose_name='Количество копий')
    price = models.DecimalField(max_digits = 10, decimal_places=2, default=0, verbose_name='Цена')
    publishing_house = models.ForeignKey(Publishing_house, on_delete=models.CASCADE, 
        verbose_name='Издательство', null=True, blank=True, 
        related_name="books", related_query_name="book")
    friend = models.ForeignKey(Friend, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Друг', related_name='books')
    
    def __str__(self):
            return self.title

            

