from peewee import *
database=SqliteDatabase("Pythone.db")

class Book(Model):
    title=TextField()
    author=TextField()
    year=IntegerField()

    class Meta:
        database=database


# Book.create_table()
# Book.create(title="River Between",author="John Mark", year=2008)
# Book.create(title="River of God",author="Chinua Achebe", year=1960)
Book.create(title="Kenya Mpya",author="Juma Achebe", year=1960)

# b1= Book.get(id=1)
# print(b1.title, b1.author)

books= Book.select()
for b in books:
    print(b.title)

# Vehicle plate, make, model, year, right/left , price, color , date of manufacture
# fetch everything
#fetch only make=Toyota
#delete fourth car
#update first car price
