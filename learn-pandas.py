# install pandas in terminal
# pip3 install panda

import pandas as pd

# data read from csv file
# Encoding মানে কী?
# কম্পিউটার ফাইলে সবকিছু byte হিসেবে সেভ করে।
# যখন আমরা টেক্সট (অক্ষর) পড়তে চাই, তখন byte গুলোকে আবার অক্ষরে রূপান্তর করতে হয়। এই রূপান্তরের নিয়মকেই বলে encoding।
# সবচেয়ে জনপ্রিয় দুটি encoding:

# UTF-8 → আধুনিক স্ট্যান্ডার্ড (বাংলা, হিন্দি, চাইনিজ, ইমোজি সবকিছু সাপোর্ট করে)
# latin1 (ISO-8859-1) → পুরোনো স্ট্যান্ডার্ড, শুধু পশ্চিম ইউরোপীয় ভাষা (ইংরেজি + ফরাসি, স্প্যানিশ, জার্মান ইত্যাদির অ্যাকসেন্ট সহ অক্ষর) সাপোর্ট করে।
# df = pd.read_excel("D:\ml_al_projects\machine_learning_AI\pandas_learn\SampleSuperstore.xlsx")


df = pd.read_csv("sales_data_sample.csv" ,encoding="latin1")
print(df)