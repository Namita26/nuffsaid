import csv
import datetime


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
        except Exception as e:
            pass
    return list_of_rows


list_of_rows = extract_file_contents()


def search_schools(search_key):
    """
    Searches the search key by cleaning and tokenizing the given string and matches with school names.
    :param search_key: input school name
    :return: prints the matching results with ranks
    """
    # list_of_rows = extract_file_contents()
    search_results_with_ranking = []
    rank = 0

    sub_strings = Tokenizer.sub_string_generator(search_key.lower())
    start_ts = datetime.datetime.now()

    for row in list_of_rows:

        if Search.exact_match(search_key.lower(), row.get("SCHNAM05").lower()) != -1:
            rank = rank + 1
            search_results_with_ranking.append([rank, row.get("LCITY05"), row.get("LSTATE05"), row.get("SCHNAM05")])
            break

        for sub_string in sub_strings:
            if Search.partial_match(sub_string, row.get("SCHNAM05").lower()) != -1:
                rank = rank + 1
                search_results_with_ranking.append([rank, row.get("LCITY05"), row.get("LSTATE05"), row.get("SCHNAM05")])

    end_ts = datetime.datetime.now()
    time_taken = end_ts-start_ts

    print("Results for '%s' (search took %s)" % (search_key, time_taken))
    for row in search_results_with_ranking:
        print("%s. %s" % (row[0], row[3]))
        print("%s, %s" % (row[1], row[2]))


class Search:

    @staticmethod
    def exact_match(search_key, source_string):
        """
        Checks whether search_key and source_string matches exactly.
        :param search_key:
        :param source_string:
        :return: 1 if the string matched exactly and rank as 1 otherwise False
        """
        if search_key == source_string.lower():
            return 1
        return -1

    @staticmethod
    def partial_match(search_key, source_string):
        """
        Searches the entire search_key in the source_string
        :param search_key:
        :param source_string:
        :return:
        """
        if search_key in source_string:
            return 1
        return -1


class Tokenizer:

    @staticmethod
    def sub_string_generator(search_key):
        """
        Generates sub-stings based on the number of words in the search key.
        :param search_key: Input string
        :return: Array of dicts with sub-strings and their relevant rank.
        """
        search_key = Cleaner.remove_all_special_chars(search_key)
        search_keys = search_key.split()
        sub_strings = []

        for i in range(len(search_keys)):
            if i < len(search_keys)-1:
                sub_strings.append(" ".join(search_keys[0:(len(search_keys) - (i+1))]))
            elif i < len(search_keys)-1:
                continue

        return sub_strings


class Cleaner:

    @staticmethod
    def remove_all_special_chars(search_key):
        """
        Removes all predefined special characters from the input string.
        :param search_key: string to be searched
        :return: Same search_key after removing all special chars
        """
        special_chars = ["%", "!", "@", "#", "$", "^", "&", "*", "(", ")", "_", "-", "+", "'", '"', ",", "."]
        for char in special_chars:
            search_key.replace(char, " ")

        return search_key

    @staticmethod
    def digit_split(search_key):
        """
        Splits the given input string if any digit is encountered.
        :param search_key: Input string
        :return: Input string with digits / numbers separated
        """
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for digit in digits:
            search_key.replace(digit, "")

        return search_key


if __name__ == "__main__":
    search_schools("jefferson belleville".lower())