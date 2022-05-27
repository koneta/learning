class Student:
    # [assignment] Skeleton class. Add your code here
    name = ""
    age = 0
    tracks = []
    score = 0.00

    def __init__(self, Name, Age, Tracks, Score):
        self.name = Name
        self.age = Age
        self.tracks = Tracks
        self.score = Score

    def change_name(self, newName):
        self.name = newName

    def change_age(self, age):
        self.age = age

    def add_track(self, new_track):
        self.tracks.append(new_track)

    def get_score(self):
        return self.score

    def print(self):
        print(self.name, self.age, self.tracks, self.score)


Bob = Student(Name="Bob", Age=26, Tracks=["FE", "BE"], Score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


Bob.print()
