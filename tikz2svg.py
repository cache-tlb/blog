#!/usr/bin/env python
#
# author: github.com/jbenet
# license: MIT
#
# tikz2svg: convert tikz input into svg
# depends on:
# - pdflatex: comes with your tex dist
# - pdf2svg: brew install pdf2svg

import os
import sys
import hashlib
import functools
from subprocess import Popen, PIPE


class cmds(object):
  pdflatex = 'xelatex --shell-escape -file-line-error -interaction=nonstopmode ../temp.tex'
  pdf2svg = 'pdf2svg texput.pdf out.svg'


latex_doc =r'''
\documentclass[border=2bp]{standlone}
\usepackage{tikz}
\begin{document}
\begingroup
\tikzset{every picture/.style={scale=1}}
  \begin{tikzpicture}[cap=round,scale=3.5]
  \definecolor{qqwuqq}{rgb}{0,0.39215686274509803,0}
  \definecolor{ududff}{rgb}{0.30196078431372547,0.30196078431372547,1}
  \definecolor{uuuuuu}{rgb}{0.26666666666666666,0.26666666666666666,0.26666666666666666}  
  \def\a{0}
  \def\b{1}
  \def\c{1.5}
  \def\d{1.875}
  \def\e{2.1875}
  \def\f{2.4609375}
  \def\ab{0.5}
  \def\bc{1.25}
  \def\cd{1.6875}
  \def\de{2.03125}
  \clip(-0.5,-0.15) rectangle (2.8,2.8);
  \def\mylist{0/0,1/1,1.5/{3/2},1.875/{15/8},2.1875/{35/16},2.4609375/{$ \cdots $}}
  \foreach \xx/\label in \mylist{
    \draw [line width=0.5pt,dashed] (0,\xx) -- (10,\xx);
    \draw [line width=0.5pt,dashed] (\xx,0) -- (\xx,10);
    \draw (\xx,-0.03) node[anchor=north] {\label};
    \draw (-0.03,\xx) node[anchor=east] {\label};
  }
  \draw [line width=1pt] (\a,\a) -- (\a,\e) -- (\b,\e) -- (\b,\d) -- (\c,\d) -- (\c,\c) -- (\d,\c) -- (\d,\b) -- (\e,\b) -- (\e,\a) -- (\a,\a) ;
  \draw (\ab,\ab) node {$R_{0,0}$};
  \draw (\ab,\bc) node {$R_{0,1}$};
  \draw (\ab,\cd) node {$R_{0,2}$};
  \draw (\ab,\de) node {$R_{0,3}$};
  \draw (\bc,\ab) node {$R_{1,0}$};
  \draw (\bc,\bc) node {$R_{1,1}$};
  \draw (\bc,\cd) node {$R_{1,2}$};
  \draw (\cd,\ab) node {$R_{2,0}$};
  \draw (\cd,\bc) node {$R_{2,1}$};
  \draw (\de,\ab) node {$R_{3,0}$};
  \def\xx{2.4457}
  \def\yy{2.0252}
  \draw[dashed,red,line width=1pt] (\xx,0) arc [start angle=0, end angle=90, radius=\xx];
  \draw[dashed,green,line width=1pt] (\yy,0) arc [start angle=0, end angle=90, radius=\yy];
  \end{tikzpicture}
\endgroup
\end{document}
'''

# util to run command in a subprocess, and communicate with it.
def run(cmd, stdin=None, exit_on_error=True):
  # print '>', cmd
  p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
  if stdin:
    p.stdin.write(stdin)
    p.stdin.close()
  p.wait()

  # error out if necessary
  if p.returncode != 0 and exit_on_error:
    print '>', cmd
    print 'Error.'
    print '-' * 20, 'STDIN'
    print stdin
    print '-' * 20, 'STDOUT'
    print p.stdout.read()
    print '-' * 20, 'STDERR'
    print p.stderr.read()
    sys.exit(p.returncode)

  return p.stdout.read()

# memoize with a file cache.
def memoize_in_file(fn):
  @functools.wraps(fn)
  def memoized(*args, **kwds):
    i = fn.__name__ + str(*args) + str(**kwds)
    h = hashlib.sha1(i).hexdigest()
    if os.path.exists(h):
      with open(h) as f:
        return f.read()

    out = fn(*args, **kwds)
    with open(h, 'w') as f:
      f.write(out)
    return out
  return memoized


# conversion functions
def tikz2tex(tikz):
  return latex_doc % {'content': tikz}

def tex2pdf(tex):
  return run(cmds.pdflatex.split(' '), stdin=tex)

def pdf2svg(pdf):
  run(cmds.pdf2svg)
  with open('out.svg') as f:
    return f.read()

@memoize_in_file
def tikz2svg(tikz):
  tex = tikz2tex(tikz)
  pdf = tex2pdf(tex)
  svg = pdf2svg(pdf)
  return svg

# move to tmp because latex litters :(
def chdir(inp):
  h = hashlib.sha1(inp).hexdigest()
  d = './tmp/%s' % h
  try:
    os.makedirs(d)
  except OSError:
      pass
#   run('mkdir -p %s' % d, exit_on_error=False)
  os.chdir(d)

if __name__ == '__main__':
  if '-h' in sys.argv or '--help' in sys.argv:
    print 'Usage: %s [<file>]' % sys.argv[0]
    print 'Outputs svg conversion of tikz input (files or stdin).'
    sys.exit(0)

  import fileinput
  lines = ''.join([l for l in fileinput.input()])
  chdir(lines)
  print tikz2svg(lines)