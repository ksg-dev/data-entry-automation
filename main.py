from zillow import ZillowData
# from form-filler import FormFiller

zillow = ZillowData()
properties = zillow.property_dict

for i in range(len(properties)):
    address = properties[i]["address"]
    print(address)



