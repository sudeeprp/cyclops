import sys
import csv


COMPLEXITY_COLUMN = 'complexity'
METHOD_COLUMN = 'method_location'


def lizard_fields_to_function_complexity(fields):
    EXPECTED_COLS_IN_CSV = 11
    FUNC_WITH_PAR_POS_IN_CSV = 8
    COMPLEXITY_POS_IN_CSV = 1
    complexity_map = {}

    assert (len(fields) == EXPECTED_COLS_IN_CSV), f'Unexpected CSV:\n{fields}'

    func_with_params = fields[FUNC_WITH_PAR_POS_IN_CSV]
    complexity_map[func_with_params] = int(fields[COMPLEXITY_POS_IN_CSV])
    return complexity_map


def fields_to_complexity_map(parsed_lines):
    complexity_dict = {}
    for line_fields in parsed_lines:
        func_complexity = \
            lizard_fields_to_function_complexity(line_fields)
        complexity_dict.update(func_complexity)
    return complexity_dict


def get_method_complexity(method_name, complexity_dict):
    method_complexity = 0
    if method_name in complexity_dict:
        method_complexity = complexity_dict[method_name]
    return method_complexity


def new_complexity_is_ok(new_complexity_limit,
                         new_methods_complexity, reference_methods_complexity):
    if not new_methods_complexity:
        return False
    complexity_is_ok = True
    for method in new_methods_complexity:
        reference_complexity = get_method_complexity(method, reference_methods_complexity)
        new_complexity = new_methods_complexity[method]
        if new_complexity > new_complexity_limit and new_complexity > reference_complexity:
            print(f'\n{method} complexity is {new_complexity}')
            if reference_complexity > 0:
                print(f'It was {reference_complexity}')
            complexity_is_ok = False
            break
    return complexity_is_ok


def map_methods_complexity(report_csv_filename):
    with open(report_csv_filename, 'r') as report:
        csv_reader = csv.reader(report)
        return fields_to_complexity_map(csv_reader)


def new_report_is_ok(new_complexity_limit, new_report_csv_filename, reference_report_csv_filename):
    new_methods_complexity = map_methods_complexity(new_report_csv_filename)
    reference_methods_complexity = map_methods_complexity(reference_report_csv_filename)
    return new_complexity_is_ok(new_complexity_limit,
                                new_methods_complexity, reference_methods_complexity)


def print_usage_and_exit():
    print(f'''
Usage:
{sys.argv[0]} <complexity-limit new code> <new report csv> <reference report csv>''')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print_usage_and_exit()

    complexity_limit = 3
    try:
        complexity_limit = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit()

    if new_report_is_ok(new_complexity_limit=complexity_limit, new_report_csv_filename=sys.argv[2],
                        reference_report_csv_filename=sys.argv[3]):
        sys.exit(0)
    else:
        sys.exit(1)
