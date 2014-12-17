import csv
import ntpath


def fix_turnstile_data(filenames):
    """
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved.

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:

    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    """

    for name in filenames:
        with open(name, 'rb') as f:
            reader = csv.reader(f)
            result = []
            rowslice = 5

            for row in reader:
                colstart = 3
                colend = colstart + rowslice
                rowlen = len(row)

                while colend <= rowlen:
                    current = [row[0]] + [row[1]] + [row[2]]

                    # add rest of the row
                    for x in range(colstart, colend):
                        current += [row[x]]

                    # add row to result
                    if current:
                        result.append(current)

                    colend += rowslice
                    colstart += rowslice

        new_filename = ntpath.dirname(name) + r'\updated_' + ntpath.basename(name)
        with open(new_filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(result)


fix_turnstile_data([r'Data\turnstile_110528.txt'])


# ['A002', 'R051', '02-00-00',
# '05-21-11', '00:00:00', 'REGULAR', '003169391', '001097585',
# '05-21-11', '04:00:00', 'REGULAR', '003169415', '001097588',
# '05-21-11', '08:00:00', 'REGULAR', '003169431', '001097607',
# '05-21-11', '12:00:00', 'REGULAR', '003169506', '001097686',
# '05-21-11', '16:00:00', 'REGULAR', '003169693', '001097734',
# '05-21-11', '20:00:00', 'REGULAR', '003169998', '001097769',
# '05-22-11', '00:00:00', 'REGULAR', '003170119', '001097792',
# '05-22-11', '04:00:00', 'REGULAR', '003170146', '001097801              ']