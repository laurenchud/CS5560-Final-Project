def parse_dataset(parsed_dataset, file, devices, vendors):
    # banner filtering
    fillers = ["html", "head", "title", "content", "charset", "script", "verdana", "arial", "helvetica", "sans-serif",
               "function", "font-family", "font-size", "font-weight", "return", "doctype", "public", "page", "meta",
               "text",
               "xhtml", "strstyle"]
    punctuation = ["{", "}", "[", "]", "/", "=", ";", ":", "<", ">", ",", "!", "#"]

    # import the banner data
    bannerfile = open(file, "r")
    lines = bannerfile.readlines()
    blogged = False  # remove this for all IPs
    ipsfound = False
    dtfound = False
    vfound = False
    pfound = False

    for line in lines:
        spl = line.split()
        if spl[0] == '"type":':
            btype = spl[1]
            btype = btype[:-1]
        elif ipsfound == True:
            ip = spl[0]
            if ip[len(ip) - 1] == ',':
                ip = ip[:-1]
            ipsfound = False
        elif dtfound == True:
            devicetype = ""
            for dtel in range(len(spl)):
                devicetype = devicetype + spl[dtel] + " "
            devicetype = devicetype[:-1]
            devicetype = devicetype[1:-1]
            if devicetype in devices:
                dtfound = False
            else:
                devices.append(devicetype)
            dtfound = False
        elif vfound == True:
            vendor = ""
            for vel in range(len(spl)):
                vendor = vendor + spl[vel] + " "
            vendor = vendor[:-1]
            vendor = vendor[1:-1]
            if vendor in vendors:
                vfound = False
            else:
                vendors.append(vendor)
            vfound = False
        elif pfound == True:
            product = ""
            for pel in range(len(spl)):
                product = product + spl[pel] + " "
            product = product[:-1]
            pfound = False
            # make tuple since product is last argument
            if blogged == False:  # remove this for all IPs
                bannerarg = [btype, banner.lower(), ip, devicetype.lower(), vendor.lower(), product.lower()]
                parsed_dataset.append(bannerarg)
                btype = ""
                banner = ""
                ip = ""
                devicetype = ""
                vendor = ""
                product = ""
                blogged = True  # remove this for all IPs
        elif spl[0] == '"banner":':
            banner = ""
            for bel in range(len(spl) - 1):
                banner = banner + spl[bel + 1] + " "
            banner = banner[:-1]
            if banner[len(banner) - 1] == ',':
                banner = banner[:-1]
            blogged = False  # remove this for all IPs
        elif spl[0] == '"ips":':
            ipsfound = True
        elif spl[0] == '"deviceTypes":':
            dtfound = True
        elif spl[0] == '"vendor":':
            vfound = True
        elif spl[0] == '"product":':
            pfound = True

    bannerfile.close()