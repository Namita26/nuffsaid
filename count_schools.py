import csv


def extract_file_contents():
    """
    Extracts the given CSV contents.
    :return: list of CSV file rows.
    """
    list_of_rows = []
    # provide the exact file path from your system.
    with open('/Users/namitamaharanwar/Documents/sl051bai_mod1.csv', newline='') as data_file:
        reader = csv.DictReader(data_file)
        try:
            for row in reader:
                list_of_rows.append(row)
        except Exception as exp:
            pass
    return list_of_rows


def print_counts():
    """
    Prints results of following questions:
    How many total schools are in this data set?
    How many schools are in each state?
    How many schools are in each Metro-centric locale?
    What city has the most schools in it? How many schools does it have in it?
    How many unique cities have at least one school in it?
    """
    list_of_rows = []
    metro_centric_locales = ['1', '2', '3', '4', '5', '6', '7', '8']
    list_of_rows = extract_file_contents()

    # How many total schools are in this data set?
    list_of_schools = list(map(lambda x: x.get("SCHNAM05"), list_of_rows))
    print("Total Schools: %s" % len(list_of_schools))

    # How many schools are in each state?
    list_of_states = set(list(map(lambda x: x.get("LSTATE05"), list_of_rows)))

    print("Schools by State:")

    for state in list_of_states:
        print("%s: %s" % (state, len(list(filter(lambda x: x.get("LSTATE05") == state, list_of_rows)))))

    # How many schools are in each Metro-centric locale?
    print("Schools by Metro-centric locale:")
    for mlocale in metro_centric_locales:
        print("%s: %s" % (mlocale, len(list(filter(lambda x: x.get("MLOCALE") == mlocale, list_of_rows)))))

    # What city has the most schools in it? How many schools does it have in it?
    list_of_cities = set(list(map(lambda x: x.get("LCITY05"), list_of_rows)))
    city_wise_schools = {}

    for row in list_of_rows:
        city = row.get("LCITY05")
        if city in city_wise_schools.keys():
            city_wise_schools[city] = city_wise_schools[city] + 1
        else:
            city_wise_schools[city] = 1

    _sorted = sorted(city_wise_schools, key=city_wise_schools.get, reverse=True)
    print("City with most schools: %s (%s schools)" % (_sorted[0], city_wise_schools[_sorted[0]]))
    print("Unique cities with at least one school: %s" % len(list_of_cities))


if __name__ == "__main__":
    print_counts()
