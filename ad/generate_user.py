import io
actual_header="First Name|Last Name|DOB|Gender|Email|Telephone"

#read file (r means read only)
with io.open("test.csv","r",encoding="utf-8")as f1: ##opening of file to read contents ##f1 just an object which gets on line 6
    data=f1.read() 
    f1.close() ##closing of file after reading contents

#validate header count and header fields
#converting into a list which contains every line as single element
data=data.split("\n")
#get header from file
header=data[0]
print(header)
if(header==actual_header):
    print("file header is ok")
    #assign line number
    line_number=2
    #iterating through the loop
    #eliminating the header
    for row in data[1:]:
        #converting into a list which contains every line as single element separated by pipe character
        delimiter_count=row.split("|")
        #geeting the count of elemenmts inside the list
        delimiter_from_file=len(delimiter_count)
        #comparing with actual element count
        if(delimiter_from_file==6):
            #print with line number
            print(f"{line_number}, delimiters are ok")
             #getting attribute mail & last name
            mail=delimiter_count[4]
            sn=delimiter_count[1]
            #checking if the mail attribute has value or not
            if(mail and sn):
                #if has value
                print("value is here")
            else:
                #if has no value
                print("no value")
        else:
            #print with line number
            print(f"{line_number}, delimiters are not ok")
        line_number=line_number+1
else:
    print("header is not correct please validate")