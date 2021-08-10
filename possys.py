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

    def add_item_order(self):
        while True:
            try:
                item_code = int(input('登録する商品コードを入力してください:\n'))
            except ValueError:
                print('もう一度やり直してください。')
                continue
            item_code_s = str(item_code).zfill(3)
            # 追加　存在チェック
            check = self.check_data(item_code_s)
            if check != None:
                try:
                    item_num = int(input('個数を入力してください:\n'))
                except ValueError:
                    print('商品登録からやり直してください。')
                    continue
                item_code_num = {'code':item_code_s, 'num':item_num}
                self.item_order_list.append(item_code_num)
                print(f'{item_code_s}を{item_num}個で登録しました！')
            else:
                print(f'{item_code_s}の商品は存在しません。')
                continue
            
            again_code = input('登録を続けますか？　y/n\n')
            if again_code == 'n':
                break
    
    def output_regist_item(self, newest_receipt):
        total_price = 0
        for item in self.item_order_list:
            for register in self.item_master:
                if item['code'] == Item.get_code(register):
                    item_num_s = str(item['num'])
                    code_sum = int(Item.get_price(register)) * item['num']
                    goods_name = f'商品名　　　　              {Item.get_name(register)}'
                    goods_price = f'商品価格　　　              ￥{Item.get_price(register)}'
                    goods_num = f'商品個数　　　              ×{item_num_s}'
                    goods_sum = f'合計金額　　　              ￥{code_sum}'
                    # ファイルへ書き出し
                    with open(newest_receipt, 'a', encoding='utf_8-sig') as wf:
                        wf.write(f'{goods_name}\n{goods_price}\n{goods_num}\n{goods_sum}\n')
                    # 最終的な合計金額
                    total_price += code_sum
        return total_price
    
    def remain_cal(self, total_price, newest_receipt):
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

    @staticmethod
    def mk_new_dir(dir_name):
        # カレントディレクトリの取得
        base_dir = os.path.dirname(os.path.abspath(__file__))
        new_dir = os.path.join(base_dir, dir_name)
        # 指定ディレクトリ作成
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        return new_dir

    @staticmethod
    def create_file(new_dir_name):
         # 現在時刻取得
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.txt'
        # ファイル名決定
        receipt = os.path.join(new_dir_name, now)
        return receipt


    
### メイン処理
def main():
    # マスタ登録
    # csvから商品登録
    option = Option()
    item_master = option.read_csv(item_csv)
    
    # オーダー登録
    order=Order(item_master)
    order.add_item_order()

    # ディレクトリチェック
    register_front_dir = option.mk_new_dir(register_front_name)
    # ファイル作成
    newest_receipt = option.create_file(register_front_dir)

    # オーダー登録した商品の出力
    total_price = order.output_regist_item(newest_receipt)

    # お釣りの出力
    order.remain_cal(total_price, newest_receipt)
    
if __name__ == "__main__":
    main()