emotions = {'happiness': 3, 'anger': 1, 'sadness': 2}

class Person:

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        print(f'{self.name} is feeling {self.emotions}')

    def feeling(self):
        feeling_level = emotions[self.emotions]
        feeling = []
        if feeling_level == 1:
            feeling_level = 'low'
        elif feeling_level == 2:
            feeling_level = 'medium'
        else:
            feeling_level == 3
            feeling_level = 'high'
        return (f"I'm {self.name} and I'm feeling {feeling_level} {self.emotions}")

person1 = Person('Jack', 'sadness')
person2 = Person('James', 'happiness')
person3 = Person('Mark', 'anger')
print(person1.feeling())
print(person2.feeling())
print(person3.feeling())