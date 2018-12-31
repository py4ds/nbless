def write_file(filename: str, contents: str) -> None:
    """Writes contents to a file with a given filename
    Args:
        filename: The name of the target file
        contents: The contents of the target file
    Examples:
        >>> import tempfile
        >>> outfile_path = tempfile.mkstemp()[1]
        >>> write_file(outfile_path, "Test file contents")
        >>> with open(outfile_path) as file:
        ...     file.read()
        'Test file contents'
    """
    with open(filename, "w") as f:
        f.write(contents)
