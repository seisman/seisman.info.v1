Perl发送邮件到BREQ_FAST
#######################

:date: 2013-07-26 21:15
:author: SeisMan
:category: 编程
:tags: breq_fast, 邮件, Perl
:slug: send-email-in-perl

.. contents::

BREQ_FAST的优势在于可脚本化生成数据申请文件，要真正申请数据还得将这些文件作为邮件内容发送过去，因而想要解放双手，利用脚本自动发送邮件是必须的。

本文给出如何用Perl发送邮件到BREQ_FAST，另一篇博文《Python发送邮件到BREQ_FAST》给出了同样功能的Python脚本。相比而言，Python版本更简单、简洁。

脚本
====

下面的Perl脚本利用Net::SMTP模块实现了邮件的脚本发送：

.. code-block:: perl

 #!/usr/bin/perl -w
 #
 #  Perl Script to send emails to IRIS
 #
 #  Author:  SeisMan @ seisman.info
 #  Date:    2013/07/22
 #

 use warnings;
 use strict;

 use Net::SMTP;
 use MIME::Base64;

 @ARGV >= 1 or die "  Usage: perl $0 mailfiles \n";

 my $host = 'smtp.163.com';          # host domain
 my $sender = 'xxxxxx@163.com';                  # my email
 my $passwd = "xxxxxxxx";            # password
 my $recipient='breq_fast@iris.washington.edu';  # BREQ_FAST email

 foreach (@ARGV) {
     my $smtp = Net::SMTP->new(
         Host    =>   $host,
         Timeout =>   30,
         Debug   =>   0,
     );

     # Log in
     $smtp->command('AUTH LOGIN')->response();
     my $userpass = encode_base64($sender);  chomp($userpass);
     $smtp->command($userpass)->response();
     $userpass = encode_base64($passwd); chomp($userpass);
     $smtp->command($userpass)->response();

     # send mail
     print "Sending mailfile $_\n";
     $smtp->mail($sender);
     $smtp->to($recipient);
     $smtp->data();
     $smtp->datasend("To:$recipient \n");
     $smtp->datasend("\n");

     open(IN, "< $_") or die "Error in opening $_\n";
         $smtp->datasend($_) foreach (<IN>);
     close(IN);
     $smtp->dataend();
     $smtp->quit;
 #   unlink "$_";

     sleep(5);
 }


其中MIME::Base64模块对邮件内容进行编码，\$host为邮件服务器的ip或者域名，\$sender为邮箱，\$passwd为明文密码。

脚本首先向邮件服务器申请身份验证，然后分别读取每个mailfile中的内容作为邮件正文发送到\$recipient。

功能及限制
==========

#. 支持一次性发送多封邮件（一次登录可以发送的邮件数是有限制的，所以采取多次登录的方式；频繁发送邮件可能会导致ip被封，因而每封邮件之间等待10s）；
#. 密码明文存储，不太安全；
#. 没有判断身份验证失败的情况；
#. 可以通过Debug=>1的方式获取调试信息以确定身份验证是否成功，但调试信息过多；

参考
====

-  perl发送邮件真正可用版本：http://blog.sina.com.cn/s/blog\_541a3cf10100ji64.html
-  CPAN Net::SMTP：http://search.cpan.org/=gbarr/libnet-1.22/Net/SMTP.pm

修订历史
========

-  2013-07-26：初稿；
-  2013-11-22：修正了脚本复制过程中的一个bug。Thanks to cxh757.
-  2014-01-13：注释\ ``unlink "$\_";``\ ，该句会在脚本执行完毕后删除邮件，由于脚本未做邮件发送是否成功的检测，贸然删除邮件对于用户不够友好。
-  2014-08-24：加入了Python版本的链接。
