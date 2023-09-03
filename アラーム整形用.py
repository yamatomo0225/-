import pandas as pd
import tkinter as tk


def push_reset():
    text_input.delete(0.0,"end")
def push_start():
    radio_value = radio_0.get()
    text =text_input.get(0.0,"end")
    
#FortiGate処理用
    if radio_value == "FortiGate":
        df = pd.read_csv("D:fortigate.csv",names=["rows"])

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

        #統一規格

        df["datetime"] = pd.to_datetime(df["date"]+"T"+df["time"])
        df["datetime"] = df["datetime"].dt.strftime('%Y/%m/%d %H:%M:%S')
        df["route"] = df["srcip"]+"→"+df["dstip"]+"(port:"+df["dstport"]+")"
        df["route_unique_srcip"] = df["route"].str.extract(r'(.*?)→')
        df["route_unique_dstip_port"] = df["route"].str.extract(r'→(.*?\(port:.*?\))')


#メール出力用

        min_date = str(df['datetime'].min())[:10]
        max_date = str(df['datetime'].max())[:10]
        if max_date == min_date:
            M_datetime = str(df['datetime'].min())+"～"+str(df['datetime'].max()[12:])+"("+str(df['datetime'].count()-1)+"件)"
        else:
            M_datetime = str(df['datetime'].min())+"～"+str(df['datetime'].max())+"("+str(df['datetime'].count()-1)+"件)"
        attack_list=""
        for i in df['attack'].unique():
            attack_list = str(attack_list) + str(i) + "\n"
        route_list=""
        for i in df["route"].unique():
            route_list = str(route_list) + str(i) + "\n"
        srcip_list=""
        for i in df['route_unique_srcip'].unique():
            srcip_list = str(srcip_list) + str(i) + "\n"
        dstip_port_list=""
        for i in df["route_unique_dstip_port"].unique():
            dstip_port_list = str(dstip_port_list) + str(i) + "\n"

        text_output.insert(
            0.0,
            '■検知時刻\n'
            +M_datetime+"\n\n"
            '■イベント名\n'
            +attack_list+"\n"
            '■通信経路\n'
            +route_list+"\n"
            '■送信元IP\n'
            +srcip_list+"\n"
            '■宛先IP(Port)\n'
            +dstip_port_list+"\n"
        )

#GUI

root = tk.Tk()
root.title(u"Software Title")
root.geometry("1000x600")

radio_0 = tk.StringVar(value="FortiGate")

radio_FortiGate = tk.Radiobutton(
    root,
    text="FortiGate",
    value="FortiGate",
    variable=radio_0
)
radio_FortiGate.grid(
    row=0,
    column=0,
)
radio_NSP = tk.Radiobutton(
    root,
    text="NSP",
    value="NSP",
    variable=radio_0
)
radio_NSP.grid(
    row=0,
    column=1,
)
radio_PaloAlto = tk.Radiobutton(
    root,
    text="PaloAlto",
    value="PaloAlto",
    variable=radio_0
)
radio_PaloAlto.grid(
    row=0,
    column=2,
)
radio_NetVisor = tk.Radiobutton(
    root,
    text="NetVisor",
    value="NetVisor",
    variable=radio_0
)
radio_NetVisor.grid(
    row=0,
    column=3,
)
radio_iMark = tk.Radiobutton(
    root,
    text="iMark",
    value="iMark",
    variable=radio_0
)
radio_iMark.grid(
    row=0,
    column=4,
)
button_read = tk.Button(
    root,
    text="Start",
    command=push_start
)
button_read.grid(
    row=2,
    column=0
)
button_reset = tk.Button(
    root,
    text="Reset",
    command=push_reset
)
button_reset.grid(
    row=2,
    column=1
)
text_input=tk.Text(
    root,
    width=50,
    height=5,
)
text_input.grid(
    row=3,
    columnspan=5
)
text_output=tk.Text(
    root,
    width=100,
    height=100,
)
text_output.grid(
    row=4,
    columnspan=5
)


root.mainloop()