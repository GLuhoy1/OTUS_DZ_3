import csv
import json
from files import BOOKS_CSV
from files import USERS_JSON

with open(BOOKS_CSV, 'r') as csvfile:
    books_data = list(csv.DictReader(csvfile))

with open(USERS_JSON, 'r') as jsonfile:
    users_data = json.load(jsonfile)

result_data = []
books_per_user, remaining_books = divmod(len(books_data), len(users_data))
for i, user in enumerate(users_data):
    books = books_data[i * books_per_user:(i + 1) * books_per_user]
    if i < remaining_books:
        books.append(books_data[len(users_data) * books_per_user + i])

    user_data = {
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age'],
        'books': books
    }
    result_data.append(user_data)

with open('result.json', 'w') as jsonfile:
    json.dump(result_data, jsonfile, indent=4)