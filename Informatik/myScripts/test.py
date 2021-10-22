from mdutils.mdutils import MdUtils
import os
import datetime
#mdFile = MdUtils(file_name='Example_Markdown',title='Markdown File Example')
#mdFile.create_md_file()
stream=os.popen('gcalcli --calendar uni --nocolor  agenda')
output=stream.read()
today = datetime.datetime.now().strftime("%a %b %d")
nextDay = output[1:].split('\n\n')[0]
if today in nextDay:
    print(nextDay[len(today):])
