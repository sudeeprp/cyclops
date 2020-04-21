import sys


COMPLEXITY_COLUMN = 'complexity'
METHOD_COLUMN = 'method_location'


def extract_column_map(heading_row_text):
    column_map = {}
    headings = heading_row_text.split()
    try:
        column_map[COMPLEXITY_COLUMN] = headings.index('CCN')
        column_map[METHOD_COLUMN] = headings.index('location')
    except ValueError:
        column_map = {}
    return column_map


def method_locator(method_col):
    method_components = method_col.split('@')
    filename = ''
    if len(method_components) >= 3:
        filename = method_components[2]
    return filename + '/' + method_components[0]


def extract_complexity(method_line, column_map):
    method_descriptors = method_line.split()
    try:
        method_location = method_locator(method_descriptors[column_map[METHOD_COLUMN]])
        complexity = int(method_descriptors[column_map[COMPLEXITY_COLUMN]])
    except (ValueError, IndexError):
        method_location = None
        complexity = 0
    return method_location, complexity


def record_method(dict, method_entry, complexity_number):
    def compose_method_serial(method, serial):
        return method + '/' + str(serial)
    if method_entry is not None:
        trial_number = 1
        while compose_method_serial(method_entry, trial_number) in dict:
            trial_number += 1
        dict[compose_method_serial(method_entry, trial_number)] = complexity_number


def map_methods_complexity(report_txt_filename):
    column_map = []
    complexity_dict = {}
    with open(report_txt_filename, 'r') as report:
        for line in report:
            bare_line = line.strip()
            if len(bare_line) == 0:
                pass
            elif bare_line[0] == '=':
                column_map = []
            elif bare_line[0].isalpha():
                column_map = extract_column_map(heading_row_text=bare_line)
            elif bare_line[0].isdigit() and len(column_map) > 0:
                method_location, complexity = \
                    extract_complexity(method_line=bare_line, column_map=column_map)
                record_method(complexity_dict, method_location, complexity)
    return complexity_dict


def get_method_complexity(method_name, complexity_dict):
    method_complexity = 0
    if method_name in complexity_dict:
        method_complexity = complexity_dict[method_name]
    return method_complexity


def new_complexity_is_ok(new_complexity_limit,
                         new_methods_complexity, reference_methods_complexity):
    complexity_is_ok = True
    for method in new_methods_complexity:
        reference_complexity = get_method_complexity(method, reference_methods_complexity)
        new_complexity = new_methods_complexity[method]
        if  new_complexity > new_complexity_limit and new_complexity > reference_complexity:
            print(f'\n{method} complexity is {new_complexity}')
            if reference_complexity > 0:
                print(f'It was {reference_complexity}')
            complexity_is_ok = False
            break
    return complexity_is_ok


def new_report_is_ok(new_complexity_limit, new_report_txt_filename, reference_report_txt_filename):
    new_methods_complexity = map_methods_complexity(new_report_txt_filename)
    reference_methods_complexity = map_methods_complexity(reference_report_txt_filename)
    return new_complexity_is_ok(new_complexity_limit,
                                new_methods_complexity, reference_methods_complexity)


def print_usage_and_exit():
    print(f'''
Usage:
{sys.argv[0]} <complexity-limit new code> <new report txt> <reference report txt>''')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print_usage_and_exit()

    complexity_limit = 3
    try:
        complexity_limit = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit()

    if new_report_is_ok(new_complexity_limit=complexity_limit, new_report_txt_filename=sys.argv[2],
                        reference_report_txt_filename=sys.argv[3]):
        sys.exit(0)
    else:
        sys.exit(1)
