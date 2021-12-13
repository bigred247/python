from pyad import *
import io

ou=pyad.adcontainer.ADContainer.from_dn("OU=devops-lab-groups,DC=devops-lab,DC=com")

#the Administrator is granted full control over groups
#this is a gloabl var because it is not insde the function
optional= {"managedBy":"CN=Administrator,CN=Users,DC=devops-lab,DC=com"}

def add_group(row):
  #print(row)
  group_attributes=row.split("|")
  cn=group_attributes[0]
  groupType=group_attributes[1]
  scope=group_attributes[2]
  membership=group_attributes[6]
  pyad.adgroup.ADGroup.create(cn,ou,security_enabled=groupType,scope=scope,optional_attributes=optional)

with io.open("groups.csv", "r", encoding="utf-8") as creategroup:
    data=creategroup.read()
    creategroup.close()

data=data.split("\n")
total_line=len(data)-1
print(f"file has {total_line} lines")

for row in data[1:]:
#    print(row)
    add_group(row)