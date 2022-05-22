import requests
import csv

region = str(input("Введіть код регіона: "))
list_region_cod= ['01', '05', '07']
list_region_cod2 = [12, 14, 18, 21, 23, 26, 32, 35, 44, 46, 48, 51, 53, 56, 59, 61, 63, 65, 68, 71, 73, 74, 80, 85]
find_region1= int(region) in list_region_cod
find_region2 = int(region) in list_region_cod2
if find_region1 is False:
    if find_region2 is False:
        print("Введіть інший код!")
        exit(0)

r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+region_cod+'&exp=json')

print("Ректор, директор, виконуюча обов'язки директора, В.о.ректора, В.о. директора")
value_name_post = str(input("Виберіть назву та впишіть: "))

universities: list = r.json()
filtered_data = [{k: row[k] for k in ['university_id', 'post_index']} for row in universities]
filtered_data2 = [{k: row[k] for k in ['university_name', 'university_email', "university_phone",
                                              'university_director_post', 'university_director_fio']}
                         for k in ['university_director_post'] for row in universities if row[k] == value_name_post]

with open('universities_'+region+'.csv', mode='w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

with open('contacts.csv', mode='w', encoding='UTF-8') as f_contact:
    writer = csv.DictWriter(f_contacts, fieldnames=filtered_data2[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data_contact)