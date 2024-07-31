all: prepare

prepare:
	./bin/make_pub.py
	./bin/make_cv.py
	cd cv && make && cp cv.pdf ../static
	hugo
