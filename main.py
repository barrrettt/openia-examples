import modules
import modules.my_open_ia


def main():
    print("🚀 Hello openIA! ")
    modules.my_open_ia.setup()
    res = modules.my_open_ia.get_completion("Hello, how are you?")
    print(res)
    print("🎉 Done! ")

if __name__ == "__main__":
    main()