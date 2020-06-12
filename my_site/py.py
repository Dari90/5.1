authors = Authors.objects \
    .annotate(books_count=Count('book')) \ 
    .filter(books_count__gt=1) 
total_sum = Book.objects \
    .filter(author__in=authors) \ 
    .aggregate(total = Sum(F('copy_count') = F('price'), output_field=FloatField())) 
result = round(total_sum['total'], 2)