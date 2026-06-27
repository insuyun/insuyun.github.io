MAIN = research_statement

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	latexmk -pdf -interaction=nonstopmode $(MAIN).tex

watch:
	latexmk -pdf -pvc -interaction=nonstopmode $(MAIN).tex

clean:
	latexmk -C
	rm -f *.bbl *.run.xml *.synctex.gz

.PHONY: all watch clean
