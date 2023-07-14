all: prepare

prepare:
	./bin/make_cv.py
	cd cv && make && cp cv.pdf ../static
	hugo
