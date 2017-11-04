# We getting some milestones: when road between some town and Rome was built/destroyed
# We can have multiple situations of each kind
# Class Roads have cities dictionary that contains all info:
# Key is city name, value is dictionary with two keys:
# build - set of build milestones, destroy - set of destruction milestones

# Need to get list of cities names that connected with Rome at the given year

# PS algorithm is stupid and straightforward, could be done better with sorting of milestones


class Roads:
    def __init__(self):
        self.cities = dict()

    def add(self, city, t):
        if city in self.cities.keys():
            self.cities[city]['build'].add(t)
        else:
            self.cities.update(
                {
                    city:
                    {
                        'build': {t},
                        'destroy': set()
                    }
                })

    def remove(self, city, t):
        if city in self.cities.keys():
            self.cities[city]['destroy'].add(t)
        else:
            self.cities.update(
                {
                    city:
                        {
                            'build': set(),
                            'destroy': {t}
                        }
                })

    def query(self, t):
        # Enumerate known cities
        for item in self.cities.items():
            # If given year coincides with one of city road build milestones - now its okay obviously
            if t in item[1]['build']:
                yield item[0]
            # Check if given year is not coincides with one of city road destruction milestones
            # If so, now road is destroyed obviously
            elif t not in item[1]['destroy']:
                # Enumerate city road build dates
                for build_date in item[1]['build']:
                    # If once upon a time road was built before now, it can be okay (maybe) ...
                    if build_date < t:
                        valid_year = True
                        for destroy_date in item[1]['destroy']:
                            # ... unless it was destroyed after built and before now
                            if build_date < destroy_date < t:
                                valid_year = False
                                break
                        if valid_year:
                            yield item[0]
                            break

# some tests
rs = Roads()
rs.add('Rimini', -260)
rs.add('Bologna', -180)
print(list(rs.query(-180)))
print(list(rs.query(-100)))

rs.add('Piacenza', -210)
print(list(rs.query(-190)))

rs.remove('Rimini', -200)
print(list(rs.query(-200)))
print(list(rs.query(-170)))