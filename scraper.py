import requests
from bs4 import BeautifulSoup
import json


#Getting Domain Name
domain = str(input("Enter the Domain: "))
print('')

#Make request
data=requests.get(f'https://ful.io/domain/{domain}')
soup = BeautifulSoup(data.text, 'html.parser')

#Grabbing Social Links
socialLinksRawData = requests.get(f'https://{domain}')
socialSoup = BeautifulSoup(socialLinksRawData.text, 'html.parser') 
socialLinks = socialSoup.find_all('a')

#Converting it to Array
socialLinksArr = []
for link in socialLinks:
  socialLinksArr.append(link['href']) 

#Required Social Links
socialMediaSites = ['facebook','linkedin','instagram','youtube','twitter']




#Grabbing Contact Details
contactDetails = soup.find('script',{'id': '__NEXT_DATA__'}).text
jsonData = json.loads(contactDetails) #converting data to JSON

mobileNumbers = jsonData['props']['pageProps']['domaindata']['mobileno']
emails = jsonData['props']['pageProps']['domaindata']['emailid']



#Printing Contact Details
print("")

print("Mobile: ")
print("")
for mob in mobileNumbers:
    if "." not in mob:
        print(mob)

print('')
print('')

print("Email: ")
print('')
for email in emails:
    print(email)
print('')



#Printing Social Links

obtainedLinks = [] #contains Duplicates
uniqueLinks = [] #contains only unique links

print('')
print('')

print("Social Links: ")
print('')
for link in socialLinksArr:
    for site in socialMediaSites:
        if site in link:
            obtainedLinks.append(link)

for i in obtainedLinks:
    if i not in uniqueLinks:
        uniqueLinks.append(i)
#Printing unique links
for link in uniqueLinks:
    print(link)
print('')



# print(socialLinks)    

# print(json.dumps(jsonData['props']['pageProps']['domaindata']['mobileno'], indent = 1))

