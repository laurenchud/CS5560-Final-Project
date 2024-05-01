# machine learning algorithm
def make_guess(list, training):
    # list has form [type, banner, ip, device, vendor, product]
    # training is a list of [type, device, vendor, product, 1]
    entrydata = [list[0].lower(), list[1].lower(), list[2].lower(), list[3].lower(), list[4].lower(), list[5].lower()]
    maximum_element = ["", "", "", "", 0]
    max_across_all = ["", "", "", "", 0]
    # find the most common entry based on the current key words
    for tr in training:
        if tr[0] == entrydata[0]:
            if tr[4] > max_across_all[4]:
                max_across_all = tr
    if entrydata[3] == "" and entrydata[4] == "" and entrydata[5] == "":
        for a in training:
            if a[0] == entrydata[0]:
                if a[4] > maximum_element[4]:
                    maximum_element = a
    elif entrydata[3] == "" and entrydata[4] == "":
        for b in training:
            if b[0] == entrydata[0] and b[3] == entrydata[5]:
                if b[4] > maximum_element[4]:
                    maximum_element = b
    elif entrydata[3] == "" and entrydata[5] == "":
        for c in training:
            if c[0] == entrydata[0] and c[2] == entrydata[4]:
                if c[4] > maximum_element[4]:
                    maximum_element = c
    elif entrydata[4] == "" and entrydata[5] == "":
        for d in training:
            if d[0] == entrydata[0] and d[1] == entrydata[3]:
                if d[4] > maximum_element[4]:
                    maximum_element = d
    elif entrydata[3] == "":
        for e in training:
            if e[0] == entrydata[0] and e[2] == entrydata[4] and e[3] == entrydata[5]:
                if e[4] > maximum_element[4]:
                    maximum_element = e
    elif entrydata[4] == "":
        for f in training:
            if f[0] == entrydata[0] and f[1] == entrydata[3] and f[3] == entrydata[5]:
                if f[4] > maximum_element[4]:
                    maximum_element = f
    elif entrydata[5] == "":
        for g in training:
            if g[0] == entrydata[0] and g[1] == entrydata[3] and g[2] == entrydata[4]:
                if g[4] > maximum_element[4]:
                    maximum_element = g
    else:
        maximum_element = [entrydata[0], entrydata[3], entrydata[4], entrydata[5], 0]
    if maximum_element[0] == "":
        maximum_element[0] = entrydata[0]
    if maximum_element[1] == "":
        if entrydata[3] == "":
            maximum_element[1] = max_across_all[1]
        else:
            maximum_element[1] = entrydata[3]
    if maximum_element[2] == "":
        if entrydata[4] == "":
            maximum_element[2] = max_across_all[2]
        else:
            maximum_element[2] = entrydata[4]
    if maximum_element[3] == "":
        if entrydata[5] == "":
            maximum_element[3] = max_across_all[3]
        else:
            maximum_element[3] = entrydata[5]

    prediction = [maximum_element[0], list[1], list[2], maximum_element[1], maximum_element[2], maximum_element[3]]
    return prediction
