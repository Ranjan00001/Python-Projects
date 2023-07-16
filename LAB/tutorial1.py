class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


b1= Book('physics','resnick',250)
print(b1)
b2=b1
print(b2)
b2.title = 'calculus'
print(b1.title == 'calculus')
b1.pages += 10        
print(b1.pages)
# dir(math)
