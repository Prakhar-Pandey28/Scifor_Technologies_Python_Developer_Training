import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.students = []

        self.roll_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.grade_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Roll No:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.roll_var).grid(row=0, column=1)

        tk.Label(self.root, text="Name:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=1, column=1)

        tk.Label(self.root, text="Age:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.age_var).grid(row=2, column=1)

        tk.Label(self.root, text="Grade:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.grade_var).grid(row=3, column=1)

        tk.Button(self.root, text="Accept", command=self.accept_details).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="Display", command=self.display_details).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Search", command=self.search_details).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Delete", command=self.delete_details).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text="Update", command=self.update_details).grid(row=8, column=0, columnspan=2)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=9, column=0, columnspan=2)

    def accept_details(self):
        roll_no = self.roll_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        grade = self.grade_var.get()
        student = Student(roll_no, name, age, grade)
        self.students.append(student)
        messagebox.showinfo("Success", "Details added successfully!")

    def display_details(self):
        if not self.students:
            messagebox.showinfo("Empty", "No details to display.")
            return
        details = ""
        for student in self.students:
            details += f"Roll No: {student.roll_no}\n"
            details += f"Name: {student.name}\n"
            details += f"Age: {student.age}\n"
            details += f"Grade: {student.grade}\n\n"
        messagebox.showinfo("Details", details)

    def search_details(self):
        roll_no = self.roll_var.get()
        for student in self.students:
            if student.roll_no == roll_no:
                messagebox.showinfo("Found", f"Name: {student.name}\nAge: {student.age}\nGrade: {student.grade}")
                return
        messagebox.showinfo("Not Found", "Details not found.")

    def delete_details(self):
        roll_no = self.roll_var.get()
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                messagebox.showinfo("Success", "Details deleted successfully!")
                return
        messagebox.showinfo("Not Found", "Details not found.")

    def update_details(self):
        roll_no = self.roll_var.get()
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = self.name_var.get()
                student.age = self.age_var.get()
                student.grade = self.grade_var.get()
                messagebox.showinfo("Success", "Details updated successfully!")
                return
        messagebox.showinfo("Not Found", "Details not found.")

def main():
    root = tk.Tk()
    root.title("Student Management")
    sms = StudentManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()