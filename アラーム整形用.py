import pandas as pd
import re
import csv
import tkinter

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

df = pd.read_csv("D:自作/fortigate.csv",names=["rows"])

#「"」で囲まれているデータは「＊＊＊="([^"]*)"\s+」で抽出
#その他は、「time=(.*?)\s+'」で抽出

df["date"]=df["rows"].str.extract(r'date=(.*?)\s+')
df["time"]=df["rows"].str.extract(r'time=(.*?)\s+')

df["type"]=df["rows"].str.extract(r'type="([^"]*)"\s+')
df["level"]=df["rows"].str.extract(r'level="([^"]*)"\s+')
df["attack"]=df["rows"].str.extract(r'attack="([^"]*)"\s+')
df["msg"]=df["rows"].str.extract(r'msg="([^"]*)"\s+')
df["action"]=df["rows"].str.extract(r'action="([^"]*)"\s+')
df["srcip"]=df["rows"].str.extract(r'srcip=(.*?)\s+')
df["srcport"]=df["rows"].str.extract(r'srcport=(.*?)\s+')
df["dstip"]=df["rows"].str.extract(r'dstip=(.*?)\s+')
df["dstport"]=df["rows"].str.extract(r'dstport=(.*?)\s+')
df["ref"]=df["rows"].str.extract(r'ref="([^"]*)"\s+')

df["datetime"] = pd.to_datetime(df["date"]+"T"+df["time"])
df["datetime"] = df["datetime"].dt.strftime('%Y/%m/%d %H:%M:%S')
df["route"] = df["srcip"]+"→"+df["dstip"]+"(port:"+df["dstport"]+")"
df["srcip_unique"] = df["route"].str.extract(r'(.*?)→')
df["dstip_unique"] = df["route"].str.extract(r'→(.*?\(port:.*?\))')

print("■日時")
min_date = str(df['datetime'].min())[:10]
max_date = str(df['datetime'].max())[:10]

if max_date == min_date:
    M_datetime = str(df['datetime'].min())+"～"+str(df['datetime'].max()[12:])+"("+str(df['datetime'].count()-1)+"件)"
    print(M_datetime)
else:
    M_datetime = str(df['datetime'].min())+"～"+str(df['datetime'].max())+"("+str(df['datetime'].count()-1)+"件)"
    print(M_datetime)

print("■イベント名")
for unique_list in df['attack'].unique():
    print(unique_list)

print("■通信経路")
for unique_list in df["route"].unique():
    print(unique_list)

print("■送信元")
for unique_list in df['srcip_unique'].unique():
    print(unique_list)
    
print("■送信先")
for unique_list in df["dstip_unique"].unique():
    print(unique_list)

    root.mainloop()