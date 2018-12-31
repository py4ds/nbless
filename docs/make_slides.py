import pypandoc
import functools

def write_file(filename: str, contents: str) -> None:
    """Writes contents to a file with a given filename
    Args:
        filename: The name of the target file
        contents: The contents of the target file
    Examples:
        >>> outfile_path = tempfile.mkstemp()[1]
        >>> write_file(outfile_path, "Test file contents")
        >>> with open(outfile_path) as file:
        ...     file.read()
        'Test file contents'
    """
    with open(filename, 'w') as f:
        f.write(contents)


def make_slides(source: str = 'habits.md', target: str = 'revealjs') -> str:
    """Creates a HTML slideshow based on a source file
    :param source: The filepath of the target file
    :param target: The target format of return string
    :return: A string of characters that are the contents of an HTML slideshow
    :raise ValueError: If target is not 'slidy', 'dzslides', or 'revealjs'
    """
    part = functools.partial(pypandoc.convert_file, source, to=target)
    if target in ('slidy', 'dzslides', 'revealjs'):
        return (part(extra_args=['-s']) if target is not 'revealjs' else
               part(extra_args=['-sV', 'revealjs-url=https://revealjs.com']))
    else:
        raise ValueError(f"{target} is not one of the 3 supported targets.")

if __name__ == "__main__":
    write_file('slides.html', make_slides())
