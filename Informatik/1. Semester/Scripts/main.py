from mdutils.mdutils import MdUtils
import os
import datetime

def createTitle(date,timestring="%Y%m%d"):
    return 'Day Planner-'+date.strftime(timestring)


todaysDate = datetime.datetime.now()
stream = os.popen('gcalcli --calendar uni --nocolor  agenda '+todaysDate.strftime("%m/%d/%Y")+" "+(todaysDate+datetime.timedelta(days=5)).strftime("%m/%d/%Y")+"T00:00")
output = stream.read()
today = todaysDate.strftime("%a %b %d")
calendarAgenda = output[1:].split('\n\n')
nextCalendarEntry = calendarAgenda.pop(0)
print(nextCalendarEntry)
nextAgendaDate = datetime.datetime.strptime(nextCalendarEntry[:10]+datetime.datetime.now().strftime("%Y"), '%a %b %d%Y')
for x in range(5):
    currentDay = todaysDate+datetime.timedelta(days=x)
    if not os.path.isfile(createTitle(currentDay)):
        mdFile = MdUtils(file_name=createTitle(currentDay), title=createTitle(currentDay, "%d.%m.%Y"))
        mdFile.new_line("| Gestern | Morgen |")
        mdFile.new_line("| ------- | ------ |")
        mdFile.new_line("| [[{}]] | [[{}]] |".format(createTitle(currentDay+datetime.timedelta(days=-1)), createTitle(currentDay+datetime.timedelta(days=1))))
        if createTitle(nextAgendaDate) == createTitle(currentDay):
            markdown = nextCalendarEntry[10:].split('\n')
            # print(markdown)
            for line in markdown:
                if line != "":
                    line = "- [ ] "+line.strip().replace("          "," ")
                    mdFile.new_line(line)
            if len(calendarAgenda) > 0:
                nextCalendarEntry = calendarAgenda.pop(0)
                print(nextCalendarEntry)
                nextAgendaDate = datetime.datetime.strptime(nextCalendarEntry[:10]+datetime.datetime.now().strftime("%Y"), '%a %b %d%Y')
        mdFile.create_md_file()

