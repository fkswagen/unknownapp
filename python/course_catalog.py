class Course:
    def __init__(self, code, title, credits, capacity):
        self.code = code
        self.title = title
        self.credits = credits
        self.capacity = capacity
        
    def __str__(self):
        return f"{self.code.ljust(10)} {self.title.ljust(40)} {str(self.credits).ljust(8)} {self.capacity}"

def main():
    catalog = [
        Course("CS101", "Introduction to Computer Science", 3, 30),
        Course("MATH201", "Calculus I", 4, 35),
        Course("ENG102", "English Composition", 3, 25)
    ]
    
    print("=" * 70)
    print("  COURSE CATALOG")
    print("=" * 70)
    print(f"  {'Code'.ljust(10)} {'Title'.ljust(40)} {'Credits'.ljust(8)} Seats")
    print("  " + "-" * 70)
    
    for course in catalog:
        print(f"  {course}")

if __name__ == "__main__":
    main()
