import subprocess
from pathlib import Path


def pytest_sessionstart(session):
    root = Path(__file__).parent
    exe = root / "main"

    subprocess.run(
        ["g++", "-Wall", "-Wextra", "--std=c++17", "main.cpp", "-o", str(exe)],
        cwd=root,
        check=True,
    )

    cases = [
        ("30 25 10\n", "result1.txt"),
        ("5 3 8\n", "result2.txt"),
        ("-5 -10 -1\n", "result3.txt"),
        ("-2 5 7\n", "result4.txt"),
    ]

    for data, filename in cases:
        with open(root / filename, "w") as output:
            subprocess.run(
                [str(exe)],
                cwd=root,
                input=data,
                text=True,
                stdout=output,
                check=True,
            )
