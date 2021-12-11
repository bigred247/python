from typing import Optional
from pyad import *
import io

ou=pyad.adcontainer.ADContainer.from_dn("OU=devops-lab,DC=devops-lab,DC=com")

def add_user(row):
  print(row)
  user_attributes=row.split("|")
  #calls the test.csv file attributes
  givenName=user_attributes[0]
  sn=user_attributes[1]
  description=user_attributes[2]
  personalTitle=user_attributes[3]
  mail=user_attributes[4]
  telephoneNumber=user_attributes[5]
  #splits the file and uses the left side eg. username portion of email as unqiue userID
  sAMAccountName=mail.split("@")[0]
  #combines first name and last name for display name
  displayName=givenName+", "+sn
  #optional syntax below generates the map of users from csv file (key value for AD is in quotes - refer to attributes editor in AD for a specific user to learn more)
  optional= {"displayName":displayName,"givenName":givenName,"sn":sn,"description":description,"personalTitle":personalTitle,"mail":mail,"telephoneNumber":telephoneNumber,"userAccountControl":512}

  try:
    #creates the user using pyad syntax pyad.aduser.ADUser.create
    #all writing to AD happens using syntax  pyad.aduser.ADUser.create
    pyad.aduser.ADUser.create(sAMAccountName,ou,password="Password123",upn_suffix=None,enable=True,optional_attributes=optional)
    print(f"{mail} user added")
    with io.open("created.csv","a",encoding="utf-8") as fcreate:
        fcreate.write("user created" + mail + "\n")
  #output exception error to screen
  except Exception as e:
    print(str(e)+mail)
    #if file already exists io will read the file but if not existing it will create the file
    with io.open("not_created.csv","a",encoding="utf-8") as notfcreate:
        #outputs  exeception error to csv file
        notfcreate.write("NOT created" + str(e) + mail + "\n")