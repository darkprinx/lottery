import os


def main():
    name = os.environ.get("INPUT_NAME")
    print(f"👋 Hello from Python, {name}!")
    with open(os.environ["GITHUB_OUTPUT"], "a") as gh_out:
        print(f"greeting=Hello from Python, {name}!", file=gh_out)


if __name__ == "__main__":
    main()
