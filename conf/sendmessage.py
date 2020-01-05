import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

def send_message():
# 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "邮箱地址"  # 用户名
    mail_pass = "dfpcglacrjbybafa"  # 口令

    sender = '发送方'
    receivers = ['1206180814@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("我是发件人", 'utf-8')  # 发件人
    message['To'] = Header("我是收件人", 'utf-8')   # 收件人

    subject = '接口测试运行结果'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    send_content = 'hi man，你收到附件了吗？'
    content_obj = MIMEText(send_content, 'plain', 'utf-8')  # 第一个参数为邮件内容
    message.attach(content_obj)

    # 构造附件1，发送当前目录下的 t1.txt 文件
    part1 = MIMEApplication(open('report.zip', 'rb').read())
    part1.add_header('Content-Disposition', 'attachment', filename='t1.txt')
    message.attach(part1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
