#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.


# In[18]:


def replace_characters(text):
   
    pattern = re.compile(r'[ ,.]')
    
    
    replaced_text = pattern.sub(':', text)
    
    return replaced_text


if __name__ == "__main__":
   
    sample_text = 'Python Exercises, PHP exercises.'
    

    result_text = replace_characters(sample_text)
    
   
    
    print(result_text)


# In[ ]:


Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.


# In[22]:


import pandas as pd
import re
data = {
    'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']
}


df = pd.DataFrame(data)

def clean_text(text):
    
    cleaned_text = re.sub(r'[^\w\s]', '', text)  
  
    cleaned_text = re.sub(r'\d+', '', cleaned_text) 
    return cleaned_text


df['SUMMARY'] = df['SUMMARY'].apply(clean_text)


print(df)



# In[ ]:


Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.


# In[27]:


def find_long_words(text):
 
    pattern = re.compile(r'\b\w{4,}\b')
    
  
    long_words = pattern.findall(text)
    
    return long_words

if __name__ == "__main__":
   
    input_text = "Here are some example words: computer, codes,java, and regular expressions!"
    
    
    result = find_long_words(input_text)
    
   
    print(result)


# In[ ]:


Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.


# In[30]:


def find_specific_length_words(text):
  
    pattern = re.compile(r'\b\w{3,5}\b')
    
  
    all_words = pattern.findall(text)
    
    
    specific_length_words = [word for word in all_words if 3 <= len(word) <= 5]
    
    return specific_length_words

if __name__ == "__main__":
  
    input_text = "Here are some words: python,language, branch,computer,bench,indian, codes, and text."
    
    
    result = find_specific_length_words(input_text)
    
    
    print(result)


# In[ ]:


Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.


# In[35]:


def remove_parentheses(text_list):
    
    pattern = re.compile(r'\(.*?\)')

    cleaned_list = [pattern.sub('', text).strip() for text in text_list]
    
    return cleaned_list


if __name__ == "__main__":
    
    sample_text_list = [
        "example (.com)",
        "hr@fliprobo (.com)",
        "github (.com)",
        "Hello (Data Science World)",
        "Data (Scientist)"
    ]
    

    result_list = remove_parentheses(sample_text_list)
    
 
    print()
    for text in result_list:
        print(text)


# In[ ]:


Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.


# In[36]:


def remove_parentheses_from_file(filename):
    
    pattern = re.compile(r'\(.*?\)')
    
    with open(filename, 'r') as file:
        text = file.read()
    
    
    cleaned_text = pattern.sub('', text).strip()
    
    
    with open(filename, 'w') as file:
        file.write(cleaned_text)
    
    return cleaned_text


if __name__ == "__main__":
   
    filename = 'sample_text.txt'
  
    sample_text = "\n".join([
        "example (.com)",
        "hr@fliprobo (.com)",
        "github (.com)",
        "Hello (Data Science World)",
        "Data (Scientist)"
    ])
    
   
    with open(filename, 'w') as file:
        file.write(sample_text)
   
    cleaned_text = remove_parentheses_from_file(filename)
    
 
 
    print(cleaned_text)


# In[ ]:


Question 7- Write a regular expression in Python to split a string into uppercase letters.


# In[37]:


def split_by_uppercase(text):
    pattern = re.compile(r'(?=[A-Z])')
    
    parts = pattern.split(text)
    
    return [part for part in parts if part]

if __name__ == "__main__":
    
    sample_text = "ImportanceOfRegularExpressionsInPython"
    
    result = split_by_uppercase(sample_text)
    
    print(result)


# In[ ]:


Question 8- Create a function in python to insert spaces between words starting with numbers.


# In[38]:


def space_between_number(s:str)->str:
    res = ""
    for i in s:
        if 0<=ord(i)-ord('0') and ord(i)-ord('0')<=9:
            res+=" "+i
        else:
            res+=i
    return res
s = "RegularExpression1IsAn2ImportantTopic3InPython"
res = space_between_number(s)
print(res)    


# In[ ]:


Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.


# In[39]:


def insert_spaces(text):
    pattern = re.compile(r'(?<=[a-zA-Z0-9])(?=[A-Z0-9])')
    
    spaced_text = pattern.sub(' ', text)
    
    return spaced_text


if __name__ == "__main__":

    sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
    print(result)


# In[ ]:


Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.


# In[40]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')
df['first_five_letters'] = df['Country'].apply(lambda x:x[:5])
df.head()


# In[ ]:


Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


# In[41]:


def is_valid_string(s):
    
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')

    if pattern.match(i):
        return True
    else:
        return False

    
test_strings = [
    "Iam_India123",
    "Another_country",
    "Unknown-country",  
    "1234567890",
    "AllCountries_123",
    "Invalid program",  
    "Special@Chars!"
]
lst = []
for i in test_strings:
    if is_valid_string(i):
        lst.append(i)
print(lst)


# In[ ]:


Question 12- Write a Python program where a string will start with a specific number. 


# In[42]:


