from struct import pack

import customtkinter
import PersonalClass
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=80, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Installment check")
label.pack(pady=12, padx=200)

name = customtkinter.CTkEntry(master=frame, placeholder_text="Name")
name.pack(pady=12, padx=20)

idno = customtkinter.CTkEntry(master=frame, placeholder_text="ID-NO")
idno.pack(pady=12, padx=20)

vehicletype = customtkinter.CTkEntry(master=frame, placeholder_text="vehicle Type")
vehicletype.pack(pady=12, padx=20)

credit = customtkinter.CTkEntry(master=frame, placeholder_text="Credit Score category : ")
credit.pack(pady=12, padx=20)


carextras = customtkinter.CTkEntry(master=frame, placeholder_text="Car Extras: ")
carextras.pack(pady=12, padx=20)


#Creating a Dictionary and storing it into the JSON FILE
def storeDetails():

    obj1 = PersonalClass.PersonalClass(name, idno, vehicletype, carextras, credit)

    PurchaseDetails = {
        "name": obj1.getName(),
        "idno": obj1.getID(),
        "Vehicletype": obj1.getVehicleType(),
        "creditscore": obj1.hasCreditScore(),
        "carExtras": obj1.getExtr()
    }

    with open('C:/Users/sifiso/Desktop/Python Tutorial/File Handling/Project File '
              'Handling/PersonaleDeatails/PersonalDetails.JSON', 'w',encoding='utf-8') as file:
        json.dump(PurchaseDetails, file, ensure_ascii=False, indent=4)


#end OF Writing to  JSON FILE
button = customtkinter.CTkButton(master=frame, text="Process", command=storeDetails)
button.pack(pady=12, padx=20)
root.mainloop()
