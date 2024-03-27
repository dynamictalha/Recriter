import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re

def fetchAndSavefile(url,path):
    r = requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)

def remove_text_after_character(input_string, specific_character):
    return input_string.split(specific_character, 1)[0]

def append_text_after_character(text, character):
    parts = text.split(character, 1)
    if len(parts) > 1:
        return parts[1]  # Return the part after the character
    else:
        return ""  # If the character is not found, return an empty string
    

def extract_emails_from_span(input_string):
    # Define the regex pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches of email addresses within <em> tags
    matches = re.findall(email_pattern, input_string)

    return matches


def append_text_with_at_symbol(input_text):
    # Find all substrings containing "@" using regular expression
    email_matches = re.findall(r'\b\S+@\S+\b', input_text)

    # Append the matched substrings together
    appended_text = ' '.join(email_matches)

    return appended_text

def remove_duplicates_and_empty_strings(input_list):
    # Remove duplicates and preserve order
    unique_strings = list(dict.fromkeys(input_list))

    # Filter out empty strings
    unique_strings = [string for string in unique_strings if string.strip()]

    return unique_strings




names_list = []
info_list = []
email_list = []
emails_list = []
url = "https://www.google.com/search?q=%22IT+recruiter%22+%22Information+Technology%22+-intitle:%22profiles%22+-inurl:%22dir/+%22+email+%22%40gmail.com%22+site:pk.linkedin.com/in/+OR+site:pk.linkedin.com/pub/&sca_esv=439e824fad57d569&sxsrf=ACQVn0-RJwyQtD7a11EgRhxugwaW6tFPKw:1711192954249&ei=erv-Za_JDp2U9u8P4a-74As&ved=0ahUKEwiv7rfBooqFAxUdiv0HHeHXDrwQ4dUDCBA&uact=5&oq=%22IT+recruiter%22+%22Information+Technology%22+-intitle:%22profiles%22+-inurl:%22dir/+%22+email+%22%40gmail.com%22+site:pk.linkedin.com/in/+OR+site:pk.linkedin.com/pub/&gs_lp=Egxnd3Mtd2l6LXNlcnAikwEiSVQgcmVjcnVpdGVyIiAiSW5mb3JtYXRpb24gVGVjaG5vbG9neSIgLWludGl0bGU6InByb2ZpbGVzIiAtaW51cmw6ImRpci8gIiBlbWFpbCAiQGdtYWlsLmNvbSIgc2l0ZTpway5saW5rZWRpbi5jb20vaW4vIE9SIHNpdGU6cGsubGlua2VkaW4uY29tL3B1Yi9IAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIAoAIAmAMA4gMFEgExIECSBwCgBwA&sclient=gws-wiz-serp&hl=en-PK&no_sw_cr=1&zx=1711193181640#ip=1"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text,"lxml")
# print(soup)

names = soup.find_all("h3",class_ = "zBAuLc l97dzf")
# print(names)

for i in names:
    name = i.text
    n = remove_text_after_character(name, "-")
    info = append_text_after_character(name,"-")
    names_list.append(n)
    info_list.append(info)

# print(len(names_list))
# print(len(info_list))

# fetchAndSavefile(url,"data/info.html")

# -----------------------------
# email = soup.find_all("div", class_ = "BNeawe s3v9rd AP7Wnd")
# # print(email)

# for i in email:
#     e = i.text
#     email = append_text_with_at_symbol(e)
#     email_list.append(email)

# emails_list = remove_duplicates_and_empty_strings(email_list)
# print(emails_list)

df = pd.DataFrame({"Name":names_list,"Business": info_list})

df.to_csv("Recuriter.csv")