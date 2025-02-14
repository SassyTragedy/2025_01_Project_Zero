# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)


# Main Routine goes here
make_statement(statement="Programming is Fun!", decoration="👍", lines: 1)
