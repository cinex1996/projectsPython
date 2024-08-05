def main():
    table = {}
    while True:
        value = input("Wprowadź nazwę miasta ")
        if value == "":
            break
        else:
            valuesecond = int(input("Wprowadź zestawienie opadu deszczu"))
            if value in table:
                x = table.get(value)
                valuesecond = valuesecond + x
                table.update({value: valuesecond})
                print({value: valuesecond})
            else:
                table.update({value: valuesecond})
                print({value: valuesecond})


if __name__ == "__main__":
    main()
