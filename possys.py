import os
import csv
import datetime

item_csv = 'item.csv'
# total_price = 0
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
        self.total_price = 0

    def check_data(self, input_code):
        for n in self.item_master:
            if input_code == Item.get_code(n):
                return Item.get_name(n)

    def add_item_order(self, item_code, item_num):
        try:
            item_code_i = int(item_code)
        except ValueError:
            return '商品登録からやり直してください。\n', 0

        item_code_s = str(item_code_i).zfill(3)
        item_num_i = 0
        # 追加　存在チェック
        check = self.check_data(item_code_s)
        if check != None:
            try:
                item_num_i = int(item_num)
            except ValueError:
                return '商品登録からやり直してください。\n', 0
            
            item_code_num = {'code':item_code_s, 'num':item_num_i}#
            self.item_order_list.append(item_code_num)#
            # 変数定義
            code_sum = 0
            goods_print = ''
            # 一致する商品コードを検索
            for register in self.item_master:
                if item_code_num['code'] == Item.get_code(register):
                    item_num_s = str(item_code_num['num'])
                    code_sum = int(Item.get_price(register)) * int(item_code_num['num'])
                    goods_name = f'商品名：　{Item.get_name(register)}'
                    goods_price = f'商品価格： ￥{Item.get_price(register)}'
                    goods_num = f'商品個数： ×{item_num_s}'
                    goods_sum = f'商品金額： ￥{code_sum}'
                    goods_print = f'{goods_name}\n{goods_price}\n{goods_num}\n{goods_sum}\n'
                    self.total_price += code_sum
            return goods_print
        else:
            # 商品コードが存在しない場合
            return f'{item_code_s}の商品は存在しません。\n', 0
    
    def get_price(self):
        return self.total_price



    
### メイン処理
def regist(code, number, order):
    # 出力値を受け取る
    output_data = order.add_item_order(code, number)
    str_p = f'総額： ￥{order.get_price()}\n'
    output_data += str_p
    return output_data

def set_price(order):
    return order.get_price()

def payment(money, order):
    print("計算するよ。")
    money_i = 0
    try:
        money_i = int(money)
    except ValueError:
        return '数字を入力してください。'
    if money_i > order.get_price():
        change = money_i - order.get_price()
        change_result = f'{change}円のお返しです。\nまたのお越しをお待ちしております！'
        return change_result
    else:
        return '商品を購入することができません。'
    
