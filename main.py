# Classifying Banner Data
# Lauren Chuderewicz and Amanda Ross

# this file runs the training and testing and prints the results to the console

from make_guess import make_guess
from parse_dataset import parse_dataset
from training import training
from evaluate_banner import evaluate_banner

import requests
import time
import string

# initialize important variables
parsed_dataset = []  # list of tuples with banner type, banner, device type, vendor, and product
result_dataset = []  # list of tuples with banner type, banner, and predicted device type, vendor, and product
training_set = []  # list of training data
devices = []  # list of known device types
vendors = []  # list of known vendors
products = []  # generate a list of products as module trains

# change this to add more or less training
trainingsetnum = 4000
# change this to add more or less tests
numofbannertests = 919

# parse the input dataset
parse_dataset(parsed_dataset, "banners.txt", devices, vendors)

# train the algorithm
training(trainingsetnum, parsed_dataset, training_set, products)

# evaluate the banners
evaluate_banner(trainingsetnum, numofbannertests, parsed_dataset, result_dataset, devices, vendors, products,
                    training_set)

# compare result tuple list and original tuple list for results
correctdt = 0
correctv = 0
correctp = 0
totcorrect = 0
wrongdt = 0
wrongv = 0
wrongp = 0
totwrong = 0
httpcorrect = 0
httpwrong = 0
ftpcorrect = 0
ftpwrong = 0
telnetcorrect = 0
telnetwrong = 0
tuplecorrect = 0
# remove any apostrophes to keep names consistent 
for count in range(numofbannertests):
    if parsed_dataset[count][3][0] == '"':
        parsed_dataset[count][3] = parsed_dataset[count][3][1:]
    if parsed_dataset[count][3][len(parsed_dataset[count][3])-1] == '"':
        parsed_dataset[count][3] = parsed_dataset[count][3][:-1]
    if parsed_dataset[count][4][0] == '"':
        parsed_dataset[count][4] = parsed_dataset[count][4][1:]
    if parsed_dataset[count][4][len(parsed_dataset[count][4])-1] == '"':
        parsed_dataset[count][4] = parsed_dataset[count][4][:-1]
    if parsed_dataset[count][5][0] == '"':
        parsed_dataset[count][5] = parsed_dataset[count][5][1:]
    if parsed_dataset[count][5][len(parsed_dataset[count][5])-1] == '"':
        parsed_dataset[count][5] = parsed_dataset[count][5][:-1]

    if result_dataset[count][3][0] == '"':
        result_dataset[count][3] = result_dataset[count][3][1:]
    if result_dataset[count][3][len(result_dataset[count][3])-1] == '"':
        result_dataset[count][3] = result_dataset[count][3][:-1]
    if result_dataset[count][4][0] == '"':
        result_dataset[count][4] = result_dataset[count][4][1:]
    if result_dataset[count][4][len(result_dataset[count][4])-1] == '"':
        result_dataset[count][4] = result_dataset[count][4][:-1]
    if result_dataset[count][5][0] == '"':
        result_dataset[count][5] = result_dataset[count][5][1:]
    if result_dataset[count][5][len(result_dataset[count][5])-1] == '"':
        result_dataset[count][5] = result_dataset[count][5][:-1]
