#! /usr/bin/env make
all: report.html report.pdf

report.html : text.txt ViEWSMapGridCell.png
	pandoc text.txt -s --mathjax -f markdown+tex_math_dollars -o report.html
	
report.pdf : text.txt ViEWSMapGridCell.png
	pandoc text.txt -s --mathjax -f markdown+tex_math_dollars -o  report.pdf
	
text.txt : approach.txt conclusion.txt litReview.txt preamble.txt results.txt
	cat preamble.txt litReview.txt approach.txt results.txt conclusion.txt >> text.txt
