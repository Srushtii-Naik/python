# fill letter template

letter = '''Dear <|Name|>,
            you are selected!
            <|Date|>'''

print(letter.replace("<|Name|>","Srushti"))
print(letter.replace("<|Name|>","Srushti").replace("<|Date|>","16 sept 2026"))