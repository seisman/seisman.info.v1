#!/usr/bin/env python
"""Convert rST to PDF

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


def read_rst(rst):
    lines = []
    with open(rst) as f:
        for line in f:
            lines.append(line)

    return lines


def update_rst(lines):
    content = []
    for line in lines:
        line = re.sub(
            "<{filename}/\w*/(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*).rst>",
            "<" + siteurl + "/" + r"\g<slug>.html>", line)
        line = re.sub(
            r".. figure:: /images/(\S)",
            r".. figure:: " + base + '/images/' + r"\1",
            line)
        content.append(line)

    return content


def write_pdf(content, pdf):
    p = subprocess.Popen(
        ["pandoc",
         "-f", "rst",
         "-t", "latex",
         "-o", pdf,
         "-s",
         "--template=seisman.latex",
         "--toc",
         "--listings",
         "--number-sections",
         "--latex-engine=xelatex",
         "-V", "SITEURL=http://seisman.info",
         ],
        stdin=subprocess.PIPE)
    out = ''.join(content)
    p.communicate(input=out.encode())


def rst2pdf(rst, pdf):
    print("%s => %s" % (os.path.split(rst)[1], os.path.split(pdf)[1]))
    content = read_rst(rst)
    updated_content = update_rst(content)
    write_pdf(updated_content, pdf)


if __name__ == '__main__':
    # parser arguments
    arguments = docopt(__doc__)

    # create dir for PDF
    if not os.path.exists(pdfdir):
            os.makedirs(pdfdir)

    for root, dirs, files in os.walk(base):
        head, tail = os.path.split(root)
        if tail in article_dirs:
            for rst in files:
                filename, ext = os.path.splitext(rst)
                if ext != '.rst':
                    continue

                pdf = filename.split('_')[1] + '.pdf'
                rstfile = os.path.join(root, rst)
                pdffile = os.path.join(pdfdir, pdf)

                if arguments['--all']:
                    rst2pdf(rstfile, pdffile)

                if arguments['--update']:
                    if not os.path.exists(pdffile):
                        rst2pdf(rstfile, pdffile)
                    else:
                        rst_mtime = os.path.getmtime(rstfile)
                        pdf_mtime = os.path.getmtime(pdffile)
                        if rst_mtime > pdf_mtime:
                            rst2pdf(rstfile, pdffile)
