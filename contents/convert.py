import pybtex
txt = pybtex.format_from_file("pubs.bib", style="plain", output_backend="markdown")

txt = txt.replace("Jacob Miller", "<b>Jacob Miller </b>")

with open("publications.md", "w") as fdata:
    fdata.write(txt)