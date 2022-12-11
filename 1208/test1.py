def main():
    a = input("please int")
    try:
        b = int(a)
    except TypeError:
        print("typeError")
    except ValueError:
        print("jhgkj")
    except KeyboardInterrupt:
        print("kbditrpt")


if __name__ == '__main__':
    main()