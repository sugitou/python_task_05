import eel
import desktop
import possys

app_name="web"
end_point="index.html"
size=(700,600)

@ eel.expose
def pos_system(code, number):
    output_data = possys.regist(code, number)
    return output_data
    print('output_data', output_data)
    print(type(output_data))
    # 関数を動かすたびに金額を足していく
    # total_price += output_data[1]
    # print('output_data', output_data[1])
    


desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)