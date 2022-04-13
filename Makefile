all: prepare

prepare:
	./bin/make_cv.py
	cd cv && ../bin/latexrun -Wall cv-gen.tex -o ../static/cv.pdf
