import main

def test_first_output(capsys):
    main.main()
    captured = capsys.readouterr()
    # copy the first four lines of the output
    lines = captured.out.splitlines()
    assert lines[0] == 'Make: Sealine, Model: S34, Year: 2019, Length: 12.5, Serial Number: 123456789'
    assert lines[1] == 'Make: Bavaria, Model: Cruiser 41, Year: 2018, Length: 12.5, Serial Number: 987654321'
    assert lines[2] == 'Make: Jeanneau, Model: Sun Odyssey 349, Year: 2017, Length: 11.5, Serial Number: 456789123'
    assert lines[3] == 'Make: Beneteau, Model: Oceanis 38, Year: 2016, Length: 11.0, Serial Number: 321456789'

def test_after_sorting_output(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out ==  'Make: Sealine, Model: S34, Year: 2019, Length: 12.5, Serial Number: 123456789\n' \
                            'Make: Bavaria, Model: Cruiser 41, Year: 2018, Length: 12.5, Serial Number: 987654321\n' \
                            'Make: Jeanneau, Model: Sun Odyssey 349, Year: 2017, Length: 11.5, Serial Number: 456789123\n' \
                            'Make: Beneteau, Model: Oceanis 38, Year: 2016, Length: 11.0, Serial Number: 321456789\n' \
                            'Make: Beneteau, Model: Oceanis 38, Year: 2016, Length: 11.0, Serial Number: 321456789\n' \
                            'Make: Jeanneau, Model: Sun Odyssey 349, Year: 2017, Length: 11.5, Serial Number: 456789123\n' \
                            'Make: Bavaria, Model: Cruiser 41, Year: 2018, Length: 12.5, Serial Number: 987654321\n' \
                            'Make: Sealine, Model: S34, Year: 2019, Length: 12.5, Serial Number: 123456789\n'