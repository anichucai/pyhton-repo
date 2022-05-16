from module.lib.cli import CLI


def sum(a, b):
    return a + b


def main():
    args = CLI().parse_args()

    print(
        "If you read this line it means that you have provided "
        "all the parameters which are:"
    )
    print(args)


main()
