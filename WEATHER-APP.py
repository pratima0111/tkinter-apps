from tkinter import *
import requests
import json
root = Tk()
root.title('WEATHER_APP')
root.geometry('600x100')

def zipLookup():
   # zip.get()
    #zipLabel =Label(root, text=zip.get())
    #zipLabel.grid(row=1, colomn=1, columnspan=2)

    #try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zip.get()+"&distance=5&API_KEY=2054729A-FCA3-4262-86AF-62ECA1B5CEF3")
    api = json.loads(api_request.content)  # json converts the data collected from api request to a python list
    city = api[0]["ReportingArea"]       # simply calling the different dictionary elements froma big list of 3 dict
    quality = api[0]["AQI"]
    category = api[0]['Category']['Name']

    if category == 'Good':
        weather_color = "#0C0"
    elif category == 'Moderate':
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000"

    root.configure(background=weather_color)

    my_lbl = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 16),background=weather_color)
    my_lbl.grid(row=1, column=0, columnspan=2)

    #except Exception as e:
     #   api = "Error..."


#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=~zipCode~&distance=5&API_KEY=2054729A-FCA3-4262-86AF-62ECA1B5CEF3

zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton=Button(root, text="LookUp Zip", command= zipLookup)
zipButton.grid(row=0 ,column=1, sticky=W+E+N+S)
root.mainloop()


