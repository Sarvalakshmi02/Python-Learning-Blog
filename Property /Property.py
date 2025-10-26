class Student:
    def __init__(self, name, marks):
        self._name = name
        self._marks = marks

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Marks must be between 0 and 100.")
        self._marks = value

    def __str__(self):
        return f"Student Name: {self._name}, Marks: {self._marks}"
