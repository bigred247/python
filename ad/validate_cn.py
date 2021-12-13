import pyad.adquery
query=pyad.adquery.ADQuery()

#gen_cn counter allows a numerical value to be added to a users name if more than one user with the same name exists
#eg. jamesbond@gmail.com will be the first user, then jamesbond1@gmail.com for second user, jamesbond2@gmail.com for third and so on and so forth.
def gen_cn(gn,counter):
    if counter==0:
        cn=gn
    else:
        cn=gn+str(counter)
    query.execute_query(attributes=["cn"],
    
    where_clause="sAMAccountName='{}'".format(cn),
    base_dn="DC=devops-lab,DC=com")
    if(query.get_row_count()>=1):
        counter=counter+1
        return gen_cn(gn,counter)

    return (counter)
    #the above return (counter) value only returns the counter value eg. 1 


#gen_mail is a copy of above function but is for email addresses
#in this scenrio, the create_ad_user.py is configured to stop creation
#of any subsequnet user with the same email address 
def gen_mail(gn,counter):
    if counter==0:
        cn=gn
    else:
        cn=gn+str(counter)
    query.execute_query(attributes=["cn"],
    
    where_clause="mail='{}'".format(cn),
    base_dn="DC=devops-lab,DC=com")
    if(query.get_row_count()>=1):
        counter=counter+1
        return gen_mail(gn,counter)

    return (counter)