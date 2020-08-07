import csv


def write_obj(writer, obj, prefix=None):

    if "cust_s" in obj.keys():
        customers = obj["cust_s"]
        customers_out = obj["cust_a"]["val"]
        percent_out = obj["percent_out"]
        area_name = obj["area_name"]

        if prefix is not None:
            prefix = f"{prefix}-{area_name}"
        else:
            prefix = area_name

        writer.writerow({
            'area_name': area_name, 
            'customers': customers,
            'customers_out': customers_out, 
            'percent_out': percent_out})

    if ("areas" in obj.keys()):
        for child in obj["areas"]:
            write_obj(writer, child, prefix=prefix)


def convert(obj, out_file):
    with open(out_file, 'w', newline='') as csvfile:
        fieldnames = ['area_name', 'customers', 'customers_out', 'percent_out']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        write_obj(writer, obj["file_data"])

# import json
# convert(json.loads(open("out/conn-1596784408984.json").read()), "conn-test.csv")