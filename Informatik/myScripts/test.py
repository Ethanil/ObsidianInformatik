from mdutils.mdutils import MdUtils
import os
import datetime
stream=os.popen('gcalcli --calendar uni --nocolor  agenda')
output=stream.read()
todaysDate=datetime.datetime.now()
today = todaysDate.strftime("%a %b %d")
nextDay = output[1:].split('\n\n')[0]
mdFile = MdUtils(file_name='Day Planner-'+todaysDate.strftime("%Y%m%d"),title=todaysDate.strftime("%d.%m.%Y"))
mdFile.new_line("| Gestern | Morgen |")
mdFile.new_line("| ------- | ------ |")
mdFile.new_line("| [[Day Planner-{}]] | [[Day Planner-{}]] |".format((todaysDate+datetime.timedelta(days=-1)).strftime("%Y%m%d"),(todaysDate+datetime.timedelta(days=1)).strftime("%Y%m%d")))
if today in nextDay:
    markdown = nextDay[len(today):].split('\n')
    for line in markdown:
        line = "[ ] "+line.strip().replace("          "," ")
        mdFile.new_line(line)
mdFile.create_md_file()
