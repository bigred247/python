from typing import Optional
from pyad import *
import io
from validate_cn import gen_cn
from validate_cn import gen_mail

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
  
  #if EMAIL exists already do NOT create user
  #email address is indexed in AD but telephone number may not be? 
  #if not indexed will make the function slow and bad performance
  counter=0
  final_mail=gen_mail(mail, counter)
  #the if statement below is NOT followed by a "else" statement so a second user with the same emaail cannot be created.
  if (final_mail==0):
    telephoneNumber=user_attributes[5]
    members=user_attributes[6].split(",")

  #splits the file and uses the left side eg. username portion of email as unqiue userID
    sAMAccountName=mail.split("@")[0]
    counter=0
  #final_cn gets called only if the "final_mail=gen_mail(mail, counter)" if condition is met
  #and does not actually use the sAMAccountName - refer to the gen_cn function for clarity
    final_cn=gen_cn(sAMAccountName, counter)
    if (final_cn==0):
      cn=sAMAccountName.strip()
    else:
      cn=sAMAccountName+str(final_cn)
      cn=cn.strip()
  #combines first name and last name for display name
    displayName=givenName+", "+sn
  #optional syntax below generates the map of users from csv file (key value for AD is in quotes - refer to attributes editor in AD for a specific user to learn more)
    optional= {"displayName":displayName,"givenName":givenName,"sn":sn,"description":description,"personalTitle":personalTitle,"mail":mail,"telephoneNumber":telephoneNumber,"userAccountControl":512}

    try:
      #creates the user using pyad syntax pyad.aduser.ADUser.create
      #all writing to AD happens using syntax  pyad.aduser.ADUser.create
      pyad.aduser.ADUser.create(cn,ou,password="Password123",upn_suffix=None,enable=True,optional_attributes=optional)
      print(f"{mail} user added")
      
      #this block of code adds users to the groups from test.csv  
      for member in members:
        user_to_add=pyad.aduser.ADUser.from_cn(sAMAccountName)
        group=pyad.adgroup.ADGroup.from_cn(member)
        user_to_add.add_to_group(group)
        print(f"{sAMAccountName} is added to {member}")
    
      with io.open("created.csv","a",encoding="utf-8") as fcreate:
          fcreate.write("user created" + mail + "\n")
  #output exception error to screen
    except Exception as e:
      print(str(e)+mail)
      #if file already exists io will read the file but if not existing it will create the file
      with io.open("not_created.csv","a",encoding="utf-8") as notfcreate:
          #outputs  exeception error to csv file
          notfcreate.write("NOT created" + str(e) + mail + "\n")
  else:
    print(f" user {mail} NOT created because email is in use")