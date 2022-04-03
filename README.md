# T301735
What's in a name? Task 2

## Environment

### Pywikibot

There's a tested example of environment setting in `user-config.py` in the pywikibot folder:

```python
family = 'wikidata'
mylang = 'wikidata'
usernames['wikidata']['wikidata'] = 'ExampleBot'
password_file = "user-password.py"
console_encoding = 'utf-8'
```

if using BotPassword, you will have to config `user-password.py` file.

## Task script

### Source code
[t301735.py](t301735.py)

### Instructions

This is an interactive script, you will have to input some information to the script, including the mandatory fields:

- Data site
- User
- Text

And some optional parameters:

- Summary
- Data type
- Property
- Linked property
- Label
- Language

After setting above parameters, the script will connect to the Wikidata website, and perform some operations mentioned in the task T301735.

You will have to put the script into the pywikibot folder, usually in the `core`, otherwise the text you input will not be saving to the user's profile.

## Output

Some author's information on Wikidata can be found in the [output](./output) folder.

## Reference

1. https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script
2. https://www.mediawiki.org/wiki/Manual:Pywikibot/Wikidata
3. https://www.wikidata.org/wiki/Wikidata:Creating_a_bot
4. https://www.mediawiki.org/wiki/Manual:Pywikibot/user-config.py#ExampleBot_on_Wikidata
5. https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Setting_up_Shop
6. https://github.com/mpeel/wikicode/blob/master/example.py