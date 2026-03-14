import pandas as pd

# raw dataset toiri kora
data = {
    "Name": [
        "Aman","Priya","Rahul","Anjali","Ravi","Meera","Arjun","Neha","Imran",
        "Sneha","Raj","Divya","Kabir","Simran","Karan","Pooja","Rakesh",
        "Isha","Rohit","Deepa"
    ],

    "Gender": [
        "Male","Female","Male","Female","Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female","Male","Female","Male",
        "Female","Male","Female"
    ],

    "City": [
        "Delhi","Mumbai","Bangalore","Mumbai","Delhi","Chennai","Bangalore",
        "Delhi","Chennai","Mumbai","Chennai","Delhi","Mumbai","Bangalore",
        "Delhi","Mumbai","Chennai","Delhi","Delhi","Bangalore"
    ],

    "Passed": [
        "Yes","Yes","No","Yes","Yes","No","Yes","Yes","No","Yes",
        "Yes","No","Yes","Yes","No","Yes","Yes","No","Yes","Yes"
    ]
}
df = pd.DataFrame(data)
print(df)

# for excel sheet
# df.to_excel("out.xlsx", index=False) 

df.to_csv("output.csv", index=False) 
# unnecessary column remove kore index false use korle