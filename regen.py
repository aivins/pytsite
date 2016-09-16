file = open('import.txt')
last_date = None
last_time = None
for line in file:
    (date, time, cat, event, heat, more1, more2, notes) = line.split("\t")
    if not date or not time:
        continue
    if date != last_date:
        print(date+':')
        last_date = date
    if time != last_time:
        print('  "{}":'.format(time))
        last_time = time
    print("    - event: {}".format(event))
    if heat:
        print("      type: {}".format(heat))
    if cat:
        print("      cat: {}".format(cat))
    if notes:
        print("      notes: {}".format(notes))


file.close()