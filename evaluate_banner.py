# the purpose of this file is to take an input of a training set, a parsed dataset, and a predefined list of devices and vendors in order
# to output key words from the current banner being processed

import requests
import time
import string

from make_guess import make_guess

def evaluate_banner(trainingsetnum, numofbannertests, parsed_dataset, result_dataset, devices, vendors, products,
                    training_set):
    # iterate through each banner to parse into usable search queries
    for entry in range(numofbannertests):
        resultdevice = ""
        resultvendor = ""
        resultproduct = ""
        if parsed_dataset[entry][0] == '"HTTP"':
            httpbanner = parsed_dataset[entry][1].lower()
            deviceinbanner = False
            vendorinbanner = False
            productinbanner = False
            # for dev in devices:
            #     if dev.lower() in httpbanner:
            #         deviceinbanner = True
            #         resultdevice = dev
            # for ven in vendors:
            #     if ven.lower() in httpbanner:
            #         vendorinbanner = True
            #         resultvendor = ven
            for pro in products:
                if pro.lower() in httpbanner:
                    productinbanner = True
                    resultproduct = pro
            # httpbanner = httpbanner.lower()
            # # eliminate banner fillers
            # httpbanner = httpbanner.strip()
            # for filler in fillers:
            #     httpbanner = httpbanner.replace(filler, "")
            # for punct in punctuation:
            #     httpbanner = httpbanner.replace(punct, "")
            # httpbanner = httpbanner[1:20]
            # httpbannersplit = httpbanner.split()
            # httpurl = "https://www.google.com/search?q="
            # for x in range(len(httpbannersplit)):
            #     httpurl = httpurl + httpbannersplit[x]
            #     httpurl = httpurl + "+"
            #     httpurl = httpurl[:-1]
            # # perform internet searches with web crawler
            # httppage = requests.get(httpurl)
            # httptxt = httppage.text.lower()
            # # see if device type is present in html
            # for dev in devices:
            #     if dev.lower() in httptxt:
            #         resultdevice = dev
            # # see if vendor is present in html
            # for ven in vendors:
            #     if ven.lower() in httptxt:
            #         resultvendor = ven
        elif parsed_dataset[entry][0] == '"FTP"':
            splitbanner = parsed_dataset[entry][1].lower()
            deviceinbanner = False
            vendorinbanner = False
            productinbanner = False
            for dev in devices:
                if dev.lower() in splitbanner:
                    deviceinbanner = True
                    resultdevice = dev
            for ven in vendors:
                if ven.lower() in splitbanner:
                    vendorinbanner = True
                    resultvendor = ven
            for pro in products:
                if pro.lower() in splitbanner:
                    productinbanner = True
                    resultproduct = pro
            # ftpurl = "https://www.google.com/search?q="
            # wordsplitbanner = splitbanner.split()
            # for x in range(len(wordsplitbanner)):
            #     ftpurl = ftpurl + wordsplitbanner[x]
            #     ftpurl = ftpurl + "+"
            # ftpurl = ftpurl[:-1]
            # # perform internet searches with web crawler
            # ftppage = requests.get(ftpurl)
            # htmltxt = ftppage.text.lower()
            # # see if device type is present in html
            # for dev in devices:
            #     if dev.lower() in htmltxt and not deviceinbanner:
            #         resultdevice = dev
            # # see if vendor is present in html
            # for ven in vendors:
            #     if ven.lower() in htmltxt and not vendorinbanner:
            #         resultvendor = ven
            # for prod in products:
            #     if prod.lower() in htmltxt and not productinbanner:
            #        resultproduct = prod
        elif parsed_dataset[entry][0] == '"TELNET"':
            telnetbanner = parsed_dataset[entry][1].lower()
            deviceinbanner = False
            vendorinbanner = False
            productinbanner = False
            for dev in devices:
                if dev.lower() in telnetbanner:
                    deviceinbanner = True
                    resultdevice = dev
            for ven in vendors:
                if ven.lower() in telnetbanner:
                    vendorinbanner = True
                    resultvendor = ven
            for pro in products:
                if pro.lower() in telnetbanner:
                    productinbanner = True
                    resultproduct = pro
            # tsplitbanner = telnetbanner.split()
            # turl = "https://www.google.com/search?q="
            # for x in range(len(tsplitbanner)):
            #     turl = turl + tsplitbanner[x]
            #     turl = turl + "+"
            #     turl = turl[:-1]
            # # perform internet searches with web crawler
            # tpage = requests.get(turl)
            # teltxt = tpage.text.lower()
            # # see if device type is present in html
            # for dev in devices:
            #     if dev.lower() in teltxt and not deviceinbanner:
            #         resultdevice = dev
            # # see if vendor is present in html
            # for ven in vendors:
            #     if ven.lower() in teltxt and not vendorinbanner:
            #         resultvendor = ven
            # for prod in products:
            #     if prod.lower() in teltxt and not productinbanner:
            #         resultproduct = prod
        # ML algorithm for result product calculation
        resultentry = [parsed_dataset[entry][0], parsed_dataset[entry][1], parsed_dataset[entry][2], resultdevice,
                       resultvendor, resultproduct]
        result = make_guess(resultentry, training_set)
        result_dataset.append(result)
        # establish a timeout to not overload the requests
        # time.sleep(1)
