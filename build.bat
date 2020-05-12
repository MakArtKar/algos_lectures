@echo off

for /r tex_files %%i in (*) do (
  pdflatex -shell-escape -synctex=1 %%i
  move %%~ni.pdf pdf_files
  del %%~ni*
)

for /f %%i in ('dir /a:d /b _minted*') do rmdir /s /q %%~ni
del *.log
