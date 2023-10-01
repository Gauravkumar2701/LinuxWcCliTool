import typer
import os

app = typer.Typer()

def wc(
        arg1: typer.FileText = typer.Option(None, "--lines", "-l", help="Print the new lines"),
        arg2: typer.FileText = typer.Option(None, "--bytes", "-c", help="Print the size"),
        arg3: typer.FileText = typer.Option(None, "--words", "-w", help="Print the number of words"),
        arg4: typer.FileText = typer.Option(None, "--chars", "-m", help="Print the number of char"),
        arg5: str = typer.Option(None, "-a", help="Print all")
):
    if arg1:
        print(getNumberOfLines(arg1), arg1.name)

    elif arg2:
        print(getNumberOfBytes(arg2), arg2.name)

    elif arg3:
        print(getNumberOfWords(arg3), arg3.name)

    elif arg4:
        print(getTheNumberOfChars(arg4), arg4.name)

    else:
        getAll(arg5)


def getTheNumberOfChars(file):
    count = 0

    for line in file:
        numberOfWords = line.split(" ")

        for word in numberOfWords:

            if word != " ":
                for char in word:
                    if char != " ":
                        count += 1

    return count


def getNumberOfWords(file):
    count = 0
    for line in file:

        numberOfWords = line.split(" ")

        for word in numberOfWords:

            if word != " ":
                count += 1

    return count


def getAll(file):
    with open(file, mode='r') as f:

        data = f.readlines()
        charCount = 0
        wordCount = 0

        for line in data:

            word = line.split(" ")

            for w in word:
                if w != " ":
                    wordCount += 1

            for char in line:
                if char != " ":
                    charCount += 1

        print(len(data), os.fstat(f.fileno()).st_size, wordCount, charCount, f.name)


def getNumberOfBytes(file):
    return os.fstat(file.fileno()).st_size


def getNumberOfLines(file):
    count = 0

    for line in file.buffer:
        count += 1

    return count


if __name__ == "__main__":
    typer.run(wc)



