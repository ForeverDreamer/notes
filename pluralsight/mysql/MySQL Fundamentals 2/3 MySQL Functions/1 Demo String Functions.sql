-- ASCII - Return numeric value of left-most character
SELECT ASCII('a'), ASCII('A');

-- CHAR() - Return the character for each integer passed
SELECT CHAR(77, 121, 83, 81, 76);
SELECT CHAR(65);

-- LENGTH() - Return the length of a string in bytes
SELECT LENGTH('SQLAuthority'), LENGTH('SQLAuthority '), LENGTH('你好世界');

-- CONCAT() - Return concatenated string
SELECT CONCAT('SQL', 'Authori', 'ty');
SELECT CONCAT('SQL', NULL, 'ty');

-- LCASE() - Return the argument in lowercase - Synonym for LOWER()
SELECT LCASE('SQLAuthority'), LOWER('PlUrAlSigHt');

-- UCASE() - Return the argument in uppercase - Synonym for UPPER()
SELECT UCASE('SQLAuthority'), UPPER('PlUrAlSigHt');

-- LEFT() - Return the leftmost number of characters as specified
SELECT LEFT('SQLAuthority', 4), LEFT('PlUrAlSigHt', 3);

-- RIGHT() - Return the rightmost number of characters as specified
SELECT RIGHT('SQLAuthority', 4), RIGHT('PlUrAlSigHt', 3);

-- RTRIM() - Remove trailing spaces
SELECT RTRIM('SQLAuthority'), RTRIM('  SQLAuthority  ');

-- LTRIM() - Remove leading spaces
SELECT LTRIM('SQLAuthority'), LTRIM('  SQLAuthority  ');

-- TRIM() - Remove leading and trailing spaces
SELECT TRIM('SQLAuthority'), TRIM('  SQLAuthority  ');