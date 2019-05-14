#coding UTF-8
import datetime
import csv

with open('data.csv', 'a',encoding="UTF-8") as f:
    data = csv.reader(f)
    header = next(data)
    for i in data:
        f0 = int(i[5])
        f1 = int(i[6])
        last = datetime.datetime.strptime(i[8], '%Y-%m-%d')
        d = last + datetime.timedelta(days=f0)+ datetime.timedelta(days=f1)
        d = datetime.date(d.year, d.month, d.day)
        if d <= datetime.date.today():
            print(str(i[3]) + ":" + str(i[1]))  # 科目：問題文
            yourAns = input('>> ')
            ans = i[2]
            if yourAns == ans:
                # 正解のとき
                flag = "Collect!"
                print(flag)

                # dataに情報上書き
                f0 = i[5]
                f1 = i[6]
                i[6] = f0  # F0をF1に移動
                i[7] = f1 + f0  # F1に元のF0とF1を足したF数を入力(新F0)
                i[8] = datetime.date.today()  # 最終学習日に今日の日付を入力

            else:
                flag = "miss"
                print(flag)
            log_no = i[0]  # 問題No
            log_day = str(datetime.date.today())
            log_flag = flag
            with open('log.csv', 'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow([str(d),i[0],flag])
        else:  # dammy
            dammy = 0