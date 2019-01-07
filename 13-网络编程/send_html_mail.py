import smtplib
from email.mime.text import MIMEText

# MIMEText 三个主要参数
# 1 邮件的内容
# 2 MINE子类型，此案例我们用plain来表示text类型,html 表示html邮件格式
# 3 邮件编码格式


content = """
        <!DOCTYPE html>
        <html>
        <head></head>
        <body></body>
        </html>
"""

msg = MIMEText(content,"html",'utf-8')

# 发送地址
from_addr = "751081818@qq.com"

# 授权码
from_pwd = ""

# 接收地址
to_addr = "marlonlengyq@gmai.com"


# smtp 服务器地址
smtp_srv = "smtp.qq.com"
try:
    # 连接 qq的邮件服务器
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    # 登录
    srv.login(from_addr,from_pwd)
    # 发送邮件
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    # 退出关闭
    srv.quit()

except Exception as e:
    print(e)
