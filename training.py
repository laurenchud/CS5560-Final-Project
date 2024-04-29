def training(trainingsetnum, parsed_dataset, training_set, products):
    # establish training set
    for trelement in range(trainingsetnum):
        trtype = parsed_dataset[0][0].lower()
        trdevice = parsed_dataset[0][3].lower()
        trvendor = parsed_dataset[0][4].lower()
        trproduct = parsed_dataset[0][5].lower()
        products.append(trproduct[1:-1].lower())
        trtuple = [trtype, trdevice, trvendor, trproduct, 1]
        entryfound = False
        if trelement == 0:
            training_set.append(trtuple)
        else:
            for el in training_set:
                if el[0] == trtype and el[1] == trdevice and el[2] == trvendor and el[3] == trproduct:
                    newel = el[4] + 1
                    el[4] = newel
                    entryfound = True
            if not entryfound:
                training_set.append(trtuple)
        parsed_dataset.remove(parsed_dataset[0])
