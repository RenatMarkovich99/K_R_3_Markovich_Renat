from utils.services import load_json, get_last_five_successful_operations, sort_by_date, print_info, filename

if __name__ == '__main__':
    json_data = load_json(filename)
    sorted_operation = sort_by_date(json_data)
    last_five_operations = get_last_five_successful_operations(sorted_operation)
    print_info(last_five_operations)
