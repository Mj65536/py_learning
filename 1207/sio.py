def main():
    import io
    s = 'Okay'
    sio = io.StringIO(s)
    print(sio)
    print(sio.getvalue())
    sio.seek(2)
    print(sio.write('s'))
    print(sio.getvalue())


if __name__ == '__main__':
    main()
