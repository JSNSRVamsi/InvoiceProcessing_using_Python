import pdfplumber
import re
import pandas
from datetime import datetime


def invoice (Inputpath,Outputpath):
    final = []
#    os.rename(r'Outputpath')
#with open("out.csv","w",newline="") as f: 
    with pdfplumber.open(Inputpath) as pdfObj:
        NoPages = len(pdfObj.pages)
        final.append(["Invoice#","Amount"])
        for i in range(0,NoPages):
            text=pdfObj.pages[i].extract_text()
#            print(text)
            invoice = re.compile(r'^(([1-9]|(3)[0-1])|([0-2][0-9]|(3)[0-1]))(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4} (\d{8}|[A-Z].*)')
            invoice_1 = re.compile(r'^(\d{8}) (([1-9]|(3)[0-1])|([0-2][0-9]|(3)[0-1]))(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}.*')
            for a in text.split('\n'):
#                print(a)
                if invoice.match(a):
                    l=len(a.split())
                    if l == 5:
                        date, name, Invoice, amt1, amt2 = a.split()
                        temp = []
                        temp.append(Invoice)
                        temp.append(amt1)
                        final.append(temp)
                    elif l == 3:
                            date, Invoice, amt1 = a.split()
                            temp = []
                            temp.append(Invoice)
                            temp.append(amt1)
                            final.append(temp)
                if invoice_1.match(a):
                    l=len(a.split())
                    if l == 4:
                        Invoice, date, amt1, amt2 = a.split()
                        temp = []
                        temp.append(Invoice)
                        temp.append(amt1)
                        final.append(temp)
                    elif l == 3:
                            date, Invoice, amt1 = a.split()
                            temp = []
                            temp.append(Invoice)
                            temp.append(amt1)
                            final.append(temp)
        myprint = pandas.DataFrame(final)
        now=datetime.now()
        timestamp = str(now.strftime("%Y%m%d_%H%M%S"))
        Outputpath = Outputpath.replace('file','FinalInvoice_'+ timestamp)
        myprint.to_csv(Outputpath)
        pdfObj.close()


invoice('C:/Automations/Invoice/ABCD.pdf','C:/Automations/Invoice/CDEF/file.csv')
