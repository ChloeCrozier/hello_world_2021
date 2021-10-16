

from flask import Flask
import os
app = Flask(__name__)
from flask import jsonify

def write(dictionary):
    @app.route('/numbers/')
    def print_list():
        return jsonify(dictionary)

    @app.route('/numbers/<string:stateName>/')
    def print_state(stateName):
        return jsonify(dictionary[stateName])
    if __name__ == '__main__':
        app.run()
    




def main():
    sNR = {}
    with open("solarRankings.txt","r") as solarRankings:
        for line in solarRankings:
            currentLineList = []
            line.strip("\n")
            lineDetails = line.split(",")
            currentLineList.append("Solar:")
            currentLineList.append(int(lineDetails[1]))
            sNR[lineDetails[0]] = currentLineList
    solarRankings.close()

    with open("hydroRankings.txt","r") as hydroRankings:
        for line in hydroRankings:
            line.strip("\n")
            lineDetails = line.split(",")
            sNR[lineDetails[0]].append("Hydro:")
            sNR[lineDetails[0]].append(int(lineDetails[1]))
    hydroRankings.close()
    
    with open("windRankings.txt","r") as windRankings:
        for line in windRankings:
            line.strip("\n")
            lineDetails = line.split(",")
            sNR[lineDetails[0]].append("Wind:")
            sNR[lineDetails[0]].append(int(lineDetails[1]))
    windRankings.close()
    print(sNR)
    
    sNRlistkeys = list(sNR.keys())
    sNRlistvalues = list(sNR.values())
    bestsNR = {}
    
    
    #What is the state best for code.
    for i in range(48):
        #If solar is the highest ranking
        if sNRlistvalues[i][1] <= sNRlistvalues[i][3]:
            if sNRlistvalues[i][1] <= sNRlistvalues[i][5]:
                bestsNR[sNRlistkeys[i]] = [sNRlistvalues[i][0],sNRlistvalues[i][1]];
             #else if Wind is the highest ranking
            else:
                bestsNR[sNRlistkeys[i]] = [sNRlistvalues[i][4],sNRlistvalues[i][5]];
        #else if Hydro is the highest ranking
        elif sNRlistvalues[i][3] < sNRlistvalues[i][1]:
            if sNRlistvalues[i][3] < sNRlistvalues[i][5]:
                bestsNR[sNRlistkeys[i]] = [sNRlistvalues[i][2],sNRlistvalues[i][3]];
            #else if Wind is the highest ranking
            else:
                bestsNR[sNRlistkeys[i]] = [sNRlistvalues[i][4],sNRlistvalues[i][5]];

    print(bestsNR)
    
    
    sNRP = {}
    with open("dataStuffPercentages.txt","r") as dataStuff:
        for line in dataStuff:
            line.strip("\n")
            lineDetails = line.split(",")
            lineDetails[3] = lineDetails[3].replace("\n","")
            lineDetails[3] = lineDetails[3].replace("%","")
            if float((lineDetails[3])) == -100:
                lineDetails[3] = "Invalid"
            else:
                lineDetails[3] = lineDetails[3]+"%"
            currentLineList = lineDetails[1:]
            currentLineList.insert(0, bestsNR[lineDetails[0]][0])
            currentLineList.insert(1, bestsNR[lineDetails[0]][1])
            sNRP[lineDetails[0]] = currentLineList
    write(sNRP)

main()





