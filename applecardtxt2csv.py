import sys
import argparse
import pandas as pd
import pdfminer.high_level

parser = argparse.ArgumentParser(description='Turn your apple card pdf statements into a csv file')
parser.add_argument('file',
                    help='a text file that contains the output of pdf2txt.py from an apple card statement pdf')
parser.add_argument('savefile',
                    help='a text file that will contain your apple card statement as a csv')

args = parser.parse_args()

def is_start(data, i):
    if data[i] == "Amount" and data[i+1] == data[i+2]:
        return False
    return data[i] in starters

def is_end(data, i):
    # if data[i] == "" and data[i+1] == "Statement":
    #     return True
    return data[i] in enders

def get_column(data, i):
    return data[i]

starters = [
    "Date",
    "Daily Cash",
    "Description",
    "Amount"
]
enders = [
    "Apple Card is issued by Goldman Sachs Bank USA, Salt Lake City Branch, Lockbox 6112, P.O. Box 7247, Philadelphia, PA 19170-6112.",
    "Apple Card Customer",
    "Total charges, credits and returns",
    "Statement",
    "Interest Charged",
    "Date",
    "Daily Cash",
    "Description",
    "Amount"
]

def main(args=None):
    values = {}
    data_start = "Transactions"
    data_end = "Interest Charges"


    filename = args.file
    with open(filename, "r") as fp:
        data = fp.read().split('\n')
        transactions_started = False
        column = False
        logging = False
        for i in range(len(data)):
            if data[i] == data_start:
                transactions_started = True
            if data[i] == data_end:
                transactions_started = False
            if (transactions_started):
                if (logging and is_end(data,i)):
                    logging = False
                if (not logging and is_start(data, i)):
                    column = get_column(data, i)
                    logging = True

                if logging and not is_start(data, i):
                    # print(data[i])
                    if column not in values:
                        values[column] = []
                    values[column].append(data[i])


        max_len = 0
        for i in values:
            if len(values[i]) > max_len:
                max_len = len(values[i])
        for i in values:
            while( len(values[i]) < max_len ):
                values[i].append("")

        df = pd.DataFrame(values)

        for (index, row) in df.iterrows():
            if row["Date"] != "" and row["Description"] == "":
                for (i, slot) in enumerate(values):
                    if slot == "Date":
                        values[slot].insert(index, "")
                    else:
                        values[slot].append("")

        df = pd.DataFrame(values)
        # print(df.to_string())
        df.to_csv(args.savefile, index=False)
    return 0


if __name__ == '__main__': sys.exit(main(args))
