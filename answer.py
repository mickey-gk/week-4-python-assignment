class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # introduce method
    def introduce(self):
        print('*' * 46)
        print('*              PERSON\'s DETAILS              *')
        print('*' * 46)
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

person_01 = Person('mickey', 23, 'male')
person_01.introduce()