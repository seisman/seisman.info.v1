Python发送邮件到BREQ_FAST
#########################

:date: 2014-08-23 16:51
:author: SeisMan
:category: 编程
:tags: breq_fast, 邮件, Python
:slug: send-email-in-python

利用Python的标准库 `smtplib <https://docs.python.org/3/library/smtplib.html>`_ 实现了通过脚本发送邮件的功能。

源码地址： `sendmail.py <https://github.com/seisman/PyScripts/blob/master/sendmail.py>`_

说明：

#. 仅支持Python 3.x
#. 需要修改的变量包括：

   - ``sender`` ：用户邮箱
   - ``passwd`` ：明文密码
   - ``host`` ：邮件服务器的IP或域名
   - ``port`` ：邮件服务器的端口号

#. 目前仅测试了网易的163、USTC邮件系统和微软的outlook：

   =========== ===================== ==========
   服务商      服务器                端口
   =========== ===================== ==========
   163         smtp.163.com          25
   USTC mail   mail.ustc.edu.cn      25
   Outlook     smtp-mail.outlook.com 587
   =========== ===================== ==========

#. 支持一次性发送多封邮件

   - 一次登录可发送的邮件数是有限制的，因而采取多次登录的方式
   - 频繁发送邮件可能会导致IP被封等问题，目前的策略是随机等待3到10秒，但在发送上百封邮件时依然可能会被封，此时只能用两个邮箱轮番发送

#. 仅为BREQ_FAST设计，因而假定邮件内存为纯ASCII字符
#. 密码明文存储，不太安全
