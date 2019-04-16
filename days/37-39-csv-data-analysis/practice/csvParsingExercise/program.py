import os
import csv
import collections
from typing import List

data = []

Record = collections.namedtuple(
    'Record',
    'RespondentID,USRegion,HouseholdIncome,MainDish'
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data',
                                         'thanksgiving-2015-poll-data.csv')

    data.clear()
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            # print(f'ROW--> {row}')
            record = parse_row(row)
            data.append(record)
            # print(record)
        # usRegions = set([row['US Region'] for row in reader
        #                 if row['US Region'] != ''])
        # print(usRegions)


def parse_row(row):
    record = Record(row['RespondentID'],
                    row['US Region'],
                    row['How much total combined money did all'
                    ' members of your HOUSEHOLD earn last year?'],
                    row['What is typically the main dish at your'
                    ' Thanksgiving dinner?'])
    return record


def most_common_item_per_region(item_name, usRegions):
    result = {}

    for region in usRegions:
        itemValues = sorted([getattr(record, item_name) for record in data
                             if record.USRegion == region])
        mostCommonItemValue = max(set(itemValues), key=itemValues.count)
        result[region] = mostCommonItemValue

    return result


def main():
    # get regions
    usRegions = set(record.USRegion for record in data
                    if record.USRegion != '')
    # print(usRegions)
    usRegions = sorted(usRegions)
    print(most_common_item_per_region('HouseholdIncome', usRegions))

if __name__ == "__main__":
    init()
    main()
