import pandas as pd
from .models import Category, SubCategory, EverydaySpendingING
import os
import datetime
#from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


file_path = os.path.join(BASE_DIR, 'sample.xls')


def parse_categories(cat_name, sub_name):
    # Category
    if not type(cat_name) == unicode:
        category = None
    else:
        category_name = cat_name.replace(' ', '_').lower()
        try:
            category = Category.objects.get(name=category_name)
        except:
            category = Category(name=category_name)
            category.save()
        # Search for category:
    # SubCategory:
    if not type(sub_name) == unicode:
        subcategory = None
    else:
        subcategory_name = sub_name.replace(' ', '_').lower()
        try:
            subcategory = SubCategory.objects.get(name=subcategory_name)
        except:
            subcategory = SubCategory(name=subcategory_name, category=category)
            subcategory.save()
    return category, subcategory


def parse_row(row):
    # Category
    date = row[0]
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    print(date)
    cat_name = row[1]
    sub_name = row[2]
    description = row[3]
    amount = row[6]
    credit = row[7]
    category, subcategory = parse_categories(cat_name, sub_name)
    spending=EverydaySpendingING(date=date,
                                 category=category,
                                 sub_category=subcategory,
                                 amount=amount,
                                 account_credit=float(credit),)
    spending.save()

def parse_ing_csv(file_path):
    df = pd.read_excel(file_path)
    df.fillna('missing')
    for index, row in df.iterrows():
        parse_row(row)
        print(index)

parse_ing_csv(file_path)
