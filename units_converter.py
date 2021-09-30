converter={'pressure': {'bar':{'Pa':100000, 'kgf/cm2':1/0.980665},
                      'Pa':{'bar': 1/1000000, 'kgf/cm2':1/980665},
                      'kgf/cm2':{'bar':0.980665, 'Pa':980665}},
           'speed': {'km/h':{'mph':1/1.852, 'm/s':0.278},
                   'mph':{'km/h':1.852, 'm/s':0.514},
                   'm/s':{'km/h':1/0.278, 'mph':1/0.514}},
           'radioactivity': {'Bq':{'mCi':1/3700000, 'dpm':60},
                           'mCi':{'Bq':3700000, 'dpm':222000000},
                           'dpm':{'Bq':1/60, 'mCi':1/222000000}}}
while True:
    print("Enter type of physical value")
    phys = str(input())
    if phys == "end":
        print("Good luck!")
        break
    else:
        while True:
            print("Enter original units")
            a_units = str(input())
            print("Enter required units")
            b_units = str(input())
            print("Enter number")
            number = float(input())
            print(converter[phys][a_units][b_units]*number, b_units, sep=' ')
            break