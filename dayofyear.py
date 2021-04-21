def translate_date(data):
    data = str(data)
    year = data[:4]
    days = data[4:]

    months = {
        "january":    "01:001,031",
        "february":   "02:032,060",
        "march" :     "03:061,091",
        "april" :     "04:092,121",
        "may" :       "05:122,152",
        "june" :      "06:153,182",
        "july" :      "07:183,213",
        "august" :    "08:214,244",
        "september" : "09:245,274",
        "october" :   "10:275,305",
        "november" :  "11:306,355",
        "december" :  "12:336,366"
             }
    if int(year) % 4 == 0:
        print("Leap year")
        for x, y in months.items():
            if int(days) >= int(y[3:6]) and int(days) <= int(y[7:]):
                day = int(days) - (int(y[3:6]) - 1)
                if day >= 10:
                    print(f"{year}{y[0:2]}{day}")
                else:
                    print(f"{year}{y[0:2]}0{day}")

    else:
        print("Normal year")
        if int(days) > 59:
            for x, y in months.items():
                if int(days) >= int(y[3:6])-1 and int(days) <= int(y[7:])-1:
                    day = int(days) - (int(y[3:6]) - 2)
                    if day >= 10:
                        print(f"{year}{y[0:2]}{day}")
                    else:
                        print(f"{year}{y[0:2]}0{day}")
        else:
            for x, y in months.items():
                if int(days) >= int(y[3:6]) and int(days) <= int(y[7:]):
                    day = int(days) - (int(y[3:6]) - 1)
                    if day >= 10:
                        print(f"{year}{y[0:2]}{day}")
                    else:
                        print(f"{year}{y[0:2]}0{day}")
translate_date(200046)




