import csv

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

    def add_item_order(self):
        while True:
            try:
                item_code = int(input('登録する商品コードを入力してください:\n'))
            except ValueError:
                item_code = 0
            item_code_s = str(item_code).zfill(3)
            self.item_order_list.append(item_code_s)
            print(f'{item_code_s}の登録が完了しました！')
            
            again_code = input('登録を続けますか？　y/n\n')
            if again_code == 'n':
                break
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
            # print(self.item_master[0])
    
    def view_regist_item(self):
        for item in self.item_order_list:
            for register in self.item_master:
                if item == Item.get_code(register):
                    print(f'商品名　:{Item.get_name(register)}')
                    print(f'商品価格:{Item.get_price(register)}')
    
    
### メイン処理
def main():
    # マスタ登録
    item_csv = 'item.csv'
    item_master=[]
    # csvから商品登録
    with open(f'./{item_csv}', 'r', encoding='utf_8-sig') as f:
        h = next(csv.reader(f))
        for row in f:
            rows = row.rstrip().split(',')
            item_master.append(Item(rows[0], rows[1], rows[2]))
    
    # オーダー登録
    order=Order(item_master)
    order.add_item_order()
    
    # オーダー表示
    order.view_item_list()

    # オーダー登録した商品の表示
    order.view_regist_item()
    
if __name__ == "__main__":
    main()