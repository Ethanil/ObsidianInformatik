---
aliases: 
---

> [!multi-column]
>
>> ## Work
>>```tasks
>>tags do not include #SG-Arbeit
>> not done
>> sort by priority
>> sort by due
>> (((no scheduled date) OR (has start date)) AND (starts on or before today)) OR ((starts on or before in four weeks) AND (tags include #Exam)) OR ((has scheduled date) AND ((scheduled on or before today) OR (no scheduled date)))
>> group by priority
>> hide backlink
>>```
>
>> ## Personal
>> ```tasks
>> tags include #SG-Arbeit
>> not done
>> sort by priority
>> sort by due
>> group by priority
>> hide backlink
>> ```
>
>> ## Charity
>> ```tasks
>> tags do not include #SG-Arbeit
>> not done
>> sort by start
>> ((((has start date) AND (starts after today)) OR (scheduled after today)) AND (tags does not include #Exam)) OR ((tags include #Exam) AND (starts after in four weeks))
>> hide backlink
>> ```


## To Do
```tasks
tags do not include #SG-Arbeit
not done
sort by priority
sort by due
(((no scheduled date) OR (has start date)) AND (starts on or before today)) OR ((starts on or before in four weeks) AND (tags include #Exam)) OR ((has scheduled date) AND ((scheduled on or before today) OR (no scheduled date)))
group by priority
hide backlink
```
## SG-Arbeit
```tasks
tags include #SG-Arbeit
not done
sort by priority
sort by due
group by priority
hide backlink
```
## Future
```tasks
tags do not include #SG-Arbeit
not done
sort by start
((((has start date) AND (starts after today)) OR (scheduled after today)) AND (tags does not include #Exam)) OR ((tags include #Exam) AND (starts after in four weeks))
hide backlink
```

## Done
```tasks
done
hide backlink
group by tags
```

## Links