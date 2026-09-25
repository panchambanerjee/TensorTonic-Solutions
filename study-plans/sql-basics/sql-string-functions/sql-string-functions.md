## SQL String Functions for Data Cleaning

SQL string functions let you clean and preprocess text data directly in the database layer, before it reaches your analysis code. The core functions covered here - TRIM, LOWER, LENGTH, SUBSTRING, and SPLIT_PART - form a practical toolkit for normalizing messy text in PostgreSQL and DuckDB.

### TRIM: Removing Stray Whitespace

`TRIM()` removes leading and trailing whitespace (or specified characters) from a string:

```sql
SELECT TRIM('  hello world  ');   -- 'hello world'
SELECT LTRIM('  hello  ');        -- 'hello  '
SELECT RTRIM('  hello  ');        -- '  hello'
```

TRIM does not affect spaces inside the string - only at the edges. You can also trim specific characters:

```sql
SELECT TRIM(BOTH '-' FROM '--hello--');  -- 'hello'
```

### LOWER and UPPER: Normalizing Case

`LOWER()` converts all characters to lowercase. `UPPER()` converts to uppercase. Case normalization is critical when the same entity appears with different casing across records.

```sql
SELECT LOWER(TRIM(respondent)) AS respondent_clean
FROM survey_responses;
-- '  Alice Chen  ' -> 'alice chen'
```

Trim first to remove whitespace, then lowercase the result. If you lowercase first, extra spaces remain and cause mismatches when grouping or joining.

### LENGTH: Measuring String Size

`LENGTH()` returns the number of characters in a string. Always trim before computing length - otherwise trailing whitespace inflates the count.

```sql
SELECT LENGTH('Hello');             -- 5
SELECT LENGTH(TRIM('  Hello  '));   -- 5
```

### SUBSTRING: Extracting Portions of Text

`SUBSTRING` extracts a portion of a string given a starting position (1-based) and an optional length:

```sql
SELECT SUBSTRING('Hello World', 1, 5);   -- 'Hello'
SELECT SUBSTRING('Hello World', 7);       -- 'World' (to end)
```

If the string is shorter than the requested length, SUBSTRING returns the full string without padding.

### SPLIT_PART: Parsing Delimited Strings

`SPLIT_PART()` splits a string by a delimiter and returns the Nth part (PostgreSQL and DuckDB):

```sql
SELECT SPLIT_PART('john@example.com', '@', 1);  -- 'john'
SELECT SPLIT_PART('john@example.com', '@', 2);  -- 'example.com'
```

For URL parsing, the domain is at position 3 because `://` produces an empty string at position 2:

```sql
SELECT SPLIT_PART('https://www.example.com/page', '/', 3);
-- 'www.example.com'
```

If the part number exceeds the number of parts, an empty string is returned. Part numbers are 1-based.

### Combining Functions

Real-world cleaning typically chains multiple functions:

```sql
SELECT LOWER(TRIM(respondent)) AS respondent_clean,
       LENGTH(TRIM(raw_answer)) AS answer_length,
       SUBSTRING(TRIM(raw_answer), 1, 20) AS answer_preview,
       SPLIT_PART(source_url, '/', 3) AS source_domain
FROM survey_responses;
```

The key principle: always clean (TRIM) before measuring or transforming.

### Database Compatibility

| Function | PostgreSQL | MySQL | DuckDB | SQL Server |
|----------|-----------|-------|--------|------------|
| TRIM | Yes | Yes | Yes | Yes (LTRIM/RTRIM) |
| LOWER/UPPER | Yes | Yes | Yes | Yes |
| LENGTH | Yes | CHAR_LENGTH | Yes | LEN |
| SUBSTRING | Yes | Yes | Yes | Yes |
| SPLIT_PART | Yes | No | Yes | No |

For databases without SPLIT_PART, combine SUBSTRING with POSITION to manually locate the delimiter and extract the portion you need.