# compare device type
    if parsed_dataset[count][3].lower() == result_dataset[count][3].lower():
        correctdt = correctdt + 1
        if parsed_dataset[count][0] == '"HTTP"':
            httpcorrect = httpcorrect + 1
        elif parsed_dataset[count][0] == '"FTP"':
            ftpcorrect = ftpcorrect + 1
        elif parsed_dataset[count][0] == '"TELNET"':
            telnetcorrect = telnetcorrect + 1
    else:
        wrongdt = wrongdt + 1
        if parsed_dataset[count][0] == '"HTTP"':
            httpwrong = httpwrong + 1
        elif parsed_dataset[count][0] == '"FTP"':
            ftpwrong = ftpwrong + 1
        elif parsed_dataset[count][0] == '"TELNET"':
            telnetwrong = telnetwrong + 1
    # compare vendor
    if parsed_dataset[count][4].lower() == result_dataset[count][4].lower():
        correctv = correctv + 1
        if parsed_dataset[count][0] == '"HTTP"':
            httpcorrect = httpcorrect + 1
        elif parsed_dataset[count][0] == '"FTP"':
            ftpcorrect = ftpcorrect + 1
        elif parsed_dataset[count][0] == '"TELNET"':
            telnetcorrect = telnetcorrect + 1
    else:
        wrongv = wrongv + 1
        if parsed_dataset[count][0] == '"HTTP"':
            httpwrong = httpwrong + 1
        elif parsed_dataset[count][0] == '"FTP"':
            ftpwrong = ftpwrong + 1
        elif parsed_dataset[count][0] == '"TELNET"':
            telnetwrong = telnetwrong + 1
    # compare product
    if parsed_dataset[count][5].lower() == result_dataset[count][5].lower():
        correctp = correctp + 1
        if parsed_dataset[count][0] == '"HTTP"':
            httpcorrect = httpcorrect + 1
        elif parsed_dataset[count][0] == '"FTP"':
            ftpcorrect = ftpcorrect + 1
        elif parsed_dataset[count][0] == '"TELNET"':
            telnetcorrect = telnetcorrect + 1
    else:
        wrongp = wrongp + 1
        if parsed_dataset[count][0] == '"HTTP"':
            httpwrong = httpwrong + 1
        elif parsed_dataset[count][0] == '"FTP"':
            ftpwrong = ftpwrong + 1
        elif parsed_dataset[count][0] == '"TELNET"':
            telnetwrong = telnetwrong + 1
    # assess if entire tuple is correct
    if parsed_dataset[count][5].lower() == result_dataset[count][5].lower() and \
            parsed_dataset[count][4].lower() == result_dataset[count][4].lower() and \
            parsed_dataset[count][3].lower() == result_dataset[count][3].lower():
        tuplecorrect = tuplecorrect + 1

totcorrect = correctdt + correctv + correctp
totwrong = wrongdt + wrongv + wrongp

# print results to console
if totcorrect == 0:
    print("NONE CORRECT :(")
else:
    pcdt = correctdt / totcorrect
    pcdt = "{:.2f}".format(pcdt)
    pwdt = wrongdt / totwrong
    pwdt = "{:.2f}".format(pwdt)
    pcv = correctv / totcorrect
    pcv = "{:.2f}".format(pcv)
    pwv = wrongv / totwrong
    pwv = "{:.2f}".format(pwv)
    pcp = correctp / totcorrect
    pcp = "{:.2f}".format(pcp)
    pwp = wrongp / totwrong
    pwp = "{:.2f}".format(pwp)
    percentcorrect = totcorrect * 100 / (totcorrect + totwrong)
    pc = "{:.2f}".format(percentcorrect)
    percentwrong = totwrong * 100 / (totcorrect + totwrong)
    pw = "{:.2f}".format(percentwrong)
    hc = httpcorrect / totcorrect
    hc = "{:.2f}".format(hc)
    hw = httpwrong / totwrong
    hw = "{:.2f}".format(hw)
    fc = ftpcorrect / totcorrect
    fc = "{:.2f}".format(fc)
    fw = ftpwrong / totwrong
    fw = "{:.2f}".format(fw)
    tc = telnetcorrect / totcorrect
    tc = "{:.2f}".format(tc)
    tw = telnetwrong / totwrong
    tw = "{:.2f}".format(tw)
    print("# of Banners tested: ", numofbannertests)
    print("% correct: ", pc, "%")
    print("% wrong: ", pw, "%")
    print(" ")
    print("% correct that are Device Types: ", pcdt)
    print("num correct ", correctdt)
    print("% correct that are Vendors: ", pcv)
    print("num correct ", correctv)
    print("% correct that are Products: ", pcp)
    print("num correct ", correctp)
    print("% wrong that are Device Types: ", pwdt)
    print("num wrong ", wrongdt)
    print("% wrong that are Vendors: ", pwv)
    print("num wrong ", wrongv)
    print("% wrong that are Products: ", pwp)
    print("num wrong ", wrongp)
    print(" ")
    print("% correct that are HTTP: ", hc)
    print("num correct ", httpcorrect)
    print("% correct that are FTP: ", fc)
    print("num correct ", ftpcorrect)
    print("% correct that are TELNET: ", tc)
    print("num correct ", telnetcorrect)
    print("% wrong that are HTTP: ", hw)
    print("num wrong ", httpwrong)
    print("% wrong that are FTP: ", fw)
    print("num wrong ", ftpwrong)
    print("% wrong that are TELNET: ", tw)
    print("num wrong ", telnetwrong)
    print(" ")
    print("percent tuple: ", tuplecorrect*100/919)
