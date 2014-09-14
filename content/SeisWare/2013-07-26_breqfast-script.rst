BREQ_FAST脚本实现
#################

:date: 2013-07-26 14:56
:author: SeisMan
:category: 地震学软件
:tags: breq_fast, Perl, 数据申请
:slug: breqfast-script

.. contents::

Perl代码
=========

.. code-block:: perl

 #!/usr/bin/perl -w
 #
 #  Perl script to generate mail content for BREQ_FAST
 #
 #  Author:  SeisMan @ seisman.info
 #  Date:    2013/07/22
 #

 use warnings;
 use strict;

 use Time::Local;

 @ARGV == 2 or die "Usage: perl $0 Event(e.g.,2008_05_12_06_28_02) Mailfile\n";

 ##  Private Information Here
 my $NAME  = 'FirstName LastName';
 my $INST  = 'University of XXXX';
 my $MAIL  = 'Dept. of Geophysics,xxxxxx';
 my $EMAIL = 'xxx@xxx.xxx';
 my $PHONE = '86-xxxxxxxxxx';
 my $FAX = "xxx-xxx-xxxx";

 ##  Other Information
 my $MEDIA = "FTP";
 my $ALTERNATEMEDIA  = "exabyte";
 my $STATIONS = "US_TA.list";
 my $timespan = 3600; # time window of one hour

 ##  DO NOT MODIFY BELOW
 my ($year, $month, $day, $hour, $min, $sec) = split('_',$ARGV[0]);
 $sec = "00" if (!defined($sec ));   # second=00

 my $mailfile=$ARGV[1];
 unlink $mailfile if (-f $mailfile);

 my $LABEL = "${year}_${month}_${day}_${hour}_${min}_${sec}";
 my $begintime  = "$year $month $day $hour $min $sec.0";

 $month -= 1;
 my $time = timegm($sec, $min, $hour, $day, $month, $year);
 $time += $timespan;

 my ($sec1, $min1, $hour1, $day1, $mon1, $year1, $wday1, $yday1, $isdast1) = gmtime($time);
 $year1 += 1900;
 $mon1 += 1;
 my $endtime = sprintf "%4d %02d %02d %02d %02d %02d.0", $year1, $mon1, $day1, $hour1, $min1, $sec1;

 open(OUT, ">$mailfile");
 print OUT ".NAME $NAME\n";
 print OUT ".INST $INST\n";
 print OUT ".MAIL $MAIL\n";
 print OUT ".EMAIL $EMAIL\n";
 print OUT ".PHONE $PHONE\n";
 print OUT ".FAX $FAX\n";
 print OUT ".MEDIA $MEDIA\n";
 print OUT ".ALTERNATE MEDIA 1/2\" tape - 6250\n";
 print OUT ".ALTERNATE MEDIA $ALTERNATEMEDIA\n";
 print OUT ".LABEL $LABEL\n";
 print OUT ".QUALITY B\n";
 print OUT ".END\n";
 print OUT "\n";
 open(IN, "< $STATIONS");
 foreach (<IN>) {
    my @c = split ",", $_;
    my ($begin, $junk1, $junk2) = split "/", $c[5]; # start time of station
    my ($end  , $junk3, $junk4) = split "/", $c[7]; # start time of station
    my $sta = $c[2];
    my $net = $c[1];
    if ($year>=$begin and $year<=$end) {
        print OUT "$sta $net $begintime $endtime 1 BH?\n";
    }
 }
 close(IN);
 close(OUT);

备注
====

- 首先要根据个人情况修改个人信息；
- 其他信息中，\ ``$STATIONS``\ 为台站列表文件，\ ``$timespan``\ 为要申请的数据长度，即从发震时刻到发震后的\ ``$timespan``\ 秒（更常用的是从P波前几秒开始申请，这里没实现）
- $STATIONS文件为台站列表文件，US_TA.list来自于 http://www.iris.edu/vnets?vnet=_US-TA ，取CSV格式；（需要将CSV文件的前几行删除，只留下与台站有关的行）
- 程序中判断了发震时刻是否在台站的有效期内，这样的判断可以减小文件内容；

修订历史
========

- 2013-07-26：原始版本；
- 2013-08-02：CSV格式要稍做编辑才可使用；
