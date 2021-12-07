from csv import reader


def get_one_line_input(file_path):
    with open(file_path, "r") as f:
        elts = f.readline().strip().split(",")
    return elts


def get_csv_line_iterator(file_path):
    with open(file_path) as f:
        spam_reader = reader(f)
        for row in spam_reader:
            if len(row) >= 0:
                yield row
