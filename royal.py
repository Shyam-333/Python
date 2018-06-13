class book:
    def __init__(self,a='Notebook',b='Nicholas Sparks',c='SSG Publisher',p=545,r='Stark'):
        self.title=a
        self.author=b
        self.publisher=c
        self.price=p
        self.royalty=r
    def get_title(self):
        return self.title
    def set_title(self,a):
        self.title=a
        return
    def get_author(self):
        return self.author
    def set_author(self,b):
        self.author=b
        return
    def get_publisher(self):
        return self.publisher
    def set_publisher(self,c):
        self.publisher=c
        return
    def get_price(self):
        return self.price
    def set_price(self,p):
        self.price=p
        return
    def get_royalty(self):
        return self.royalty
    def set_royalty(self,r):
        self.royalty=r
        return
    def royalty(price,copies):
        if(copies == 500):
            amt=0.1*500
            return amt
        elif(copies>500 && copies<=1000):
            amt=0.125*1000
            return amt
        else(copies>1000):
            amt=0.15*copies
            return amt

class ebook(book):
    def __init__(self,a='EPUB',b='MOBI',c='PDF'):
        self.format1=a
        self.format2=b
        self.format3=c
    def royalty(price,copies):
        amt+=0.12*copies
