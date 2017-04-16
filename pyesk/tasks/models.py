from django.db import models


class Ticket(models.Model):
    PRIORITY_NAMES = (
        ('niski', 'Niski'),
        ('średni', 'Średni'),
        ('wysoki', 'Wysoki'),
    )

    user = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10, null=True, blank=True)
    category = models.ForeignKey("Category")
    priority = models.CharField(max_length=40, choices=PRIORITY_NAMES)

    def save(self, *args, **kwargs):
        if not self.code:
            super().save(*args, **kwargs)
            self.code = "{}/{}".format(self.category, self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Priority(models.Model):
    PRIORITY_NAMES = (
        ('niski', 'Niski'),
        ('średni', 'Średni'),
        ('wysoki',  'Wysoki'),
    )

    def __str__(self):
        return self.name
