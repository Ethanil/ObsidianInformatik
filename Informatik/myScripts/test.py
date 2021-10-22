from mdutils.mdutils import MdUtils
import os
import datetime
todaysDate=datetime.datetime.now()
command = 'gcalcli --calendar uni --nocolor  agenda '+todaysDate.strftime("%m/%d/%Y")+" "+(todaysDate+datetime.timedelta(days=4)).strftime("%m/%d/%Y")
print(command)
stream=os.popen('gcalcli --calendar uni --nocolor  agenda '+todaysDate.strftime("%m/%d/%Y")+" "+(todaysDate+datetime.timedelta(days=4)).strftime("%m/%d/%Y"))
output=stream.read()
print(output)
todaysDate = datetime.datetime(2021,10,25)
today = todaysDate.strftime("%a %b %d")
for calendarEntry in output[1:].split('\n\n'):
    #nextDay = output[1:].split('\n\n')[0]
    thisDay = datetime.datetime.strptime(calendarEntry[:10]+datetime.datetime.now().strftime("%Y"),'%a %b %d%Y')
    print(thisDay)
    print(today)
    mdFile = MdUtils(file_name='Day Planner-'+thisDay.strftime("%Y%m%d"),title=thisDay.strftime("%d.%m.%Y"))
    mdFile.new_line("| Gestern | Morgen |")
    mdFile.new_line("| ------- | ------ |")
    mdFile.new_line("| [[Day Planner-{}]] | [[Day Planner-{}]] |".format((thisDay+datetime.timedelta(days=-1)).strftime("%Y%m%d"),(thisDay+datetime.timedelta(days=1)).strftime("%Y%m%d")))
    if today in calendarEntry:
        markdown = nextDay[len(today):].split('\n')
        for line in markdown:
            line = "[ ] "+line.strip().replace("          "," ")
            mdFile.new_line(line)
    mdFile.create_md_file()

