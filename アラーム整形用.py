# tkinterのインポート
import tkinter as tk
import pandas as pd

#####  GUI  #####
root = tk.Tk()
root.geometry("350x400")


#####  関数  #####


#ファイル選択用
def test_open_file():
    df = pd.read_csv("D:fortigate.csv",names=["rows"])

#####  GUIウィジェット  #####

text_box = tk.Text()
text_box.grid(
    row=1,
    sticky=tk.NE+tk.NW+tk.S
)


# Runボタン設置
text_read_button = tk.Button(root, text = "Read",command=test_open_file())
text_read_button.grid(
    row=0,
)


root.mainloop()