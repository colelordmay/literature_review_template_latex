This is a LaTeX template to put together large/maintainable literature review documents.
I've included two examples from one of my lit review documents. I'm unsure of the legality here, so I picked two old papers. Normally I also have a subfolder "papers" with all of the pdfs included.

Additionally included is the "sort.py" file. This will sort the entries of both your .bib and .tex files alphabetically. Makes it much easier to read when the files get big. I couldn't find any simple python codes to do this (only lots of Perl code and complicated .tex that I don't understand). That said, the implementation requires:
1. In the .tex file, each section must start with `\def \sect {...}`
2. Each section must end with `\newpage` with no other uses of `\newpage` in the document (except after the table of contents)

I highly suggest backing up your .tex and .bib files before using for the first time.