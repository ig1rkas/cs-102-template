class Recomendation:
    def __init__(self, films_file="films.txt", users_file="users.txt"):
        films = list(map(
            lambda x: [int(x[0]), " ".join(x[1:]).rstrip()], 
            map(
                lambda x: x.split(","), 
                open(films_file, "r", encoding="UTF8").readlines()
                )
            ))
        self.films = dict()
        for n, film in films:
            self.films[n] = film
        self.users = list(map(lambda x: set(map(int, x.split(","))), open(users_file, "r").readlines()))
    
    def rec_film(self, watched: list) -> list:
        recs = {}
        watched = set(watched)
        for user in self.users:
            intersecection = watched & user
            if len(intersecection) >= len(watched) // 2:
                power = round(len(intersecection) / len(watched), 2)
                for film in user - watched:
                    if self.films[film] not in recs:
                        recs[self.films[film]] = 0
                    recs[self.films[film]] += power
        return list(map(lambda x: x[0], sorted(list(zip(recs.keys(), recs.values())), key=lambda x: -x[1])))


if __name__ == "__main__":
    rec = Recomendation("films1.txt", "users1.txt")
    print(rec.rec_film(list(map(int, input().split()))))