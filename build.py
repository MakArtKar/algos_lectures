from os import popen
from os import system

dirs = popen('ls tex_files').read().split()
for filename in dirs:
    filename = filename[:-4]
    system('pdflatex -shell-escape -synctex=1 tex_files/' + filename + '.tex')
    system('mv ' + filename + '.pdf pdf_files')
    system('rm ' + filename + '*')
system('rm -rf _minted*')
system('rm *.log')