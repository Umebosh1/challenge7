list=["2","3","5"]
while True:
    a=input("数字を入力してください:")
    if a in list:
        print("正解")
        break
    elif a=="q":
        print("終了します")
        break
    else:
        print("不正解")
        print("数字を入力するか、qで終了します")
