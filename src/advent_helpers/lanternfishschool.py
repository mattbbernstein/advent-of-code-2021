from collections import defaultdict

class LanternfishSchool:

    def __init__(self, fish: list[int]):
        '''Creates a lanternfish school'''

        self.school = defaultdict(lambda: 0)
        for f in fish:
            self.school[f] += 1

    def step(self):
        '''Does one timestep'''

        new_school = defaultdict(lambda: 0)
        for fish, count in self.school.items():
            if fish == 0:
                new_school[6] += count
                new_school[8] += count
            else:
                new_school[fish - 1] += count
        self.school = new_school

    def simulate(self, days: int) -> int:
        '''Simulates x days and returns number of fish in school'''
        for _ in range(days):
            self.step()
        school_size = sum(self.school.values())
        return school_size