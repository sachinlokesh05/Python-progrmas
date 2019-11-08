import json

# json function is created
def json_inventory():
    with open("Inventroy.json", "r") as f:  # json file is loaded in dict format
        data = json.load(f)
        # print(data)

    wheatinvent = 0
    pulseinvent = 0

    riceinvent = 0
    try:  # try exception is used id data is not present in the inventory
        total1=0
        total2=0
        total3=0
        # to file data in each inventory
        for i in data["Rice"]:
            # for price in i:
            riceinvent = i["price per kg"]*i["weight"]
            print("total",i["name"],"is : ",riceinvent,"kg")
            total1 +=riceinvent # data is incremented
        print()

        for i in data["wheat"]:
            # for price in i:
                wheatinvent = i["price per kg"]*i["weight"]
                total2 +=wheatinvent
                # data is incremented
                print("total",i["name"],"is :",wheatinvent,"kg")
        print()
        for i in data["pulses"]:
            # for price in i:
                pulseinvent = i["price per kg"]*i["weight"] # data is incremented
                total3 +=pulseinvent
                print("total",i["name"],"is : ",pulseinvent,"kg")
        print()
    except TypeError:
        print(" there is type error ")

    print("""total value for rice in inventory is {} rs,\ntotal value for wheat in inventory is {} rs,
total value for pulse in inventory is {} rs""".format(total1 , total2, total3))

    dump = json.dumps("Inventroy.json")
    print(dump)

# main function is created and called
if __name__ == '__main__':
    json_inventory()