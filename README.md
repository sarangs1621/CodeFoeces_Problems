# CodeForces_Problems
These are the set of codeforces problems I have done


# [**A. A+B (Trial Problem)**](https://codeforces.com/problemset/problem/1351/A)
You are given two integers a and b. Print a+b.

**Input**

The first line contains an integer t (1≤t≤104) — the number of test cases in the input. Then t test cases follow.

Each test case is given as a line of two integers a and b (−1000≤a,b≤1000).

**Output**

Print t integers — the required numbers a+b.

# [**A. Bear and Big Brother**](https://codeforces.com/contest/791/problem/A)
Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.

Right now, Limak and Bob weigh a and b respectively. It's guaranteed that Limak's weight is smaller than or equal to his brother's weight.

Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year.

After how many full years will Limak become strictly larger (strictly heavier) than Bob?

**Input**

The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10) — the weight of Limak and the weight of Bob respectively.

**Output**

Print one integer, denoting the integer number of years after which Limak will become strictly larger than Bob.


# [**A. Boy or Girl**](https://codeforces.com/contest/236/problem/A)
Those days, many boys use beautiful girls' photos as avatars in forums. So it is pretty hard to tell the gender of a user at the first glance. Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man! Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

**Input**

The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

**Output**

If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).

# [**A. Candies and Two Sisters**](https://codeforces.com/contest/1335/problem/A)
There are two sisters Alice and Betty. You have n candies. You want to distribute these n candies between two sisters in such a way that:

Alice will get a (a>0) candies; Betty will get b (b>0) candies; each sister will get some integer number of candies; Alice will get a greater amount of candies than Betty (i.e. a>b); all the candies will be given to one of two sisters (i.e. a+b=n). Your task is to calculate the number of ways to distribute exactly n candies between sisters in a way described above. Candies are indistinguishable.

Formally, find the number of ways to represent n as the sum of n=a+b, where a and b are positive integers and a>b.

You have to answer t independent test cases.

**Input**

The first line of the input contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.

The only line of a test case contains one integer n (1≤n≤2⋅109) — the number of candies you have.

**Output**

For each test case, print the answer — the number of ways to distribute exactly n candies between two sisters in a way described in the problem statement. If there is no way to satisfy all the conditions, print 0.

# [**A. Coins**](https://codeforces.com/contest/1061/problem/A)
You have unlimited number of coins with values 1,2,…,n. You want to select some set of coins having the total value of S.

It is allowed to have multiple coins with the same value in the set. What is the minimum number of coins required to get sum S?

**Input**

The only line of the input contains two integers n and S (1≤n≤100000, 1≤S≤109)

**Output**

Print exactly one integer — the minimum number of coins required to obtain sum S.

# **[A. Diagonal Walking](https://codeforces.com/contest/954/problem/A)**
Mikhail walks on a 2D plane. He can go either up or right. You are given a sequence of Mikhail's moves. He thinks that this sequence is too long and he wants to make it as short as possible.

In the given sequence moving up is described by character U and moving right is described by character R. Mikhail can replace any pair of consecutive moves RU or UR with a diagonal move (described as character D). After that, he can go on and do some other replacements, until there is no pair of consecutive moves RU or UR left.

Your problem is to print the minimum possible length of the sequence of moves after the replacements.

**Input**

The first line of the input contains one integer n (1 ≤ n ≤ 100) — the length of the sequence. The second line contains the sequence consisting of n characters U and R.

**Output**

Print the minimum possible length of the sequence of moves after all replacements are done.

# [**A. Domino Piling**](https://codeforces.com/contest/50/problem/A)
You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

Each domino completely covers two squares.

No two dominoes overlap.

Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.

**Input**

In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).

**Output**

Output one number — the maximal number of dominoes, which can be placed.

# [**A. Elections**](https://codeforces.com/contest/1593/problem/A)
The elections in which three candidates participated have recently ended. The first candidate received a votes, the second one received b votes, the third one received c votes. For each candidate, solve the following problem: how many votes should be added to this candidate so that he wins the election (i.e. the number of votes for this candidate was strictly greater than the number of votes for any other candidate)?

Please note that for each candidate it is necessary to solve this problem independently, i.e. the added votes for any candidate do not affect the calculations when getting the answer for the other two candidates.

**Input**

The first line contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.

Each test case consists of one line containing three integers a, b, and c (0≤a,b,c≤109).

**Output**

For each test case, output in a separate line three integers A, B, and C (A,B,C≥0) separated by spaces — the answers to the problem for the first, second, and third candidate, respectively.


# [**A. Elephant**](https://codeforces.com/problemset/problem/617/A)
An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

**Input**

The first line of the input contains an integer x (1 ≤ x ≤ 1 000 000) — The coordinate of the friend's house.

