from urllib import request

googleurl="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512046437&di=613d2c56b456206a53203b57fbdca4b2&imgtype=jpg&er=1&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2F42166d224f4a20a472ebf2fd9b529822720ed017.jpg"

def dlfile(url):
    response =request.urlopen(url)
    cvs =response.read()
    cvs_str= str(cvs)
    lines = cvs_str.split("\\n")
    des_url=r'google.csv'
    fx=open(des_url, "w")
