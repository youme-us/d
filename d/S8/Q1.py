import pandas as pd

data = {
    'Book_Title': [
        'Wings of Fire', 'Harry Potter', 'The Alchemist',
        'Ikigai', 'Rich Dad Poor Dad', 'Atomic Habits',
        'The Hobbit', 'Think and Grow Rich'
    ],
    'Author': [
        'A.P.J. Abdul Kalam', 'J.K. Rowling', 'Paulo Coelho',
        'Hector Garcia', 'Robert Kiyosaki', 'James Clear',
        'J.R.R. Tolkien', 'Napoleon Hill'
    ],
    'Category': [
        'Biography', 'Fantasy', 'Fiction', 'Self-help',
        'Finance', 'Self-help', 'Fantasy', 'Finance'
    ],
    'Rating': [4.8, 4.7, 4.5, 4.4, 4.6, 4.8, 4.7, 4.3]
}

df = pd.DataFrame(data)

print("First 5 Book Records:")
print(df.head())