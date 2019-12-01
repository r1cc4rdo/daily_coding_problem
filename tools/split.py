from pathlib import Path

test_string = """


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
"""


def split():
    files = sorted(Path('.').glob('daily*.py'))
    for filename in files:
        divider = 'def coding_problem_'
        declarations, *problems = filename.read_text().split(divider)
        for index, problem in enumerate(problems):

            content = declarations + divider + problem.rstrip()
            before, comment, after = content.split('"""')
            test = test_string if index != (len(problems) - 1) else ''
            num = int(problem.split("(")[0])

            p = (Path('problems') / f'{num:02}' / f'problem_{num:02d}.py')
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(before + '"""' + comment + '"""\n    pass' + test)

            (Path('problems') / f'{num:02}' / f'solution_{num:02d}.py').write_text(before + '"""' + comment + '"""' + after + test)

            lines = [s.strip() for s in comment.strip().split('\n')]

            within_test = False
            for index, line in enumerate(lines):
                if line.startswith('>>>'):
                    lines[index] = '    ' + line
                    within_test = True
                else:
                    if within_test:
                        lines[index] = '    ' + line
                    within_test = False

            (Path('problems') / f'{num:02}' / f'README.md').write_text(f'##Problem {num}\n\n' + '\n'.join(lines))


if __name__ == '__main__':
    split()
