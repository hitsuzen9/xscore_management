import click
import frappe
from frappe import _
import json

@click.command('set-test')
# @click.argument('email')

def set_test():
    frappe.init(site='site2name.local')
    frappe.connect()

    try:
        json_array = frappe.get_file_json('/var/www/Test_f/frappe-bench/apps/xscore_management/xscore_management/files/doctype.json')

        names_with_data = []
        for item in json_array:
            name = item['name']

            if frappe.get_meta(name).issingle:
                # if frappe.db.exists('Singles', {'doctype': name}):
                names_with_data.append(name)
            else:
                data = frappe.get_all(name, fields=["name"])
                if data:
                    names_with_data.append(name)

        with open('/var/www/Test_f/frappe-bench/apps/xscore_management/xscore_management/files/test1.json', 'w') as f:
            json.dump(names_with_data, f, indent=4)

        print('ok')
    finally:
        frappe.destroy()
    

commands = [
    set_test
]