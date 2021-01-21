from __future__ import unicode_literals
import frappe, json
from frappe.utils import cint

def update_picture_series_value(self,method):
    max_value=get_max_picture_series_value()
    for item in self.get('items'):
        if item.picture_series_cf==None:
            item.picture_series_cf=max_value
            max_value=max_value+1


def get_max_picture_series_value():
    picture_series_cf=frappe.db.sql("""select max(picture_series_cf) as max_value from `tabSales Invoice Item`""",as_dict=True)
    if picture_series_cf[0].max_value != None :
        max_value=cint(picture_series_cf[0].max_value)+1
    else:
        max_value=1001
    return max_value