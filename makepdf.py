#!/usr/bin/env python
"""Convert rST and markdown to PDF

Usage:
    makepdf.py (--all | --update)
"""

import os
import re
import subprocess

from docopt import docopt

siteurl = "http://seisman.info"
base = os.path.abspath("content")
pdfdir = os.path.join(base, "pdfs")
article_dirs = ['FreeTalk', 'GeoResource', 'GMT', 'Linux', 'Programming',
                'SAC', 'SeisBasic', 'SeisWare', ]


def rst2pdf(rst, pdf):
    content = []
    toc = False

    # read rst file and do some replacement
    with open(rst) as f:
        for line in f:
            line = re.sub(
                "<{filename}/\w*/(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*).rst>",
                "<" + siteurl + "/" + r"\g<slug>.html>",
                line)
            line = re.sub(
                r".. figure:: /images/(\S)",
                r".. figure:: " + base + '/images/' + r"\1",
                line)
            content.append(line)

            if (line.startswith(".. contents::")):  # has tableofcontents
                toc = True

    # convert rst to PDF
    cmd = ["pandoc",
           "-f", "rst",
           "-t", "latex",
           "-o", pdf,
           "-s",
           "--template=seisman.latex",
           "--listings",
           "--number-sections",
           "--latex-engine=xelatex",
           "-V", "SITEURL=http://seisman.info",
           ]
    if (toc):
        cmd.append("--toc")
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    p.communicate(input=''.join(content).encode())


def md2pdf(md, pdf):
    meta = {}
    content = []
    with open(md) as f:
        for line in f:
            entry = line.strip().split(': ', 2)
            if len(entry) != 2:
                break
            meta[entry[0].lower()] = entry[1]

        for line in f:
            line = re.sub(
                "({filename}/\w*/(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*).rst)",
                siteurl + "/" + r"\g<slug>.html",
                line)
            line = re.sub(
                "({filename}/images/(?P<filename>))",
                base + "/images/" + r"\g<filename>",
                line)
            content.append(line)

    cmd = ["pandoc",
           "-f", "markdown",
           "-t", "latex",
           "-o", pdf,
           "-s",
           "--template=seisman.latex",
           "--listings",
           "--number-sections",
           "--latex-engine=xelatex",
           "-VSITEURL=http://seisman.info",
           ]
    for key, value in meta.items():
        cmd.append("-V" + key + "=" + value)

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    p.communicate(input=''.join(content).encode())

def post2pdf(src, pdf):
    filename, ext = os.path.splitext(src)

    print("%s => %s" % (os.path.split(src)[1], os.path.split(pdf)[1]))
    if ext == '.rst':
        rst2pdf(src, pdf)
    elif ext == '.md':
        md2pdf(src, pdf)


if __name__ == '__main__':
    # parser arguments
    arguments = docopt(__doc__)

    # create dir for PDF
    if not os.path.exists(pdfdir):
        os.makedirs(pdfdir)

    for root, dirs, files in os.walk(base):
        head, tail = os.path.split(root)
        if tail in article_dirs:
            for post in files:
                filename, ext = os.path.splitext(post)
                if ext not in ['.rst', '.md']:
                    continue

                pdf = filename.split('_')[1] + '.pdf'
                srcfile = os.path.join(root, post)
                pdffile = os.path.join(pdfdir, pdf)

                if arguments['--all']:
                    post2pdf(srcfile, pdffile)

                if arguments['--update']:
                    if not os.path.exists(pdffile):
                        post2pdf(srcfile, pdffile)
                    else:
                        src_mtime = os.path.getmtime(srcfile)
                        pdf_mtime = os.path.getmtime(pdffile)
                        if src_mtime > pdf_mtime:
                            post2pdf(srcfile, pdffile)

