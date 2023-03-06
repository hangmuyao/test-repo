#! /usr/bin/env make

report.html : text.txt ViEWSMapGridCell.png
	pandoc text.txt -s --mathjax -f markdown+tex_math_dollars -t html -o report.html
	
text.txt : approach.txt conclusion.txt litReview.txt preamble.txt results.txt
	cat preamble.txt litReview.txt approach.txt results.txt conclusion.txt >> text.txt
