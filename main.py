from boat import Boat
def main():

    boats = [Boat(make='Sealine', model='S34', year=2019, length=12.5, serial_number='123456789'),
            Boat(make='Bavaria', model='Cruiser 41', year=2018, length=12.5, serial_number='987654321'),
            Boat(make='Jeanneau', model='Sun Odyssey 349', year=2017, length=11.5, serial_number='456789123'),
            Boat(make='Beneteau', model='Oceanis 38', year=2016, length=11.0, serial_number='321456789')]

    # TODO 1: Ergänzen Sie die Klasse Boot um die Methode __str__ in der die Attribute des Bootes ausgegeben werden.

    # TODO 2: Passen Sie das folgende Codestück so an, dass nicht mehr printInfos() verwendet wird,
    #  sondern die __str__() Methode.
    #        Die Ausgabe soll wie folgt aussehen:
    #        Make: Sealine, Model: S34, Year: 2019, Length: 12.5, Serial Number: 123456789
    #        Make: Bavaria, Model: Cruiser 41, Year: 2018, Length: 12.5, Serial Number: 987654321
    #        Make: Jeanneau, Model: Sun Odyssey 349, Year: 2017, Length: 11.5, Serial Number: 456789123
    #        Make: Beneteau, Model: Oceanis 38, Year: 2016, Length: 11.0, Serial Number: 321456789

    for boat in boats:
        boat.print_infos()

    # TODO 3: Testen Sie Ihre Lösung mir dem Testfall 'test_first_output', anschliessend
    #  Commiten und Pushen Sie die Lösung.

    # TODO 4: Machen Sie ihre Boote zuerst nach Länge (aufsteigend) und dann nach Jahrgang (aufsteigend) vergleichbar

    # TODO 5: Sortieren Sie die Boote nach Länge und dann nach Jahrgang

    # TODO 6: Geben Sie die sortierte Liste der Boote aus

    # TODO 7: Testen Sie Ihre Lösung mir dem Testfall 'test_after_sorting_output', anschliessend
    #  Commiten und Pushen Sie die Lösung.

if __name__ == '__main__':
    main()