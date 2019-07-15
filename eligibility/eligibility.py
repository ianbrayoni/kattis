"""
https://open.kattis.com/problems/eligibility

Simple if-else checks of the provided conditions

python eligibility/eligibility.py < eligibility/data/eligibility-01.in
"""

import sys
from datetime import datetime


def datetime_converter(date, format):
    # convert string to datetime object to compare dates
    return datetime.strptime(date, format)


DATE_FORMAT = "%Y/%m/%d"
POST_SECONDARY_DATE = "2010"
EXPECTED_POST_SECONDARY_DATE = datetime_converter(POST_SECONDARY_DATE, "%Y")
DATE_OF_BIRTH = "1991"
EXPECTED_DATE_OF_BIRTH = datetime_converter(DATE_OF_BIRTH, "%Y")
EXPECTED_COURSES = 40
ELIGIBLE = " eligible"
INELIGIBLE = " ineligible"
PETITION = " coach petitions"


def eligibility(name, study_date, date_birth, courses):
    study_date = datetime_converter(study_date, DATE_FORMAT)
    date_birth = datetime_converter(date_birth, DATE_FORMAT)
    courses = int(courses)

    if study_date >= EXPECTED_POST_SECONDARY_DATE:
        verification = name + ELIGIBLE
    elif date_birth >= EXPECTED_DATE_OF_BIRTH:
        verification = name + ELIGIBLE
    elif courses > EXPECTED_COURSES:
        verification = name + INELIGIBLE
    else:
        verification = name + PETITION

    return verification


if __name__ == "__main__":
    contestants = (n.strip().split() for n in sys.stdin.readlines()[1:])
    for contestant in contestants:
        print(eligibility(*contestant))
