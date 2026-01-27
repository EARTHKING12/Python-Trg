from bs4 import BeautifulSoup

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Available Books</h1>
    <p class="Books">Book 1</p>
    <p class="Books">Book 2</p>
    <p class="Books">Book 3</p>
</body>
</html>"""

soup = BeautifulSoup(html_content, "html.parser")
books = soup.find_all("p", class_="Books")

for book in books:
    print(book.text)
