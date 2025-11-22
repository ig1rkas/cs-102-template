class SplitOnGroups:
    def __init__(self, age_range='18 25 35 45 60 80 100'):
        age_range = [-1] + list(map(int, age_range.split())) + [123]
        self.ranges = []
        for i in range(1, len(age_range)):
            if age_range[i] == 123:
                self.ranges.append(range(age_range[i - 1] + 1, 124))
                continue
            self.ranges.append(range(age_range[i - 1] + 1, age_range[i] + 1))
        
    def split_by_age(self, array: list, out=False) -> list:
        """
        array: list, all names and ages
        out: bool, should to out or not
        """
        self.groups = [[] for i in self.ranges]
        for person in array:
            name, age = person[:-1], int(person[-1])
            for i in range(len(self.ranges)):
                if age in self.ranges[i]:
                    self.groups[i].append(" ".join(name) + f" ({age})")
        if out:
            for i in range(len(self.groups) - 1, -1, -1):
                if self.groups[i]:
                    print(f"{list(self.ranges[i])[0]}-{list(self.ranges[i])[-1]}: {", ".join(self.groups[i])}")

        return [i for i in self.groups if i]

if __name__ == "__main__":
    son = SplitOnGroups()
    array = []
    while 1:
        inp = input()
        if inp == "END": break
        array.append(tuple(inp.split()))

    son.split_by_age(list(set(array)), out=True)