from tortoise import models, fields


class Article(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    description = fields.TextField()
    
class Author(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    books: fields.ManyToManyRelation["Book"]
    
class Category(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    books: fields.ManyToManyRelation["Book"]

class Book(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    authors: fields.ManyToManyRelation[Author] = fields.ManyToManyField("models.Author", related_name="books")
    genres: fields.ManyToManyRelation[Category] = fields.ManyToManyField("models.Category", related_name="books")