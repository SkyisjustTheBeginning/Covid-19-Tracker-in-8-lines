from covid import *
Handle = Covid()
target = str(input("Country : "))
info = Handle.get_status_by_country_name(target)
print("Confirmed : " , info.get('confirmed'))
print("Active : " , info.get('active'))
print("Deaths : " , info.get("deaths"))
print("ID : " , info.get("id"))