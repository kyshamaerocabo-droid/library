from django.db import models

# Model 1: Category (Many-to-Many target)
class Category(models.Model):
    """Represents a genre or type of book."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

# Model 2: Author (Foreign Key target)
class Author(models.Model):
    """Represents a book's author."""
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Model 3: Book
class Book(models.Model):
    """Represents a single book with relationships to Author and Category."""
    title = models.CharField(max_length=255)

    # Foreign Key (One-to-Many): A Book has one Author, an Author can have many Books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    # Many-to-Many: A Book can have many Categories, a Category can have many Books.
    categories = models.ManyToManyField(Category, related_name='books')

    # Date field for the published year/date
    published_date = models.DateField(help_text="Date the book was first published.")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
