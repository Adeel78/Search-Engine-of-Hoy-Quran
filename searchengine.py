
from flask import Flask,jsonify
import json
from flask import Flask, render_template, request

#Opening and formating file so we can access it accordingly

filename = "quran.txt"  # Replace with the path to your text file

res = {}

with open(filename, 'r',encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        split_line = line.split(':', 2)
        if len(split_line) >= 3:
            line_number = split_line[0]
            key = split_line[1]
            value = split_line[2].strip()
            dict_key = f"{line_number}:{key}"
            res[dict_key] = value


# opening the file in read mode
filename = "urdu.txt"  # Replace with the path to your text file

res1 = {}

with open(filename, 'r',encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        split_line = line.split(':', 2)
        if len(split_line) >= 3:
            line_number = split_line[0]
            key = split_line[1]
            value = split_line[2].strip()
            dict_key = f"{line_number}:{key}"
            res1[dict_key] = value



#print(r2)
#print(len(b))

filename = "eng_trans.txt"  # Replace with the path to your text file

res2 = {}

with open(filename, 'r',encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        split_line = line.split(':', 2)
        if len(split_line) >= 3:
            line_number = split_line[0]
            key = split_line[1]
            value = split_line[2].strip()
            dict_key = f"{line_number}:{key}"
            res2[dict_key] = value
repr(res2)

import re

# Read the contents of the file
with open('tafseer.txt', 'r',encoding='utf-8',) as file:
    text = file.read()

# Find all occurrences of numbers within brackets and their associated texts
pattern = r'\((\d+)\)(.*?)\s*(?=\(\d+\)|$)'
matches = re.findall(pattern, text, re.DOTALL)


result = {}
key_counts = {}
for match in matches:
    key = match[0]
    value = match[1].strip()
    
    if key in result:
        if key in key_counts:
            key_counts[key] += 1
        else:
            
            key_counts[key] = 1
        key = key + 's' * key_counts[key]
    
    if key in result:
        result[key].append(value)
    else:
        result[key] = [value]


res3 = {}
a=0
for k, v in res.items():
    keys_list = list(result.keys())
    if a < len(result):
        first_key = keys_list[a]
        value_of_first_key = result[first_key]
        res3[k] =value_of_first_key
        a+=1

#print(len(r1))
filename = 'wbwurdu.txt'  # Replace with the path to your text file


result1 = {}


with open(filename, 'r',encoding='utf-8') as file:
    lines = file.readlines()
    key = None
    value = ''
    for line in lines:
        if ':' in line:
            if key is not None:
                result1[key] = value.strip().replace('\n', '|')
            key, value = line.strip(), ''
        else:
            value += line
    if key is not None:
        result1[key] = value.strip().replace('\n', '|')
for key, value in result1.items():
    if value is None:
        result1[key] = 'NO DATA'
filename = 'wbwenglish.txt'  # Replace with the path to your text file


result2 = {}


with open(filename, 'r',encoding='utf-8') as file:
    lines = file.readlines()
    key = None
    value = ''
    for line in lines:
        if ':' in line:
            if key is not None:
                result2[key] = value.strip().replace('\n', '|')
            key, value = line.strip(), ''
        else:
            value += line
    if key is not None:
        result2[key] = value.strip().replace('\n', '|')
for key, value in result2.items():
    if value is None:
        print(3)
        result2[key] = 'NO DATA'


app = Flask(__name__)


@app.route('/')
def search_page():
    return render_template('search_page.html')

@app.route('/search', methods=['GET'])
@app.route('/search/<string:search_word>/<string:language>', methods=['GET'])
def search(search_word=None, language=None):
    if search_word is None or language is None:
        # Extract search parameters from URL query string
        language = request.args.get('language')
        search_word = request.args.get('word')

    # Check if language is valid
    if language not in ['arabic', 'urdu', 'eng']:
        return render_template('search.html', results=[{'Content': 'Invalid language selected'}])


    if language == "arabic":
        results = []
        count = 0
        c = 0

        for i in res.values():
            if search_word in i:
                a1 = list(res.keys())[list(res.values()).index(i)]
                verse_no = a1
                arabic = res.get(a1)
                urdu = res1.get(a1)
                eng = res2.get(a1)
                if result1.get(a1) != None:
                    wbw_urdu = result1.get(a1)
                    wbw_eng = result2.get(a1)
                    tafseer = res3.get(a1)
                else:
                    wbw_urdu = "No Data"
                    wbw_eng = "No Data"
                    tafseer = "No Data"                
                result = {
                    "verse_no": verse_no,
                    "Arabic": arabic,
                    "Urdu": urdu,
                    "Wbw_Urdu": wbw_urdu,
                    "Eng": eng,
                    "Wbw_Eng": wbw_eng,
                    "Tafseer": tafseer,
                }   
                results.append(result)
                count += 1
                c += 1
        results.insert(0, c)

        if count < 1:
            pass

    elif language == "eng":
        results = []
        count = 0
        c = 0
        

        for i in res2.values():
            if search_word in i:
                a1 = list(res2.keys())[list(res2.values()).index(i)]
                verse_no = a1
                arabic = res.get(a1)
                urdu = res1.get(a1)
                eng = res2.get(a1)
                if result1.get(a1) != None:
                    wbw_urdu = result1.get(a1)
                    wbw_eng = result2.get(a1)
                    tafseer = res3.get(a1)
                else:
                    wbw_urdu = "No Data"
                    wbw_eng = "No Data"
                    tafseer = "No Data"
                
                result = {
                    "verse_no": verse_no,
                    "Arabic": arabic,
                    "Urdu": urdu,
                    "Wbw_Urdu": wbw_urdu,
                    "Eng": eng,
                    "Wbw_Eng": wbw_eng,
                    "Tafseer": tafseer,
                }
                results.append(result)
                count += 1
                c += 1
        results.insert(0, c)

        if count < 1:
            pass

    elif language == "urdu":
        results = []
        count = 0
        c = 0

        for i in res1.values():
            if search_word in i:
                a1 = list(res1.keys())[list(res1.values()).index(i)]
                verse_no = a1
                arabic = res.get(a1)
                urdu = res1.get(a1)
                eng = res2.get(a1)
                if result1.get(a1) != None:
                    wbw_urdu = result1.get(a1)
                    wbw_eng = result2.get(a1)
                    tafseer = res3.get(a1)
                else:
                    wbw_urdu = "No Data"
                    wbw_eng = "No Data"
                    tafseer = "No Data"
                
                result = {
                    "verse_no": verse_no,
                    "Arabic": arabic,
                    "Urdu": urdu,
                    "Wbw_Urdu": wbw_urdu,
                    "Eng": eng,
                    "Wbw_Eng": wbw_eng,
                    "Tafseer": tafseer,
                }
                results.append(result)
                count += 1
                c += 1
        results.insert(0, c)

        if count < 1:
            pass

    else:
        results = []
        results.append({
            "Content": "Language not found"
        })

    return render_template('search.html', results=results,word=search_word)

if __name__ == '__main__':
    app.run()




