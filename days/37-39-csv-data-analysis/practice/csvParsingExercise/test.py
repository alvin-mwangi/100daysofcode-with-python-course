
import collections
from typing import List


Record = collections.namedtuple(
    'Record',
    'RespondentID,USRegion,HouseholdIncome,MainDish'
)


Record.RespondentID = 'test123'

print(getattr(Record, 'RespondentID'))
