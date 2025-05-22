---
aliases: 
---

> [!multi-column]
>
>> ## To Do
>>```tasks
>>tags do not include #SG-Arbeit
>> not done
>> sort by priority
>> sort by due
>> (((no scheduled date) OR (has start date)) AND (starts on or before today)) OR ((starts on or before in four weeks) AND (tags include #Exam)) OR ((has scheduled date) AND ((scheduled on or before today) OR (no scheduled date)))
>> group by priority
>> hide backlink
>> hide recurrence rule
>>```
>
>> ## Arbeit
>> ```tasks
>> tags include #SG-Arbeit
>> not done
>> sort by priority
>> sort by due
>> group by priority
>> hide backlink
>> hide recurrence rule
>> ```
>
>> ## Future
>> ```tasks
>> tags do not include #SG-Arbeit
>> not done
>> sort by start
>> ((((has start date) AND (starts after today)) OR (scheduled after today)) AND (tags does not include #Exam)) OR ((tags include #Exam) AND (starts after in four weeks))
>> hide backlink
>> hide recurrence rule
>> ```
## Done
```tasks
done
hide backlink
hide recurrence rule
group by tags
```

## Links