def starts_with_number(s, number):
    number_str = str(number)
    return s.startswith(number_str)

if __name__ == "__main__":
    

    number_to_check = 321
    
    test_strings = [
        "123abc",
        "123abc456",
        "456abc",
        "abc123",
        "321",
        "09876test"
    ]
    
    for s in test_strings:
        print(f"'{s}' starts with {number_to_check}: {starts_with_number(s, number_to_check)}")


# In[ ]:


Question 13- Write a Python program to remove leading zeros from an IP address


# In[44]:


def remove_leading_zeros(ip_address):
 
    octets = ip_address.split('.')
    
 
    cleaned_octets = [str(int(octet)) for octet in octets]
    
  
    cleaned_ip_address = '.'.join(cleaned_octets)
    
    return cleaned_ip_address


if __name__ == "__main__":
   
    ip_addresses = [
        "192.168.001.001",
        "10.000.0.5",
        "255.255.255.255",
        "001.002.003.004",
        "000.0.0.000"
    ]
    
   
    for ip in ip_addresses:
        print(f": {ip} -> : {remove_leading_zeros(ip)}")


# In[ ]:


Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.


# In[45]:


def find_dates(text):
    

    pattern = re.compile(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(?:st|nd|rd|th)? \d{4}\b')
    
   
    matches = pattern.findall(text)
    
    return matches


if __name__ == "__main__":
  
    sample_text = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.'
    
   
    dates = find_dates(sample_text)
    
  
    print
    for date in dates:
        print(date)


# In[ ]:


Question 15- Write a Python program to search some literals strings in a string. 


# In[46]:


def search_literals(text, literals):
    results = {}
    for literal in literals:
        if literal in text:
            results[literal] = True
        else:
            results[literal] = False
    return results


if __name__ == "__main__":
  
    sample_text = 'The quick brown fox jumps over the lazy dog.'
    
 
    literals_to_search = [
     
        'fox',
        'horse',
        'dog'
    ]
    
   
    search_results = search_literals(sample_text, literals_to_search)
    
    
    print
    for literal, found in search_results.items():
        print(f"'{literal}': {'Found' if found else 'Not found'}")


# In[ ]:


Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs


# In[52]:


def search_literals_and_positions(text, literals):
    results = {}
    for literal in literals:
      
        matches = list(re.finditer(re.escape(literal), text))
        if matches:
            results[literal] = [(match.start(), match.end()) for match in matches]
        else:
            results[literal] = None
    return results


if __name__ == "__main__":
    
    sample_text = 'The quick brown fox jumps over the lazy dog.'
    
   
    literals_to_search = [
        
        'fox'
       
    ]
    
   
    search_results = search_literals_and_positions(sample_text, literals_to_search)
    
  
    print
    for literal, positions in search_results.items():
        if positions is not None:
            print(f"'{literal}' found at positions: {positions}")
        else:
            print(f"'{literal}' not found in the text.")


# In[ ]:


Question 17- Write a Python program to find the substrings within a string.


# In[53]:


def find_substrings_with_regex(text, pattern):
    matches = [match.start() for match in re.finditer(re.escape(pattern), text)]
    return matches


if __name__ == "__main__":
    sample_text = 'Python exercises, PHP exercises, C# exercises'
    
    substring_to_find = 'exercises'
    
    positions = find_substrings_with_regex(sample_text, substring_to_find)
    
    print(f"Substring '{substring_to_find}' ")


# In[ ]:


Question 18- Write a Python program to find the occurrence and position of the substrings within a string.


# In[49]:


def find_substrings_positions(text, substring):
    positions = []
    start = 0
    while True:
        start = text.find(substring, start)
        if start == -1:
            break
        positions.append((substring, start))
        start += len(substring)  # Move past the current substring
    return positions


if __name__ == "__main__":
   
    sample_text = 'Python exercises, PHP exercises, C# exercises'
    
   
    substring_to_find = 'exercises'
    
 
    occurrences = find_substrings_positions(sample_text, substring_to_find)
    
  
    print
    for substring, position in occurrences:
        print(f"Substring '{substring}' found at position: {position}")


# In[ ]:


Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.


# In[54]:


from datetime import datetime

def convert_date_format(date_str):
   
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
  
    new_date_str = date_obj.strftime('%d-%m-%Y')
    
    return new_date_str


if __name__ == "__main__":
    
    sample_date = '2024-08-23'
    
   
    converted_date = convert_date_format(sample_date)
    
  
    print(f"Original date: {sample_date}")
    print(f"Converted date: {converted_date}")


# In[ ]:


Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.


# In[55]:


def find_decimal_numbers(text):
    
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    
  
    matches = pattern.findall(text)
    
    return matches


if __name__ == "__main__":
   
    sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
    
   
    decimal_numbers = find_decimal_numbers(sample_text)
    
    
    print(decimal_numbers)


# In[ ]:


Question 21- Write a Python program to separate and print the numbers and their position of a given string.


# In[56]:


def find_numbers_and_positions(text):
  
    pattern = re.compile(r'\b\d+(\.\d+)?\b')
    
 
    matches = list(pattern.finditer(text))
    
   
    numbers_positions = [(match.group(), match.start()) for match in matches]
    
    return numbers_positions


if __name__ == "__main__":
    
    sample_text = "Here are some numbers: 345, 25.6, and 99.2. "
    
    
    numbers_positions = find_numbers_and_positions(sample_text)
    
    
   
    for number, position in numbers_positions:
        print(f"Number: '{number}'  position: {position}")


# In[ ]:


Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.


# In[57]:


def extract_max_numeric_value(text):
    
    pattern = re.compile(r'\b\d+\b')
    
    
    matches = pattern.findall(text)
    
    
    numbers = [int(match) for match in matches]
    
    max_value = max(numbers) if numbers else None
    
    return max_value


if __name__ == "__main__":
   
    sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
    
  
    max_numeric_value = extract_max_numeric_value(sample_text)
    
  
    print(f": {max_numeric_value}")


# In[ ]:


Question 23- Create a function in python to insert spaces between words starting with capital letters.


# In[58]:


def insert_spaces_camel_case(text):
  
    pattern = re.compile(r'(?<!^)(?<!\s)([A-Z])')
    
  
    spaced_text = pattern.sub(r' \1', text)
    
    return spaced_text


if __name__ == "__main__":
  
    sample_text = "RegularExpressionIsAnImportantTopicInPython"
    
    
    result_text = insert_spaces_camel_case(sample_text)
    
    

    print(result_text)


# In[ ]:


Question 24- Python regex to find sequences of one upper case letter followed by lower case letters


# In[61]:


def find_uppercase_followed_by_lowercase(text):
    
    pattern = re.compile(r'\b[A-Z][a-z]+\b')
    
  
    matches = pattern.findall(text)
    
    return matches


if __name__ == "__main__":
  
    sample_text = 'Here are some examples: Python, Computer,RegularExpressions, and HtmlParser,'
    

    sequences = find_uppercase_followed_by_lowercase(sample_text)
    

    print
    for sequence in sequences:
        print(sequence)


# In[ ]:


Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.


# In[63]:


def remove_continuous_duplicates(sentence):
   
    pattern = re.compile(r'\b(\w+)\s+\1\b',)
    
    
    cleaned_sentence = pattern.sub(r'\1', sentence)
    
    return cleaned_sentence

if __name__ == "__main__":
   
    sample_text = "Hello hello world world"
    
  
    result_text = remove_continuous_duplicates(sample_text)
    
    
   
    print(result_text)


# In[ ]:


Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.


# In[64]:


def is_valid_string(text):
 
    pattern = re.compile(r'.*[A-Za-z0-9]$')
    
  
    if pattern.match(text):
        return True
    else:
        return False


if __name__ == "__main__":
    
    test_strings = [
        "Hello World",       
        "Python123",         
        "computer!@#",       
        "NoTrailingSpace ", 
        "EndWithNumber123"  
    ]
    

    for string in test_strings:
        result = is_valid_string(string)
        print(f"'{string}' is valid: {result}")



# In[ ]:


Question 27-Write a python program using RegEx to extract the hashtags.


# In[65]:


def extract_hashtags(text):
  
    pattern = re.compile(r'#\w+')
    
   
    hashtags = pattern.findall(text)
    
    return hashtags


if __name__ == "__main__":
   
    sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
    
    
    hashtags = extract_hashtags(sample_text)
    
   
    print
    for hashtag in hashtags:
        print(hashtag)


# In[ ]:


Question 28- Write a python program using RegEx to remove <U+..> like symbols


# In[66]:


def remove_unicode_symbols(text):
 
    pattern = re.compile(r'<U\+[A-F0-9]{4,}>')
    
   
    cleaned_text = pattern.sub('', text)
    
    return cleaned_text


if __name__ == "__main__":
   
    sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"
    
   
    cleaned_text = remove_unicode_symbols(sample_text)
    

    print(cleaned_text)


# In[ ]:


Question 29- Write a python program to extract dates from the text stored in the text file.


# In[67]:


def create_sample_file(filename):
    
    sample_text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
    
   
    with open(filename, 'w') as file:
        file.write(sample_text)

def extract_dates_from_file(filename):
    
    pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    
  
    with open(filename, 'r') as file:
        text = file.read()
    
   
    dates = pattern.findall(text)
    
    return dates


filename = 'sample_text.txt'


create_sample_file(filename)


dates = extract_dates_from_file(filename)


print("Extracted dates:")
for date in dates:
    print(date)


# In[ ]:


Question 30- Create a function in python to remove all words from a string of length between 2 and 4.


# In[68]:


def remove_short_words(text):
    
    pattern = re.compile(r'\b\w{2,4}\b')
    
    cleaned_text = pattern.sub('', text)
    
   
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

if __name__ == "__main__":
   
    sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    

    result_text = remove_short_words(sample_text)
    
  
    
    print(result_text)


# In[ ]:




