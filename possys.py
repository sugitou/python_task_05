import os
import csv
import datetime
import random

item_csv = 'item.csv'
### 商品クラス
class Item:
    def __init__(self, item_code, item_name, price):
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
    def __init__(self, item_master):
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
            return '商品登録からやり直してください。\n'

        item_code_s = str(item_code_i).zfill(3)
        item_num_i = 0
        # 追加　存在チェック
        check = self.check_data(item_code_s)
        if check != None:
            try:
                item_num_i = int(item_num)
            except ValueError:
                return '商品登録からやり直してください。\n'
            
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
            return f'{item_code_s}の商品は存在しません。\n'
    
    def get_price(self):
        return self.total_price

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

### 計算クラス
class Calculation:
    def __init__(self, order, coupon):
        self.order=order
        self.coupon=coupon
    ### 商品登録
    def regist(self, code, number):
        # 出力値を受け取る
        output_data = self.order.add_item_order(code, number)
        str_p = f'総額： ￥{self.order.get_price()}\n'
        output_data += str_p
        return output_data
    ### レジ計算
    def payment(self, money, coupon_code):
        money_i = 0
        try:
            money_i = int(money)
        except ValueError:
            return '数字を入力してください。'
        # クーポン適用
        disc_after = self.coupon.cp_trans(self.order.get_price(), coupon_code)
        # お預かり金額の確認
        if money_i >= disc_after:
            change = money_i - disc_after
            cp = self.coupon.cp_gift()
            change_result = f'{change}円のお返しです。\n{cp}\nまたのお越しをお待ちしております。\n'
            return change_result
        else:
            return 'お金が足りません。'

### クーポンクラス
class Create_Coupon:
    ### クーポン発券
    @staticmethod
    def cp_gift():
        cps = ['Lucky10%', 'Lucky20%', 'Lucky30%']
        gift = random.choice(cps)
        if gift == 'Lucky10%':
            cp_result = f'10%引きのクーポンが発券されました！\n{gift}'
        elif gift == 'Lucky20%':
            cp_result = f'20%引きのクーポンが発券されました！\n{gift}'
        else:
            cp_result = f'30%引きのクーポンが発券されました！\n{gift}'
        return cp_result
    ### クーポン交換
    @staticmethod
    def cp_trans(tp, ticket):
        if ticket == 'Lucky10%':
            disc_amount = tp * 0.9
        elif ticket == 'Lucky20%':
            disc_amount = tp * 0.8
        elif ticket == 'Lucky30%':
            disc_amount = tp * 0.7
        else:
            disc_amount = tp
        return int(disc_amount)
    
