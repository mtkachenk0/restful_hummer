from django.db import models


class Model(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(Model):

    name = models.CharField(max_length=82)
    parent_category = models.ForeignKey(to='self', default=None, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey('auth.User', related_name='categories')
    created = models.DateTimeField(auto_now_add=True)


class Item(Model):

    name = models.CharField(max_length=82)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category)
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
