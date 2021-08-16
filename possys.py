import os
import csv
import datetime

item_csv = 'item.csv'
register_front_name = 'receipt_box'
### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

    def get_code(self):
        return self.item_code

    def get_name(self):
        return self.item_name

    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master

    def check_data(self, input_code):
        for n in self.item_master:
            if input_code == Item.get_code(n):
                return Item.get_name(n)

    def add_item_order(self, item_code, item_num):
        item_code_s = str(item_code).zfill(3)
        item_num_i = 0
        total_price = 0
        # 追加　存在チェック
        check = self.check_data(item_code_s)
        if check != None:
            try:
                item_num_i = int(item_num)
            except ValueError:
                print('商品登録からやり直してください。')
            
            item_code_num = {'code':item_code_s, 'num':item_num_i}#
            self.item_order_list.append(item_code_num)#
            for register in self.item_master:
                if item_code_num['code'] == Item.get_code(register):
                    item_num_s = str(item_code_num['num'])
                    code_sum = int(Item.get_price(register)) * item_code_num['num']
                    goods_name = f'商品名：　{Item.get_name(register)}'
                    goods_price = f'商品価格： ￥{Item.get_price(register)}'
                    goods_num = f'商品個数： ×{item_num_s}'
                    goods_sum = f'合計金額： ￥{code_sum}'
                    goods_print = f'{goods_name}\n{goods_price}\n{goods_num}\n{goods_sum}\n'
                    return goods_print, code_sum
        else:
            return f'{item_code_s}の商品は存在しません。', 0
            
    
    # def output_regist_item(self, newest_receipt):
    #     total_price = 0
    #     for item in self.item_order_list:
    #         for register in self.item_master:
    #             if item['code'] == Item.get_code(register):
    #                 item_num_s = str(item['num'])
    #                 code_sum = int(Item.get_price(register)) * item['num']
    #                 goods_name = f'商品名　　　　              {Item.get_name(register)}'
    #                 goods_price = f'商品価格　　　              ￥{Item.get_price(register)}'
    #                 goods_num = f'商品個数　　　              ×{item_num_s}'
    #                 goods_sum = f'合計金額　　　              ￥{code_sum}'
    #                 # ファイルへ書き出し
    #                 with open(newest_receipt, 'a', encoding='utf_8-sig') as wf:
    #                     wf.write(f'{goods_name}\n{goods_price}\n{goods_num}\n{goods_sum}\n')
    #                 # 最終的な合計金額
    #                 total_price += code_sum
    #     return total_price
    

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
                item_master.append(Item(rows[0], rows[1], rows[2]))
        return item_master

    
### メイン処理
def regist(code, number):
    # マスタ登録
    # csvから商品登録
    option = Option()
    item_master = option.read_csv(item_csv)
    print('item_master:', item_master)
    
    # オーダー登録
    order=Order(item_master)
    order_info = order.add_item_order(code, number)

    return order_info
    # オーダー登録した商品の出力
    # total_price = order.output_regist_item(newest_receipt)

def payment(total_price, newest_receipt):
    with open(newest_receipt, 'a', encoding='utf_8-sig') as wf:
        wf.write('-----------------------------------\n')
        wf.write(f'商品の合計金額              ￥{total_price}\n')
        while True:
            try:
                money = int(input('支払う金額を入力してください:\n'))
                break
            except ValueError:
                print('もう一度やり直してください。')
        if money > total_price:
            change = money - total_price
            wf.write(f'お預かり金額　              ￥{money}\n')
            wf.write(f'お釣り　　　　              ￥{change}\n')
        else:
            print('商品を購入することができません。')
    
