TARGET?=poster

.PHONY: $(TARGET).pdf
$(TARGET).pdf: $(TARGET).tex example.pdf
	pdflatex -shell-escape $(TARGET).tex
	pdflatex -shell-escape $(TARGET).tex
	pkill -HUP mupdf

example.pdf: drawmodel.py example.yaml
	python drawmodel.py example.yaml $@

clean:
	rm -f $(TARGET).pdf
	rm -f $(TARGET).{aux,dvi,nav,snm,bbl,blg,log,out,toc,lof,lot,glsdefs}
	rm -rf _minted-$(TARGET)
	rm -f example.pdf
