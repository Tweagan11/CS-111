from byu_pytest_utils import max_score, run_python_script, test_files, this_folder, ensure_missing

def convert_file(filename):
    from platform import system
    if system() == "Windows":
        import re
        with open(filename, "rb") as fin:
            buffer = re.sub(b"\r\n", b"\n", fin.read())
        with open(filename, "wb") as fout:
            fout.write(buffer)
    return filename


@ensure_missing(this_folder / 'sample.output.txt')
@max_score(6)
def test_sample_scavenger_hunt():
    with open(test_files / 'sample.key.png', 'rb') as fin:
        expected = fin.read()

    run_python_script('lab21.py', 'https://cs111.cs.byu.edu/lab/lab21/assets/sample1.html',
                      'li', 'checkpoint1', this_folder / 'sample.output.txt')
    convert_file(this_folder / 'sample.output.txt')
    with open(this_folder / 'sample.output.txt', 'rb') as fin:
        observed = fin.read()

    assert observed == expected


@ensure_missing(this_folder / 'mediumhunt.output.txt')
@max_score(7)
def test_medium_scavenger_hunt():
    with open(test_files / 'mediumhunt.key.png', 'rb') as fin:
        expected = fin.read()

    run_python_script('lab21.py', 'https://cs111.cs.byu.edu/lab/lab21/assets/webpage1.html',
                      'p', 'mediumhunt-checkpoint1', this_folder / 'mediumhunt.output.txt')
    convert_file(this_folder / 'mediumhunt.output.txt')
    with open(this_folder / 'mediumhunt.output.txt', 'rb') as fin:
        observed = fin.read()

    assert observed == expected


@ensure_missing(this_folder / 'longhunt.output.txt')
@max_score(7)
def test_long_scavenger_hunt():
    with open(test_files / 'longhunt.key.png', 'rb') as fin:
        expected = fin.read()

    run_python_script('lab21.py', 'https://cs111.cs.byu.edu/lab/lab21/assets/webpage4.html',
                      'ul', 'longhunt-checkpoint1', this_folder / 'longhunt.output.txt')
    convert_file(this_folder / 'longhunt.output.txt')
    with open(this_folder / 'longhunt.output.txt', 'rb') as fin:
        observed = fin.read()

    assert observed == expected
