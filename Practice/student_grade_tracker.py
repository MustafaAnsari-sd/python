class student:
    def __init__(self, name, roll_no, sub1, sub2, sub3):
        self.name = name
        self.roll_no = roll_no
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def calculate_average(self):
        return (self.sub1 + self.sub2 + self.sub3) / 3
    def get_grade(self):
        avg=  self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    def get_info(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Sub1: {self.sub1}, Sub2: {self.sub2}, Sub3: {self.sub3}, Average: {self.calculate_average()}, Grade: {self.get_grade()}"
# Create student objects
std1 = student("Rahul", "101", 85, 90, 78)
std2 = student("Sneha", "102", 88, 92, 80)
print(std1.get_info())
print(std2.get_info())