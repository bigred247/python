RONI DAS1:41 PM

   
from pyad import *
RONI DAS1:48 PM
ou=pyad.adcontainer.ADContainer.from_dn("OU=test,DC=totaltechnology,DC=com")
RONI DAS1:52 PM
def add_user(row):
    print(row)
RONI DAS1:55 PM
user_attributes=row.split("|")
RONI DAS1:58 PM
givenName=user_attributes[0]
sn=user_attributes[1]
RONI DAS2:04 PM
sAMAccountName=mail.split("@")[0]
RONI DAS2:07 PM
optional={"givenName":givenName,"sn":sn,"dob":dob,"personalTitle":personalTitle,"mail":mail,"mobile":mobile,"userAccountControl":512}
RONI DAS2:17 PM
try:
        pyad.aduser.ADUser.create(sAMAccountName,ou,password="Rambo@1234",upn_suffix=None,enable=True,optional_attributes=optional)
        print(f"{mail} user adeed")
    except Exception as e:
        print(str(e)+mail)
You2:42 PM
mahmud.fraz@gmail.com


<https://www.onlinedatagenerator.com/>