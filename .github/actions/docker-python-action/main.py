import os

def main():
    name = os.environ.get('INPUT_NAME', 'World')
    print(f'Hello {name} from Python Docker Action!')
    print(f'::set-output name=greeting::Hello {name} from Python Docker Action!')

if __name__ == "__main__":
    main()
