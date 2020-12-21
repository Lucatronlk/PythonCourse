from IT_team_course_solution import Name
from skill import BackendSkill


class Dev:
    def __init__(self, name, experience, backend_skill):
        self.name = name
        self.experience = experience
        self.backed_skill = backend_skill


class JuniorDev(Dev):
    def __init__(self, name, experience, backend_skill: BackendSkill):
        if 0 <= experience <= 2:
            #if the condition is met, build the object
            super().__init__(name, experience, backend_skill)
        else:
            #if not stop the program
            raise Exception('xp should be within 0-2')

class BackendJuniorDev(JuniorDev):
    def __init__(self, name, experience, backend_skill):
        if backend_skill.rating > 5:
            super().__init__(name,experience,backend_skill)
        else:
            raise Exception('skill should be higher then 5')


    def show(self):
        self.name.show()
        self.backed_skill.show()

jr = BackendJuniorDev(Name("First", "Last"), 2, BackendSkill(6))
jr.show()