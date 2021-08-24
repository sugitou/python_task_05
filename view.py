import eel
import desktop
import possys

app_name="web"
end_point="index.html"
size=(600,700)
item_csv = 'item.csv'

@ eel.expose
def pos_system(code, number):
    output_data = calc.regist(code, number)
    return output_data
@ eel.expose
def pay_system(money, coupon_code):
    change_data = calc.payment(money, coupon_code)
    return change_data

# マスタ登録
# csvから商品登録
option = possys.Option()
item_master = option.read_csv(item_csv)
# オーダー登録
order=possys.Order(item_master)
# クーポンクラス
coupon=possys.Create_Coupon()
# 計算クラス
calc=possys.Calculation(order, coupon)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)