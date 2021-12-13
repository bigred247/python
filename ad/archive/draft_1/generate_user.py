import io
import csv,sys #calling csv and sys modules
actual_header="First Name|Last Name|DOB|Gender|Email|Telephone"

#read file (r means read only)
##opening of file to read contents  ##f1 is an object which buffers the contents of list 
 ##then f1 is called here with a var name of data to read
  ##closing of file otherwise contents of file get buffered in memory 
with io.open("test.csv","r",encoding="utf")as f1:  
    data=f1.read()
    f1.close()


#validate header count and header fields
#converting into a list which contains every line as single element
#the -1 excludes 1 line which is the header line
data=data.split("\n")
total_line=len(data)-1
print(f"file has {total_line} lines")

#read the output.csv ##add the first value in manually based on number of lines initially in test.csv
with open("output.csv")as f3:
    data_from_output=csv.reader(f3,delimiter=",")
    for row in data_from_output:
        percentage=total_line
        #calculation based on the given percentage 
        #row[0] is the value taken from the output.csv file. You must manually add one in to start off with 
        #0.6 below refers to 60%
        if(percentage>(int(row[0])+int(row[0])*.6)):
            #print and exit
            print("huge number of changes coming")
            #exit from code
            sys.exit()

#get header from file
header=data[0]
print(header)
if(header==actual_header):
    print("file header is ok")
    #assign line number for first user in test.csv ##line 1 is header
    line_number=2
    #iterating through the loop
    #eliminating the header which is 1. [1:] is 1 til the last value
    for row in data[1:]:
        #converting into a list which contains every line as single element separated by pipe character
        delimiter_count=row.split("|")
        #get the count (len) of elements (header values) in file
        delimiter_from_file=len(delimiter_count)
        #comparing with actual element count ## 6 is taken from actual headers "First Name|Last Name|DOB|Gender|Email|Telephone"
        if(delimiter_from_file==6):
            #print with line number
            print(f"{line_number}, delimiters are ok")
            #getting attribute Email [4}] & last name [1]
            mail=delimiter_count[4]
            sn=delimiter_count[1]
            #check if the mail and sn attributes exist for a user or not
            if(mail and sn):
                #if the test.csv file has  values populated for mail and surname
                print("value is here")
            else:
                #if email or surname is misisng than print "no value"
                print("no value")
        

        else:
            #print with line number
            print(f"{line_number}, delimiters are not ok")

        line_number=line_number+1


else:
    print("header is not correct please validate")

#write the last execute row count into output csv   (w means read only) 
#only writes to output.csv if meets the above conditions otherwise script exits
with io.open("output.csv","w",encoding="utf-8")as f2:
    f2.write(str(total_line)+"\n")
    f2.close()
