import smtplib  # 邮件发送模块
from email.mime.text import MIMEText
from email.header import Header


def email_send():
    # 邮件配置信息
    smtp_server = 'smtp.qq.com'  # 邮箱服务器
    smtp_port = 465  # SSL端口
    smtp_user = 'shwaige_zhang@qq.com'
    smtp_password = 'sevvqpztwodgcijf'  # 邮箱授权码

    # 发送邮件信息
    sender = 'shwaige_zhang@qq.com'  # 发送者邮箱
    receivers = ['chaxun@troodo.com']  # 接收者邮箱

    # 邮件正文
    mail_content = '魔窟活动无异常可以上线'  # 邮件正文内容
    message = MIMEText(mail_content, 'plain', 'utf-8')  # 邮件正文格式

    # 邮件信息配置
    message['From'] = 'shwaige_zhang@qq.com'  # 邮件标头中发件人，不影响实际发送邮箱
    message['To'] = 'chaxun@troodo.com'  # 邮件标头中收件人
    message['Subject'] = Header("魔窟活动", 'utf-8')  # 邮件标题

    # 发送邮件
    try:
        smtp_obj = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 使用SSL连接服务器
        smtp_obj.login(smtp_user, smtp_password)  # 登入发送者邮箱
        smtp_obj.sendmail(sender, receivers, message.as_string())  # 发送邮件指令
        print("邮件发送成功")

    except smtplib.SMTPException as e:
        print("Error: 邮件发送失败: ", e)


if __name__ == '__main__':
    email_send()  # 调用发送邮件函数
