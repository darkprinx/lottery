import os

def main():
    name = os.environ.get('INPUT_NAME', 'World')
    print(f"👋 Hello from Python, {name}!")
    print(f"echo 'greeting=Greetings from {name}' >> $GITHUB_OUTPUT")

if __name__ == "__main__":
    main()
