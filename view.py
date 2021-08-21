import csv
import eel
import desktop
import possys

app_name="web"
end_point="index.html"
size=(700,600)
item_csv = 'item.csv'
# total_price = 0

### ファイル操作クラス
class Option:
    @staticmethod
    def read_csv(filename):
        item_master = []
        # csvから商品登録
        with open(f'./{filename}', 'r', encoding='utf_8-sig') as f:
            h = next(csv.reader(f))
            for row in f:
                rows = row.rstrip().split(',')
                item_master.append(possys.Item(rows[0], rows[1], rows[2]))
        return item_master

@ eel.expose
def pos_system(code, number):
    output_data = possys.regist(code, number, order)
    return output_data
    
@ eel.expose
def pay_system(money):
    print("関数内です。")
    change_data = possys.payment(money, order)
    return change_data


# マスタ登録
# csvから商品登録
option = Option()
item_master = option.read_csv(item_csv)
# オーダー登録
order=possys.Order(item_master)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)