import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

def send_message():
# ������ SMTP ����
    mail_host = "smtp.qq.com"  # ���÷�����
    mail_user = "�����ַ"  # �û���
    mail_pass = "dfpcglacrjbybafa"  # ����

    sender = '���ͷ�'
    receivers = ['1206180814@qq.com']  # �����ʼ���������Ϊ���QQ���������������
    # ����һ����������ʵ��
    message = MIMEMultipart()
    message['From'] = Header("���Ƿ�����", 'utf-8')  # ������
    message['To'] = Header("�����ռ���", 'utf-8')   # �ռ���

    subject = '�ӿڲ������н��'
    message['Subject'] = Header(subject, 'utf-8')

    # �ʼ���������
    send_content = 'hi man�����յ���������'
    content_obj = MIMEText(send_content, 'plain', 'utf-8')  # ��һ������Ϊ�ʼ�����
    message.attach(content_obj)

    # ���츽��1�����͵�ǰĿ¼�µ� t1.txt �ļ�
    part1 = MIMEApplication(open('report.zip', 'rb').read())
    part1.add_header('Content-Disposition', 'attachment', filename='t1.txt')
    message.attach(part1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 Ϊ SMTP �˿ں�
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("�ʼ����ͳɹ�")

    except smtplib.SMTPException:
        print("Error: �޷������ʼ�")
