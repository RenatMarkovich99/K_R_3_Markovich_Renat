from utils.services import load_json, get_last_five_successful_operations, sort_by_date, sorted_data,


if __name__ == '__main__':
    main()
    json_dict = load_json(filename)
    sorted_data = sort_by_data(json_dict)
    last_5 = get_last_five_successful_operations(sorted_data)



