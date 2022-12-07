def main():
    a = 'My name is {a}, my age is {b}, my signature phrase is {b}{b}{b}.'
    print(a.format(a='Pepe', b='6'))
    b = "{name} have {money:+.4f}$ in his credit card."
    print(b.format(name="Pepe", money=9999999.99999))


if __name__ == '__main__':
    main()
