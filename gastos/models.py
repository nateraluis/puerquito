from django.db import models


# Create your models here.

# Model to store households, one household can have multiple users associated to.
class Household(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField("auth.User")

    def __str__(self):
        return self.name


# Model to store spending with multiple currencies
class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# Model to store multiple categories for spending
class CategoryExpense(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryIncome(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model to store Expense with multiple currencies, categories and descriptions, store the user who made the expense, and the household it belongs to
class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(CategoryExpense, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=200)
    date = models.DateField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=False)
    household = models.ForeignKey(Household, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def amount_format(self):
        return "{0:.2f}".format(self.amount)


# Model to store payment with multiple currencies
class Income(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    currency = models.CharField(max_length=3, null=False)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(CategoryIncome, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=False)
    household = models.ForeignKey(Household, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
