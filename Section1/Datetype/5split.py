text = "We are learning python devops"
new_text =  text.split()      ## here split is the method, which spliting spaces from string.
print(new_text)
print("Word:", new_text)

#Print specific object in split ()
print(text.split()[2])
print(text.split()[4])
print(text.split()[1])


#another example

arn = "arn:partition:service:region:account-id:resource-type/resource-id"
new_arn = arn.split("/")              ## here slash (/) is spliting
print("Display new arn with splited:", new_arn)

#Print specific object in split ()
print(arn.split("/")[0])
print(arn.split("/")[1])


arn1 = "arn:partition:service:region:account-id:resource-type/resource-id1"
new_arn1 = arn.split(":")
print(new_arn1)