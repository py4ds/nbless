from subprocess import call

call('ls ' +  '-l', shell=True)
call('Rscript -e \'rmarkdown::render("cat.Rmd", "all")\'', shell=True)
call('jupyter nbconvert --to notebook --execute raw.ipynb --output out.ipynb', shell=True)


