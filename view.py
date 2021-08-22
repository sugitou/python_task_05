import eel
import desktop
import possys

app_name="web"
end_point="index.html"
size=(600,700)
item_csv = 'item.csv'

@ eel.expose
def pos_system(code, number):
    output_data = possys.regist(code, number, order)
    return output_data
@ eel.expose
def pay_system(money, coupon):
    change_data = possys.payment(money, coupon, order)
    return change_data

# マスタ登録
# csvから商品登録
option = possys.Option()
item_master = option.read_csv(item_csv)
# オーダー登録
order=possys.Order(item_master)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)