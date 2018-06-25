
import os
from dotenv import load_dotenv
import csv

deal_list = []
deal_list_file_path = r"I:\python_projects\Called Deal Check\deal_list.csv"


def connection_test():
    load_dotenv()
    api_key = os.environ.get("ACCESS_KEYCODE")
    return api_key


def deal_list_check():
    with open(deal_list_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=["dealname"])
        for row in reader:
            deal_list.append(row["dealname"])

    return len(deal_list)


test1 = connection_test()

test2 = deal_list_check()

print(test1)
print(test2)


# https://www.jetbrains.com/help/pycharm/run-debug-configuration-py-test.html
# pytest messes up pycharm debugger apparently
