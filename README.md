# Apple Card Statements can be converted into a nice CSV

only converts the transactions into a csv and doesn't parse all of them.

I felt this was useful because you could then use the csv and send it to 
anything that you would like to keep track of your expenses.

## How to get your pdf statement from Apple Card

To actually get your statements from your phone:
1. Open Wallet
2. Tap your Apple Card
3. Tap Total Balance
4. in Statements, tap on one of your existing statements
5. Tap Download as PDF Statement

I prefer to just airdrop that pdf to this local repository in `data/`

# How to convert your pdf statement to a csv


```
pip install requirements.txt
./convert.sh /path/to/pdf.pdf /path/to/output.csv
```

WARNING: There are some problems when converting from the PDF version to
the text version of the pdf. It makes it difficult to determine which
transaction is a part of which section sometimes. I added printing of the dataframe
in order to make sure you can see that all of your values align correctly. If they 
don't, then I suggest editing the file `/tmp/pdf_temp` where the intermediate
pdf is stored in order to make sure everything is parsed correctly from the pdf.
