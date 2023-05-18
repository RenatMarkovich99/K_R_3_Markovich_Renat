from utils.services import load_json
from utils.services import sort_by_date
from utils.services import

def main():
    data = load_json(filename)
    sorted_data = sort_by_data(data)

    last_5 = get_last_five_successful_operations(sorted_data)


#main()