**Output**

Print the minimum number of steps that elephant needs to make to get from point 0 to point x

# [**A. Fafa and his Company**](https://codeforces.com/problemset/problem/935/A)

Fafa owns a company that works on huge projects. There are n employees in Fafa's company. Whenever the company has a new project to start working on, Fafa has to divide the tasks of this project among all the employees.

Fafa finds doing this every time is very tiring for him. So, he decided to choose the best l employees in his company as team leaders. Whenever there is a new project, Fafa will divide the tasks among only the team leaders and each team leader will be responsible of some positive number of employees to give them the tasks. To make this process fair for the team leaders, each one of them should be responsible for the same number of employees. Moreover, every employee, who is not a team leader, has to be under the responsibility of exactly one team leader, and no team leader is responsible for another team leader.

Given the number of employees n, find in how many ways Fafa could choose the number of team leaders l in such a way that it is possible to divide employees between them evenly.

**Input**

The input consists of a single line containing a positive integer n (2 ≤ n ≤ 105) — the number of employees in Fafa's company.

**Output**

Print a single integer representing the answer to the problem.

# [**Football**](https://codeforces.com/contest/96/problem/A)

Petya loves football very much. One day, as he was watching a football match, he was writing the players' current positions on a piece of paper. To simplify the situation he depicted it as a string consisting of zeroes and ones. A zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players of some team standing one after another, then the situation is considered dangerous. For example, the situation 00100110111111101 is dangerous and 11110111011101 is not. You are given the current situation. Determine whether it is dangerous or not.

**Input**

The first input line contains a non-empty string consisting of characters "0" and "1", which represents players. The length of the string does not exceed 100 characters. There's at least one player from each team present on the field.

**Output**

Print "YES" if the situation is dangerous. Otherwise, print "NO"

# [**A. Frog Jumping**](https://codeforces.com/problemset/problem/1077/A)

A frog is currently at the point 0 on a coordinate axis Ox. It jumps by the following algorithm: the first jump is a units to the right, the second jump is b units to the left, the third jump is a units to the right, the fourth jump is b units to the left, and so on.

Formally:

if the frog has jumped an even number of times (before the current jump), it jumps from its current position x to position x+a;
otherwise it jumps from its current position x to position x−b.
Your task is to calculate the position of the frog after k jumps.

But... One more thing. You are watching t different frogs so you have to answer t independent queries.

**Input**

The first line of the input contains one integer t (1≤t≤1000) — the number of queries.

Each of the next t lines contain queries (one query per line).

The query is described as three space-separated integers a,b,k (1≤a,b,k≤109) — the lengths of two types of jumps and the number of jumps, respectively.

**Output**

Print t integers. The i-th integer should be the answer for the i-th query.

# [**A. Golden Plate**](https://codeforces.com/problemset/problem/1031/A)

You have a plate and you want to add some gilding to it. The plate is a rectangle that we split into w×h cells. There should be k gilded rings, the first one should go along the edge of the plate, the second one — 2 cells away from the edge and so on. Each ring has a width of 1 cell. Formally, the i-th of these rings should consist of all bordering cells on the inner rectangle of size (w−4(i−1))×(h−4(i−1)).

![image](https://user-images.githubusercontent.com/92372142/145137915-665b2a65-79e8-42fd-ada0-e0f9474c21af.png)

The picture corresponds to the third example.
Your task is to compute the number of cells to be gilded.

**Input**

The only line contains three integers w, h and k (3≤w,h≤100, 1≤k≤⌊min(n,m)+14⌋, where ⌊x⌋ denotes the number x rounded down) — the number of rows, columns and the number of rings, respectively.

**Output**

Print a single positive integer — the number of cells to be gilded.

# [**A. Good Number**](https://codeforces.com/contest/365/problem/A)
Let's call a number k-good if it contains all digits not exceeding k (0, ..., k). You've got a number k and an array a containing n numbers. Find out how many k-good numbers are in a (count each number every time it occurs in array a).

**Input**

The first line contains integers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ 9). The i-th of the following n lines contains integer ai without leading zeroes (1 ≤ ai ≤ 109).

**Output**

Print a single integer — the number of k-good numbers in a.

# [**A. In Search of an Easy Problem**](https://codeforces.com/contest/1030/problem/A)

When preparing a tournament, Codeforces coordinators try treir best to make the first problem as easy as possible. This time the coordinator had chosen some problem and asked n people about their opinions. Each person answered whether this problem is easy or hard.

If at least one of these n people has answered that the problem is hard, the coordinator decides to change the problem. For the given responses, check if the problem is easy enough.

**Input**

The first line contains a single integer n (1≤n≤100) — the number of people who were asked to give their opinions.

