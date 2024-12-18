from scrapy import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import re
from datetime import datetime, timedelta


def clean_input(value):
    value = value.strip()
    if value != '':
        return value
    return None

def convert_date(text):
    text = text.replace("Ngày đăng: ", "")
    today = datetime.today()
    
    if "Hôm nay" in text:
        return str(today.strftime('%d/%m/%Y'))
    
    elif "Hôm qua" in text:
        yesterday = today - timedelta(days=1)
        return str(yesterday.strftime('%d/%m/%Y'))
    
    else:
        return text


def get_number(text):
    numbers = re.findall(r'\d{1,3}', text)
    if numbers is not None:
        return numbers[0]
    
def TakeAll(lst):
    value = " ".join(text.strip() for text in lst)
    return value

class ApartmentItem(Item):
    id = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    url = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    title = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    # description = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    price = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    price_per_area = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    area = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    type = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    bedrooms = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    bathrooms = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    address = Field(input_processor=MapCompose(clean_input), output_processor=Join(separator=", "))
    # floor = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    # kitchen = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    direction = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    furniture = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    utilities = Field(input_processor=MapCompose(clean_input), output_processor=Join(separator=", "))
    # investor = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    # parking_lot = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    law_doc = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    project = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    # entrance = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
    post_date = Field(input_processor=MapCompose(clean_input), output_processor=TakeFirst())
