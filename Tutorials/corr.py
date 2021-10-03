def searcher():
 import time
 book = "this is a function which is made to study coroutines"
 time.sleep(4)
 while True:
     text = (yield)
     if text in book : print("Text is in the book")
     else: print("text is not in the book")

search = searcher()
next(search)
search.send("function")
input("press any key")
search.send("this is")

 

