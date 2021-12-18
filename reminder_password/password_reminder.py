import boto3
from datetime import datetime
from send_mail import send_email

#boto3.setup_default_session(profile_name='python', region_name='eu-west-2')
client=boto3.client("iam")
response=client.get_credential_report()
#print(response.keys())
#the above prints all keys inside a dictionary for get_credential_report()
data=response["Content"]
data=data.decode("utf-8")
#due to TypeError: a bytes-like object is required, not 'str' we had to use the utf-8 line above
data=data.split("\n")
#print(data)
userid=""
userid1=""
for user in data[1:]:
    print(user.split(",")[0],user.split(",")[6])
    todays_date=datetime.today().date()
    get_time_object=datetime.strptime((user.split(",")[6]).split("T")[0], '%Y-%m-%d')
    if(get_time_object.date() < datetime.today().date()):
      print("password has expired already")
      # if todays date is greater than user.split(",")[6]) then password has already expired
      userid1=userid1+user.split(',')[0]+"\n"
    elif ((get_time_object.date() - datetime.today().date()).days<=15):
      print(f"{user.split(',')[0]} your password is due to expire - please reset password!!!")
      userid=userid+user.split(',')[0]+"\n"
      # if user.split(",")[6]) minus todays date is =< than 15 days then user should get daily notification at 10am
send_email(userid)
send_email(userid1)