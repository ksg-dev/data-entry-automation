from zillow import ZillowData
from form_filler import FormFiller

zillow = ZillowData()
properties = zillow.property_dict

# # Testing form filler
# for i in range(1):
#     form_filler = FormFiller()
#     form_filler.fill_form(properties[i])

form_count = 1
for i in range(len(properties)):
    print(f"Filling form {form_count} of {len(properties)}...")
    form_filler = FormFiller()
    form_filler.fill_form(properties[i])




