class Student:
    name = "Marcin"

    @classmethod
    def tstring(cls):
        print(cls.name)


Student.tstring()
