class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        return 'C'