The second line contains n integers, each integer is either 0 or 1. If i-th integer is 0, then i-th person thinks that the problem is easy; if it is 1, then i-th person thinks that the problem is hard.

**Output**

Print one word: "EASY" if the problem is easy according to all responses, or "HARD" if there is at least one person who thinks the problem is hard.

You may print every letter in any register: "EASY", "easy", "EaSY" and "eAsY" all will be processed correctly.

# [**A. Love "A"**](https://codeforces.com/problemset/problem/1146/A)

Alice has a string s. She really likes the letter "a". She calls a string good if strictly more than half of the characters in that string are "a"s. For example "aaabb", "axaa" are good strings, and "baca", "awwwa", "" (empty string) are not.

Alice can erase some characters from her string s. She would like to know what is the longest string remaining after erasing some characters (possibly zero) to get a good string. It is guaranteed that the string has at least one "a" in it, so the answer always exists.

**Input**

The first line contains a string s (1≤|s|≤50) consisting of lowercase English letters. It is guaranteed that there is at least one "a" in s.

**Output**

Print a single integer, the length of the longest good string that Alice can get after erasing some characters from s

# [**A. Make a triangle!**](https://codeforces.com/problemset/problem/1064/A)

Masha has three sticks of length a, b and c centimeters respectively. In one minute Masha can pick one arbitrary stick and increase its length by one centimeter. She is not allowed to break sticks.

What is the minimum number of minutes she needs to spend increasing the stick's length in order to be able to assemble a triangle of positive area. Sticks should be used as triangle's sides (one stick for one side) and their endpoints should be located at triangle's vertices.

**Input**

The only line contains tree integers a, b and c (1≤a,b,c≤100) — the lengths of sticks Masha possesses.

**Output**

Print a single integer — the minimum number of minutes that Masha needs to spend in order to be able to make the triangle of positive area from her sticks.

# [**A. Mike and palindrome**](https://codeforces.com/contest/798/problem/A)

Mike has a string s consisting of only lowercase English letters. He wants to change exactly one character from the string so that the resulting one is a palindrome.
A palindrome is a string that reads the same backward as forward, for example strings "z", "aaa", "aba", "abccba" are palindromes, but strings "codeforces", "reality", "ab" are not.

**Input**

The first and single line contains string s (1 ≤ |s| ≤ 15).

**Output**

Print "YES" (without quotes) if Mike can change exactly one character so that the resulting string is palindrome or "NO" (without quotes) otherwise.

# **[A. Minimizing the String](https://codeforces.com/contest/1076/problem/A)**

You have to remove at most one (i.e. zero or one) character of this string in such a way that the string you obtain will be lexicographically smallest among all strings that can be obtained using this operation.

String s=s1s2…sn is lexicographically smaller than string t=t1t2…tm if n<m and s1=t1,s2=t2,…,sn=tn or there exists a number p such that p≤min(n,m) and s1=t1,s2=t2,…,sp−1=tp−1 and sp<tp.

For example, "aaa" is smaller than "aaaa", "abb" is smaller than "abc", "pqr" is smaller than "z".

**Input**

The first line of the input contains one integer n (2≤n≤2⋅105) — the length of s.

The second line of the input contains exactly n lowercase Latin letters — the string s.

**Output**

Print one string — the smallest possible lexicographically string that can be obtained by removing at most one character from the string s.

# [**A. Police Recruits**](https://codeforces.com/contest/427/problem/A)
The police department of your city has just started its journey. Initially, they don’t have any manpower. So, they started hiring new recruits in groups.

Meanwhile, crimes keeps occurring within the city. One member of the police force can investigate only one crime during his/her lifetime.

