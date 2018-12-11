import re


HTML_START_TAG_PATTERN = re.compile(r'<\s*[a-z]\s*([a-z]+="[\w\.]+")*>')

def findtags(text):
    """
    Return a list of all the html start tags in the text.
    """
    matches = re.finditer(HTML_START_TAG_PATTERN, text)
    return [match.group() for match in matches]
