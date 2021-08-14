import eel
import desktop
import possys

app_name="web"
end_point="index.html"
size=(700,600)

@ eel.expose
def pos_system(code, number):
    possys.regist(code, number)
    


desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)