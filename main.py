from zillow import ZillowData
from form_filler import FormFiller

zillow = ZillowData()
properties = zillow.property_dict

# # Testing form filler
# for i in range(1):
#     form_filler = FormFiller()
#     form_filler.fill_form(properties[i])


for i in range(len(properties)):
    form_filler = FormFiller()
    form_filler.fill_form(properties[i])