If there is no police officer free (isn't busy with crime) during the occurrence of a crime, it will go untreated.

Given the chronological order of crime occurrences and recruit hirings, find the number of crimes which will go untreated.

**Input**

The first line of input will contain an integer n (1 ≤ n ≤ 105), the number of events. The next line will contain n space-separated integers.

If the integer is -1 then it means a crime has occurred. Otherwise, the integer will be positive, the number of officers recruited together at that time. No more than 10 officers will be recruited at a time.

**Output**

Print a single integer, the number of crimes which will go untreated.

# [**A. Repeating Cipher**](https://codeforces.com/contest/1095/problem/A)

Polycarp loves ciphers. He has invented his own cipher called repeating.

Repeating cipher is used for strings. To encrypt the string s=s1s2…sm (1≤m≤10), Polycarp uses the following algorithm:

he writes down s1 ones,
he writes down s2 twice,
he writes down s3 three times,
...
he writes down sm m times.
For example, if s="bab" the process is: "b" → "baa" → "baabbb". So the encrypted s="bab" is "baabbb".

Given string t — the result of encryption of some string s. Your task is to decrypt it, i. e. find the string s.

**Input**

The first line contains integer n (1≤n≤55) — the length of the encrypted string. The second line of the input contains t — the result of encryption of some string s. It contains only lowercase Latin letters. The length of t is exactly n.

It is guaranteed that the answer to the test exists.

**Output**

Print such string s that after encryption it equals t.

#[**A. Romaji**](https://codeforces.com/contest/1008/problem/A)

Vitya has just started learning Berlanese language. It is known that Berlanese uses the Latin alphabet. Vowel letters are "a", "o", "u", "i", and "e". Other letters are consonant.

In Berlanese, there has to be a vowel after every consonant, but there can be any letter after any vowel. The only exception is a consonant "n"; after this letter, there can be any letter (not only a vowel) or there can be no letter at all. For example, the words "harakiri", "yupie", "man", and "nbo" are Berlanese while the words "horse", "king", "my", and "nz" are not.

Help Vitya find out if a word  is Berlanese.

**Input**

The first line of the input contains the string  consisting of  () lowercase Latin letters.

**Output**

Print "YES" (without quotes) if there is a vowel after every consonant except "n", otherwise print "NO".

You can print each letter in any case (upper or lower).

# **[A. Superhero Transformation](https://codeforces.com/contest/1111/problem/A)**

We all know that a superhero can transform to certain other superheroes. But not all Superheroes can transform to any other superhero. A superhero with name s can transform to another superhero with name t if s can be made equal to t by changing any vowel in s to any other vowel and any consonant in s to any other consonant. Multiple changes can be made.

In this problem, we consider the letters 'a', 'e', 'i', 'o' and 'u' to be vowels and all the other letters to be consonants.

Given the names of two superheroes, determine if the superhero with name s can be transformed to the Superhero with name t.

**Input**

The first line contains the string s having length between 1 and 1000, inclusive.

The second line contains the string t having length between 1 and 1000, inclusive.

Both strings s and t are guaranteed to be different and consist of lowercase English letters only.

**Output**

Output "Yes" (without quotes) if the superhero with name s can be transformed to the superhero with name t and "No" (without quotes) otherwise.

You can print each letter in any case (upper or lower).

# [**A. Team**](https://codeforces.com/contest/231/problem/A)

One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests. Participants are usually offered several problems during programming contests. Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. Otherwise, the friends won't write the problem's solution.

This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution. Help the friends find the number of problems for which they will write a solution.

**Input**

The first input line contains a single integer n (1 ≤ n ≤ 1000) — the number of problems in the contest. Then n lines contain three integers each, each integer is either 0 or 1. If the first number in the line equals 1, then Petya is sure about the problem's solution, otherwise he isn't sure. The second number shows Vasya's view on the solution, the third number shows Tonya's view. The numbers on the lines are separated by spaces.

**Output**

Print a single integer — the number of problems the friends will implement on the contest.

# **[A. The Rank](https://codeforces.com/problemset/problem/1017/A)**

John Smith knows that his son, Thomas Smith, is among the best students in his class and even in his school. After the students of the school took the exams in English, German, Math, and History, a table of results was formed.

There are n students, each of them has a unique id (from 1 to n). Thomas's id is 1. Every student has four scores correspond to his or her English, German, Math, and History scores. The students are given in order of increasing of their ids.

In the table, the students will be sorted by decreasing the sum of their scores. So, a student with the largest sum will get the first place. If two or more students have the same sum, these students will be sorted by increasing their ids.

Please help John find out the rank of his son.

**Input**

The first line contains a single integer n (1≤n≤1000) — the number of students.

Each of the next n lines contains four integers ai, bi, ci, and di (0≤ai,bi,ci,di≤100) — the grades of the i-th student on English, German, Math, and History. The id of the i-th student is equal to i.

**Output**

Print the rank of Thomas Smith. Thomas's id is 1.

# **[A. Watermelon](https://codeforces.com/problemset/problem/4/A)**
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

**Input**

The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

**Output**

Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

# [**A. Word**](https://codeforces.com/contest/59/problem/A)

Vasya is very upset that many people on the Net mix uppercase and lowercase letters in one word. That's why he decided to invent an extension for his favorite browser that would change the letters' register in every word so that it either only consisted of lowercase letters or, vice versa, only of uppercase ones. At that as little as possible letters should be changed in the word. For example, the word HoUse must be replaced with house, and the word ViP — with VIP. If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.

**Input**

The first line contains a word s — it consists of uppercase and lowercase Latin letters and possesses the length from 1 to 100.

**Output** 

Print the corrected word s. If the given word s has strictly more uppercase letters, make the word written in the uppercase register, otherwise - in the lowercase one.

