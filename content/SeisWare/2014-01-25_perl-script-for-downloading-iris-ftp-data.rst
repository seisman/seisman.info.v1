IRIS FTP数据下载脚本
####################

:date: 2014-01-25 00:40
:author: SeisMan
:category: 地震学软件
:tags: breq_fast, IRIS, 数据, Perl
:slug: perl-script-for-downloading-iris-ftp-data

前文说到了IRIS官方给出的几种FTP数据下载方式，除此之外，还有很多方法。比如直接浏览器右键另存为，比如Windows下迅雷的下载链接自动识别，再比如Firefox浏览器+附加组件"DownThemAll!"。这些工具其实和前文说的下载方法类似，都有各种各样的缺点。

下面的Perl脚本实现了IRIS FTP数据的下载，其思路如下：

#. 登录IRIS的ftp，获取ftp内的全部文件列表，保存到本地文件ftp.filelist中；
#. 由于IRIS ftp里的数据默认会保存7天，且用户无删除权限，因而可能有些ftp中的数据已经下载了，所以在本地需要有一个已经下载的数据的列表local.filelist；
#. 读取ftp.filelist和local.filelist的内容，检查ftp.filelist中的文件是否在local.filelist中，若在则不下载，若不在则下载。
#. 所有文件下载完成后，则意味着ftp.filelist中的全部文件都已在本地，更新local.filelist。
#. 重复步骤1,2,3,若ftp.filelist与local.filelist不同则意味着下载过程中有新数据到达，继续下载（这一步其实可以手动重复执行该脚本，而不需要在脚本内部进行循环）。

脚本的一些特性：

-  已下载的数据可以移动到其他文件夹，这些数据不会重复下载；（需要重复下载时可手动修改local.filelist）
-  FTP中所有不在local.filelist中的文件都会被下载；
-  若local.filelist为空，则ftp中所有数据都会被下载；
-  若local.filelist包含了7天以前的数据下载信息，这些数据已经在FTP中被删除，这种情况脚本可以处理，不需要删除local.filelist；
-  检测本地数据的大小与ftp中数据的大小是否相等，保证了数据的完整性；若不相等，则不将文件名写入local.filelist。
-  当脚本或网络由于外部因素出现中断导致数据不完整时，借助于wget断点续传功能，可以直接重新运行该脚本，而不做任何特殊处理。

`irisFetch.pl <https://gist.github.com/seisman/2ccefac15c4cd3239382>`

代码预览：

.. code-block:: perl

	#!/usr/bin/env perl
	#
	#  Perl script to fetch seed data form IRIS FTP
	#
	#  Author:  SeisMan @ seisman.info
	#  Date:    05/16/2013
	#
	#  Modules:
	#   1. Net::FTP     #  It is already installed for most Linux OS
	#
	#  Description:
	#   1. $passwd is your email address
	#   2. $cmd and $option is tool for downloading
	#       $cmd = "wget";  $option = "-c";
	#   3. ftp.filelist contains all the data in the ftp (less than 7 days).
	#   4. local.filelist contains all the file you have already download,
	#      file in ftp.filelist but not in local.filelist will be downloaded,
	#      so do not delete local.filelist.
	#
	#  Revision History:
	#   05/16/2013  SeisMan    Initial Coding
	#   01/16/2014  SeisMan    Modify to a serial script
	#

	use strict;
	use warnings;
	use Net::FTP;

	############# Personal Infomation #############
	my $user = "XXXXXXXX";
	my $passwd = 'xxxx@xxxxxxxxxx';

	#############################################################
	## DO NOT MODIFY BELOW UNLESS YOU KNOW WHAT YOU ARE DOING! ##
	#############################################################
	my $server = "ftp.iris.washington.edu";
	my $login = "anonymous";
	my $dir = "pub/userdata";

	# download tools
	my $cmd = "wget";
	my $option = "-c";

	# get filelist of ftp
	print STDERR "Fetching filelist from $server...\n";
	&ftp_list($server, $login, $passwd, $dir, $user);

	# lists
	my @ftp_list    = ();   # all the files in ftp
	my @local_list  = ();   # files already downloaded
	my @finish_list = ();   # files already downloaded
	　　　　　　　　　　　　　#  + files downloaded successfully in this run.

	# read ftp filelist
	open FTP, "< ftp.filelist" or die "Can't open ftp.filelist! \n";
	@ftp_list = <FTP>;
	close FTP;

	# read local filefilst
	if (-e "local.filelist") {
    	open LOCAL, "< local.filelist" or die "Can't open local.filelist\n";
        	@local_list = <LOCAL>;
        	chomp @local_list;
    	close LOCAL;
	}

	############################ start downloading ##############################
	foreach (@ftp_list) {
    	my ($ftp_file, $ftp_size) = split /\s+/, $_;

    	# determine $ftp_file downloaded or not
    	my $in = 0;
    	foreach (@local_list) {
        	chomp;
        	if ($_ =~ $ftp_file) {
            	$in = 1;
            	last;
        	}
    	}

    	if ( $in==1 ) {  # already downloaded
        	push @finish_list, $ftp_file;
    	} else { # need to be downloaded
        	my $err = system "$cmd $option $server/$dir/$user/$ftp_file";
        	# err = 0 means succeed in downloading
        	# err = 1 means downloading error
        	# err = 2 means interrupt by user
        	push @finish_list, $ftp_file if $err==0 && -s $ftp_file == $ftp_size;
    	}
	}
	########################## end downloading ##################################

	# update local.filelist
	open OUT, "> local.filelist" or die "Can't open local.filelist\n";
	foreach (@finish_list) {
    	print OUT "$_\n" if /seed/;
	}
	close OUT;

	sub ftp_list() {
    	my ($server, $login, $passwd, $dir, $user) = @_;

    	my $ftp = Net::FTP->new(
        	Host    =>   $server,
        	Debug   =>   0,
    	) or die "Can't connect to $server\n";

    	$ftp->login($login,$passwd);
    	$ftp->cwd("$dir/$user");
    	my @files = $ftp->dir();
    	$ftp->quit();

    	open OUT, "> ftp.filelist";
    	foreach (@files) {
        	if (/seed$/){
            	my @line = split;
            	print OUT "$line[8] $line[4]\n";
        	}
    	}
    	close OUT;
	}


一些说明：

-  用户只需要修改$user和$passwd即可使用，其中$passwd为邮箱；
-  该脚本为串行版本，并行和多线程版本暂不公开；
-  该脚本经过测试，但不对其任何特性做任何保证；由于使用该脚本造成的任何损失或损害，由用户自己负责；
-  任何疑问、评论、Bug报告，可以在当前页面留言，或邮件联系seisman.info@gmail.com；

