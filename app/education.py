class TradingEducation:
    def __init__(self):
        self.courses = []

    def add_course(self, course_name):
        """Add a trading course."""
        self.courses.append(course_name)
        print(f"Course '{course_name}' added successfully!")

    def show_courses(self):
        """Show all available trading courses."""
        for course in self.courses:
            print(course)