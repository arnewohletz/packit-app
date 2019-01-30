import parse


@parse.with_pattern(r"not\s+")
def parse_word_not(text):
    """Type converter for "not " (followed by one/more spaces)."""
    return text.strip()
