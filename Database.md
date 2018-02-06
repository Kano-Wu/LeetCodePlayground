# Database

## 175. Combine Two Tables

### 知识点

1. LEFT JOIN    
LEFT JOIN 关键字会从左表 (table_name1) 那里返回所有的行，即使在右表 (table_name2) 中没有匹配的行。

**My Answer**

```sql
SELECT
    FirstName,
    LastName,
    City,
    State
FROM
    Person
LEFT JOIN Address ON Person.PersonId = Address.PersonId
```

## 176. Second Highest Salary

### 难点

1. 当没有第二大值时，输出null

**My Answer**

```sql
SELECT Salary AS SecondHighestSalary FROM Employee ORDER BY Salary DESC LIMIT 1,1
```
PS: 当没有第二大值时，出错！如果确保有第二大值，则是最佳答案。

**Another Wrong Answer**

```sql
SELECT
    e.Salary AS SecondHighestSalary
FROM
    Employee e
WHERE
    e.Salary = (
        SELECT
            MAX(e1.Salary)
        FROM
            Employee e1
        WHERE
            e1.Salary NOT IN (
                SELECT
                    MAX(e2.Salary)
                FROM
                    Employee e2
            )
    );
```

**Another Wrong Answer**

```sql
SELECT
    IFNULL(e.Salary, null) AS SecondHighestSalary
FROM
    Employee e
WHERE
    e.Salary = (
        SELECT
            MAX(e1.Salary)
        FROM
            Employee e1
        WHERE
            e1.Salary NOT IN (
                SELECT
                    MAX(e2.Salary)
                FROM
                    Employee e2
            )
    );
```

**Best Answer**

```sql
SELECT
    MAX(Salary) AS SecondHighestSalary
FROM
    Employee
WHERE
    Salary < (
        SELECT
            MAX(Salary)
        FROM
            Employee
    )
```

* 当值不存在时，MAX()会返回null。

## 177. Nth Highest Salary

### 知识点

1. 自定义函数   

2. LIMIT 与 OFFSET   
从第9条记录开始，取4条记录    
SELECT * FROM student LIMIT 9,4    
SELECT * FROM student LIMIT 4 OFFSET 9    

3. 变量   
变量定义：DECLARE M INT    
变量赋值：SET M = 1

**Best Answer**

```sql
DELIMITER $$
DROP  FUNCTION  IF  EXISTS  `getNthHighestSalary`  $$
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary AS getNthHighestSalary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET M
  );
END $$

SELECT getNthHighestSalary(2);
```

## 178. Rank Scores

### 难点

1. 排序时，相同数值有相同序号
2. GROUP BY

**Wrong Answer**

```sql
SELECT
    (@rowNum :=@rowNum + 1) AS Rank,
    Score
FROM
    Scores,
    (SELECT(@rowNum := 0)) AS Q1
ORDER BY
    Scores.Score DESC
```

### ERROR

```sql
[Err] 1248 - Every derived table must have its own alias
```

* Select 嵌套使用临时表时，需要为临时表指定别名。

**Right Answer**

```sql
SELECT
    Scores.Score,
    COUNT(Ranking.Score) AS Rank
FROM
    Scores,
    (
        SELECT DISTINCT
            Score
        FROM
            Scores
    ) AS Ranking
WHERE
    Scores.Score <= Ranking.Score
GROUP BY
    Scores.Id,
    Scores.Score
ORDER BY
    Scores.Score DESC;
```