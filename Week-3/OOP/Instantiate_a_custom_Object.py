class MyFirstClass():
    print("Khong Hieu Bon Nay Day Cai Gi")
    def __init__(self) -> None:
        self.index = "Author-Book"
    
    def hand_list(self, philosopher, book):
        print(self.index)
        print(f" {str(philosopher)} wrote the book: {str(book)}")
        
if __name__ == "__main__":
    whodunnit = MyFirstClass()
    whodunnit.hand_list(
        "Sun Tzu",
        "The Art of War",
    )