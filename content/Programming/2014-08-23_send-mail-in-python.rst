Python发送邮件到BREA_FAST
#########################

:date: 2014-08-23 16:51
:author: SeisMan
:category: 编程
:tags: breq_fast, 邮件, Python
:slug: send-email-in-python

.. contents::

前面的一篇博文\ `《Perl发送邮件》 <{filename}/Programming/2013-07-26_send-email-in-perl.rst>`_\ 中用Perl实现了向BREQ_FAST发送邮件申请数据的功能。

这篇博文用Python重新实现了这一功能，相比于Perl脚本而言，Python的面向对象特性使得脚本更简单、简短。

Python脚本
==========

该脚本使用了Python标准库smtplib实现邮件的发送，在Python 2.7及3.4下测试通过。

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    #  Send multiple emails to BREQ_FAST for waveform datas
    #
    #  Author:  Dongdong Tian @ USTC
    #  Date:    2014-08-23
    #

    import sys
    import time
    from smtplib import SMTP

    sender = "xxxxxxx@163.com"
    passwd = "xxxxxxx"
    # host and port for 163 mail
    host, port = "smtp.163.com", 25
    # BREQ_FAST mail address
    recipient = 'breq_fast@iris.washington.edu'

    if len(sys.argv) == 1:
        print("Usage:")
        print("  python %s mailfile ..." % (sys.argv[0]))
        sys.exit()

    head = ("From: %s\r\nTo: %s\r\n\r\n" % (sender, recipient))

    print("Total %d mails to send!" % (len(sys.argv[1:])))

    for mail in sys.argv[1:]:
        print("Sending %s ..." % (mail))
        msg = head
        with open(mail) as f:
            msg += f.read()

        smtp = SMTP(host=host, port=port)
        smtp.set_debuglevel(0)
        smtp.login(sender, passwd)
        smtp.sendmail(sender, recipient, msg)
        smtp.quit()

        time.sleep(5)

其中\ ``host``\ 为邮件服务器的ip或域名， \ ``sender``\ 为用户邮箱名， \ ``passwd``\ 为明文密码。

Host列表
========

163和USTC mail测试通过，Gmail测试失败。

.. list-table::
   :widths: 10 30 10
   :header-rows: 1

   * - 服务商
     - Host
     - Port
   * - 163
     - smtp.163.com
     - 25
   * - USTC mail
     - mail.ustc.edu.cn
     - 25


功能及限制
==========

#. 支持一次性发送多封邮件。（单次登录可发送的邮件数是有限制的，因而采取多次登录的方式；频繁发送邮件可能会导致ip被封，因而每封邮件之间等待5s）；
#. 密码明文存储，不太安全；
