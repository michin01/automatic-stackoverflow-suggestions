# Stack Exchange
 
## Old Queries

select * from Posts where Body like '%reactjs%'

<del>select * from Posts where find_in_set('react', Body) and find_in_set('api', Body) </del>



select * from Posts where CHARINDEX('react', Body) >0

## Not able to access data directly

![](leanote://file/getImage?fileId=5b515690c01c510560000009)


> Two Ideas:

>> 1. Use the Stack Exchange API
https://api.stackexchange.com/

>> 2. Download the whole **StackOverflow** database
https://archive.org/download/stackexchange/



![](leanote://file/getImage?fileId=5b515690c01c510560000008)

# Queries
## NO.1 

```
select * from Posts p
where p.Title like '%##Key##%'
```

35937 rows from excel
key=react
34687 rows returned in 26915 ms

## NO.2  


```
select * from Posts p
where p.Title like '%##Key##%'
and p.Body like '%##Key##%'
```

26927 rows from excel
25940 rows returned in 24777 ms

key=react



## NO.3 

```
select * from Posts p
where p.Tags like '%react%'

```

![](leanote://file/getImage?fileId=5b55fd0016255432b4000000)


```
select p.Id from Posts p
where p.Tags like '%react%'
```

![](leanote://file/getImage?fileId=5b55fe3116255432b4000003)


```
select count(p.Id) from Posts p
where p.Tags like '%react%'
```

![](leanote://file/getImage?fileId=5b55fdfb16255432b4000002)


## NO.4 


```
select * from Posts p
where p.Tags like '%react%js%'
```

```
select count(*) from Posts p
where p.Tags like '%react%js%'
```
![](leanote://file/getImage?fileId=5b55fd7b16255432b4000001)

```
select Top 60000 p.Id from Posts p
where p.Tags like '%reactjs%'
```
50000 rows returned in 16463 ms


```
select count(p.Id) from Posts p
where p.Tags like '%reactjs%'
```

92823

https://meta.stackexchange.com/questions/213050/why-cant-i-pull-in-all-the-so-users-from-data-explorer


![](leanote://file/getImage?fileId=5b56025116255432b4000004)


![](leanote://file/getImage?fileId=5b56026016255432b4000005)

![](leanote://file/getImage?fileId=5b5602a916255432b4000006)

![](leanote://file/getImage?fileId=5b56039b16255432b4000007)

![](leanote://file/getImage?fileId=5b5606cc16255432b4000008)

![](leanote://file/getImage?fileId=5b5606d216255432b4000009)

> `Much Faster,but hard to save csv or json and no sufficient data.`

```
select * from Posts Order by Id offset 6000 rows fetch next 30 rows only
```

It works

## NO.5 

```
select * from Posts p 
where p.Tags like '%react%js%' 
Order by Id 
offset 0 rows fetch next 50000 rows only
```

50000+44283 rows totally

## NO.6 

```
select * from Posts p 
where p.Tags like '%react%' 
Order by Id 
offset 0 rows fetch next 50000 rows only
```

133603


## Outlayer 

```
select * from Posts p 
where p.Id = 50622831
```

![](leanote://file/getImage?fileId=5b563e8616255432b400000a)


## Time Out 

```

select * from Posts p
where 
(p.Title like '%##Key1##%'
and 
p.Title like '%##Key2##%')
or 
(p.Body like '%##Key1##%'
and 
p.Body like '%##Key2##%')

```

```
select * from Posts p
where 
CHARINDEX('%##Key1##%', p.Title) >0 
and 
CHARINDEX('%##Key2##%', p.Title) >0 
or 
CHARINDEX('%##Key1##%', p.Body) >0 
and 
CHARINDEX('%##Key2##%', p.Body) >0 
```

## NLTK 

![](leanote://file/getImage?fileId=5b569ae416255432b400000b)

http://www.nltk.org/book/ch05.html

![](leanote://file/getImage?fileId=5b569bb516255432b400000c)

***

Working on:
<del>1. Find a better way to solve this problem using T-SQL language
2. Work out available API methods to access data directly
3. (Most time and storage consuming) Download the whole database and process data in local storage.
</del>
1. Find out a proper query to collect reactJs data set
2. Use data cleaning technique and NLTK or jieba




