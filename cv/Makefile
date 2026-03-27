all: gen
	../bin/latexrun -Wall cv-gen.tex -o cv.pdf

gen:
	../bin/make_cv.py

clean:
	rm -rf *.out *.pdf *.aux latex.out

.PHONY: all gen clean
