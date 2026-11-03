import re

text = "Patient ID: 12345, Contact: 9876543210"

pattern = r"\d+"

match_result = re.match(pattern, text)
search_result = re.search(pattern, text)
find_result = re.findall(pattern, text)

print("Original Text:", text)
print("Match Result:", match_result)
print("Search Result:", search_result.group() if search_result else "Not Found")
print("Find All Result:", find_result)
