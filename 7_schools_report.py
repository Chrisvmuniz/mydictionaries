"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
"Graduation rate  women (DRVGR2020)": 67
Display report for all universities that have a total price for in-state students living off campus over $50,000
"Total price for out-of-state students living on campus 2020-21 (DRVIC2020)": 53672,

"NCAA": {
      "NAIA member for football (IC2020)": 1,
      "NAIA conference number football (IC2020)": 132

"""
import json

infile = open ("school_data.json",'r')
schools = json.load(infile)
conference_schls = [372, 108, 107, 130]
print(type(schools))

howManySchools = len(schools)
print("ACC, Big 12, Big Ten, Pac-12 and SEC divison schools: \n")
for x in schools:
    for y in conference_schls:
        if int(x["NCAA"]["NAIA conference number football (IC2020)"]) == y:
            print(x["instnm"] + " : " + str(x["NCAA"]["NAIA conference number football (IC2020)"]))
        if int(x["Graduation rate  women (DRVGR2020)"]) > 50:
            print("Graduation rate above 50% : " + str(x["Graduation rate  women (DRVGR2020)"]))
        if int(x["Total price for out-of-state students living on campus 2020-21 (DRVIC2020)"]) > 50000:
            print("Off campus tuition over $50,000 : " + str(x["Total price for out-of-state students living on campus 2020-21 (DRVIC2020)"]))



