# CodeForces, Hacker Rank & CodeChef Problems 
These are the set of Codeforces, HackerRank and CodeChef problems I have done


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

# [**A. Unimodal Array**](https://codeforces.com/problemset/problem/831/A)
Array of integers is unimodal, if:

it is strictly increasing in the beginning;
after that it is constant;
after that it is strictly decreasing.
The first block (increasing) and the last block (decreasing) may be absent. It is allowed that both of this blocks are absent.

For example, the following three arrays are unimodal: [5, 7, 11, 11, 2, 1], [4, 4, 2], [7], but the following three are not unimodal: [5, 5, 6, 6, 1], [1, 2, 1, 2], [4, 5, 5, 6].

Write a program that checks if an array is unimodal.

**Input**

The first line contains integer n (1 ≤ n ≤ 100) — the number of elements in the array.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 1 000) — the elements of the array.

**Output**

Print "YES" if the given array is unimodal. Otherwise, print "NO".

You can output each letter in any case (upper or lower).

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

# [**A. Lesha and array splitting**](https://codeforces.com/problemset/problem/754/A)

One spring day on his way to university Lesha found an array A. Lesha likes to split arrays into several parts. This time Lesha decided to split the array A into several, possibly one, new arrays so that the sum of elements in each of the new arrays is not zero. One more condition is that if we place the new arrays one after another they will form the old array A.

Lesha is tired now so he asked you to split the array. Help Lesha!

**Input**

The first line contains single integer n (1 ≤ n ≤ 100) — the number of elements in the array A.

The next line contains n integers a1, a2, ..., an ( - 103 ≤ ai ≤ 103) — the elements of the array A.

**Output**

If it is not possible to split the array A and satisfy all the constraints, print single line containing "NO" (without quotes).

Otherwise in the first line print "YES" (without quotes). In the next line print single integer k — the number of new arrays. In each of the next k lines print two integers li and ri which denote the subarray A[li... ri] of the initial array A being the i-th new array. Integers li, ri should satisfy the following conditions:

l1 = 1
rk = n
ri + 1 = li + 1 for each 1 ≤ i < k.
If there are multiple answers, print any of them.

# [**A. Spy Detected!**](https://codeforces.com/contest/1512/problem/A)
You are given an array a consisting of n (n≥3) positive integers. It is known that in this array, all the numbers except one are the same (for example, in the array [4,11,4,4] all numbers except one are equal to 4).

Print the index of the element that does not equal others. The numbers in the array are numbered from one.

**Input**

The first line contains a single integer t (1≤t≤100). Then t test cases follow.

The first line of each test case contains a single integer n (3≤n≤100) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤100).

It is guaranteed that all the numbers except one in the a array are the same.

**Output**

For each test case, output a single integer — the index of the element that is not equal to others.

# [**A. Review Site**](https://codeforces.com/contest/1511/problem/A)
You are an upcoming movie director, and you have just released your first movie. You have also launched a simple review site with two buttons to press — upvote and downvote.

However, the site is not so simple on the inside. There are two servers, each with its separate counts for the upvotes and the downvotes.

n reviewers enter the site one by one. Each reviewer is one of the following types:

type 1: a reviewer has watched the movie, and they like it — they press the upvote button;
type 2: a reviewer has watched the movie, and they dislike it — they press the downvote button;
type 3: a reviewer hasn't watched the movie — they look at the current number of upvotes and downvotes of the movie on the server they are in and decide what button to press. If there are more downvotes than upvotes, then a reviewer downvotes the movie. Otherwise, they upvote the movie.
Each reviewer votes on the movie exactly once.

Since you have two servers, you can actually manipulate the votes so that your movie gets as many upvotes as possible. When a reviewer enters a site, you know their type, and you can send them either to the first server or to the second one.

What is the maximum total number of upvotes you can gather over both servers if you decide which server to send each reviewer to?

**Input**

The first line contains a single integer t (1≤t≤104) — the number of testcases.

Then the descriptions of t testcases follow.

The first line of each testcase contains a single integer n (1≤n≤50) — the number of reviewers.

The second line of each testcase contains n integers r1,r2,…,rn (1≤ri≤3) — the types of the reviewers in the same order they enter the site.

**Output**

For each testcase print a single integer — the maximum total number of upvotes you can gather over both servers if you decide which server to send each reviewer to.

# [**A. Ehab and another construction problem**](https://codeforces.com/contest/1088/problem/A)

Given an integer x, find 2 integers a and b such that:

1≤a,b≤x
b divides a (a is divisible by b).
a⋅b>x.
ab<x.

**Input**

The only line contains the integer x (1≤x≤100).

**Output**

You should output two integers a and b, satisfying the given conditions, separated by a space. If no pair of integers satisfy the conditions above, print "-1" (without quotes).

# [**A. Find Divisible**](https://codeforces.com/contest/1096/problem/A)

You are given a range of positive integers from l to r.

Find such a pair of integers (x,y) that l≤x,y≤r, x≠y and x divides y.

If there are multiple answers, print any of them.

You are also asked to answer T independent queries.

**Input**

The first line contains a single integer T (1≤T≤1000) — the number of queries.

Each of the next T lines contains two integers l and r (1≤l≤r≤998244353) — inclusive borders of the range.

It is guaranteed that testset only includes queries, which have at least one suitable pair.

**Output**

Print T lines, each line should contain the answer — two integers x and y such that l≤x,y≤r, x≠y and x divides y. The answer in the i-th line should correspond to the i-th query from the input.

If there are multiple answers, print any of them.

# [**B. File Name**](https://codeforces.com/contest/978/problem/B)

You can not just take the file and send it. When Polycarp trying to send a file in the social network "Codehorses", he encountered an unexpected problem. If the name of the file contains three or more "x" (lowercase Latin letters "x") in a row, the system considers that the file content does not correspond to the social network topic. In this case, the file is not sent and an error message is displayed.

Determine the minimum number of characters to remove from the file name so after that the name does not contain "xxx" as a substring. Print 0 if the file name does not initially contain a forbidden substring "xxx".

You can delete characters in arbitrary positions (not necessarily consecutive). If you delete a character, then the length of a string is reduced by 1. For example, if you delete the character in the position 2 from the string "exxxii", then the resulting string is "exxii".

**Input**

The first line contains integer n (3≤n≤100) — the length of the file name.

The second line contains a string of length n consisting of lowercase Latin letters only — the file name.

**Output**

Print the minimum number of characters to remove from the file name so after that the name does not contain "xxx" as a substring. If initially the file name dost not contain a forbidden substring "xxx", print 0.

# [**B. Two-gram**](https://codeforces.com/contest/977/problem/B)

Two-gram is an ordered pair (i.e. string of length two) of capital Latin letters. For example, "AZ", "AA", "ZA" — three distinct two-grams.

You are given a string s consisting of n capital Latin letters. Your task is to find any two-gram contained in the given string as a substring (i.e. two consecutive characters of the string) maximal number of times. For example, for string s = "BBAABBBA" the answer is two-gram "BB", which contained in s three times. In other words, find any most frequent two-gram.

Note that occurrences of the two-gram can overlap with each other.

**Input**

The first line of the input contains integer number n (2≤n≤100) — the length of string s. The second line of the input contains the string s consisting of n capital Latin letters.

**Output**

Print the only line containing exactly two capital Latin letters — any two-gram contained in the given string s as a substring (i.e. two consecutive characters of the string) maximal number of times.

# [**Sum of Digits**](https://www.codechef.com/problems/FLOW006)

You're given an integer N. Write a program to calculate the sum of all the digits of N.

**Input**

The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

**Output**

For each test case, calculate the sum of digits of N, and display it in a new line.

**Constraints**

1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000

**Example**

**Input**

3 
12345
31203
2123

**Output**

15
9
8

# [**A. The King's Race**](https://codeforces.com/contest/1075/problem/A)
On a chessboard with a width of n and a height of n, rows are numbered from bottom to top from 1 to n, columns are numbered from left to right from 1 to n. Therefore, for each cell of the chessboard, you can assign the coordinates (r,c), where r is the number of the row, and c is the number of the column.

The white king has been sitting in a cell with (1,1) coordinates for a thousand years, while the black king has been sitting in a cell with (n,n) coordinates. They would have sat like that further, but suddenly a beautiful coin fell on the cell with coordinates (x,y)...

Each of the monarchs wanted to get it, so they decided to arrange a race according to slightly changed chess rules:

As in chess, the white king makes the first move, the black king makes the second one, the white king makes the third one, and so on. However, in this problem, kings can stand in adjacent cells or even in the same cell at the same time.

The player who reaches the coin first will win, that is to say, the player who reaches the cell with the coordinates (x,y) first will win.

Let's recall that the king is such a chess piece that can move one cell in all directions, that is, if the king is in the (a,b) cell, then in one move he can move from (a,b) to the cells (a+1,b), (a−1,b), (a,b+1), (a,b−1), (a+1,b−1), (a+1,b+1), (a−1,b−1), or (a−1,b+1). Going outside of the field is prohibited.

Determine the color of the king, who will reach the cell with the coordinates (x,y) first, if the white king moves first.

**Input**

The first line contains a single integer n (2≤n≤1018) — the length of the side of the chess field.

The second line contains two integers x and y (1≤x,y≤n) — coordinates of the cell, where the coin fell.

**Output**

In a single line print the answer "White" (without quotes), if the white king will win, or "Black" (without quotes), if the black king will win.

You can print each letter in any case (upper or lower).

# [**C. Songs Compression**](https://codeforces.com/problemset/problem/1015/C)

Ivan has n songs on his phone. The size of the i-th song is ai bytes. Ivan also has a flash drive which can hold at most m bytes in total. Initially, his flash drive is empty.

Ivan wants to copy all n songs to the flash drive. He can compress the songs. If he compresses the i-th song, the size of the i-th song reduces from ai to bi bytes (bi<ai).

Ivan can compress any subset of the songs (possibly empty) and copy all the songs to his flash drive if the sum of their sizes is at most m. He can compress any subset of the songs (not necessarily contiguous).

Ivan wants to find the minimum number of songs he needs to compress in such a way that all his songs fit on the drive (i.e. the sum of their sizes is less than or equal to m).

If it is impossible to copy all the songs (even if Ivan compresses all the songs), print "-1". Otherwise print the minimum number of songs Ivan needs to compress.

**Input**

The first line of the input contains two integers n and m (1≤n≤105,1≤m≤109) — the number of the songs on Ivan's phone and the capacity of Ivan's flash drive.

The next n lines contain two integers each: the i-th line contains two integers ai and bi (1≤ai,bi≤109, ai>bi) — the initial size of the i-th song and the size of the i-th song after compression.

**Output**

If it is impossible to compress a subset of the songs in such a way that all songs fit on the flash drive, print "-1". Otherwise print the minimum number of the songs to compress.

# [**B. Array Stabilization**](https://codeforces.com/problemset/problem/1095/B)

You are given an array a consisting of n integer numbers.

Let instability of the array be the following value: ![image.png](data:image/png;base64,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)

You have to remove exactly one element from this array to minimize instability of the resulting (n−1)-elements array. Your task is to calculate the minimum possible instability.

**Input**

The first line of the input contains one integer n (2≤n≤105) — the number of elements in the array a.

The second line of the input contains n integers a1,a2,…,an (1≤ai≤105) — elements of the array a.

**Output**

Print one integer — the minimum possible instability of the array if you have to remove exactly one element from the array a.

# [**B. Letters Rearranging**](https://codeforces.com/problemset/problem/1093/B)

You are given a string s consisting only of lowercase Latin letters.

You can rearrange all letters of this string as you wish. Your task is to obtain a good string by rearranging the letters of the given string or report that it is impossible to do it.

Let's call a string good if it is not a palindrome. Palindrome is a string which is read from left to right the same as from right to left. For example, strings "abacaba", "aa" and "z" are palindromes and strings "bba", "xd" are not.

You have to answer t independent queries.

**Input**

The first line of the input contains one integer t (1≤t≤100) — number of queries.

Each of the next t lines contains one string. The i-th line contains a string si consisting only of lowercase Latin letter. It is guaranteed that the length of si is from 1 to 1000 (inclusive).

**Output**

Print t lines. In the i-th line print the answer to the i-th query: -1 if it is impossible to obtain a good string by rearranging the letters of si and any good string which can be obtained from the given one (by rearranging the letters) otherwise.

# [**B. Delete from the Left**](https://codeforces.com/problemset/problem/1005/B)

You are given two strings s and t. In a single move, you can choose any of two strings and delete the first (that is, the leftmost) character. After a move, the length of the string decreases by 1. You can't choose a string if it is empty.

For example:

by applying a move to the string "where", the result is the string "here",
by applying a move to the string "a", the result is an empty string "".
You are required to make two given strings equal using the fewest number of moves. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the initial strings.

Write a program that finds the minimum number of moves to make two given strings s and t equal.

**Input**

The first line of the input contains s. In the second line of the input contains t. Both strings consist only of lowercase Latin letters. The number of letters in each string is between 1 and 2⋅105, inclusive.

**Output**

Output the fewest number of moves required. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the given strings.

# ["Hello World!" in C](https://www.hackerrank.com/challenges/hello-world-c/problem?isFullScreen=true)
**Objective**

In this challenge, we will learn some basic concepts of C that will get you started with the language. You will need to use the same syntax to read input and write output in many C challenges. As you work through these problems, review the code stubs to learn about reading from stdin and writing to stdout.

Task

This challenge requires you to print  on a single line, and then print the already provided input string to stdout. If you are not familiar with C, you may want to read about the printf() command.

Example

The required output is:

Hello, World!  
Life is beautiful  
Function Descriptio

Complete the main() function below.

The main() function has the following input:

string s: a string
Prints

*two strings: * "Hello, World!" on one line and the input string on the next line.

**Input**

Welcome to C programming.

**Output**

Hello, World!
Welcome to C programming.

# [**Playing With Characters**](https://www.hackerrank.com/challenges/playing-with-characters/problem?isFullScreen=true)
**Objective**

This challenge will help you to learn how to take a character, a string and a sentence as input in C.

To take a single character  as input, you can use scanf("%c", &ch ); and printf("%c", ch) writes a character specified by the argument char to stdout

char ch;
scanf("%c", &ch);
printf("%c", ch);
This piece of code prints the character .

You can take a string as input in C using scanf(“%s”, s). But, it accepts string only until it finds the first space.

In order to take a line as input, you can use scanf("%[^\n]%*c", s); where  is defined as char s[MAX_LEN] where  is the maximum size of s. Here, [] is the scanset character. ^\n stands for taking input until a newline isn't encountered. Then, with this %*c, it reads the newline character and here, the used * indicates that this newline character is discarded.

Note: The statement: scanf("%[^\n]%*c", s); will not work because the last statement will read a newline character, \n, from the previous line. This can be handled in a variety of ways. One way is to use scanf("\n"); before the last statement.

Task

You have to print the character, ch , in the first line. Then print  in next line. In the last line print the sentence, sen.

**Input**

First, take a character,ch as input.
Then take the string,s as input.
Lastly, take the sentence sen as input.

**Constraints**

Strings for s and sen will have fewer than 100 characters, including the newline.

**Output**

Print three lines of output. The first line prints the character, ch.
The second line prints the string, s.
The third line prints the sentence, sen.

# [**Sum and Difference of Two Numbers**](https://www.hackerrank.com/challenges/sum-numbers-c/problem?isFullScreen=true)
**Objective**

The fundamental data types in c are int, float and char. Today, we're discussing int and float data types.

The printf() function prints the given statement to the console. The syntax is printf("format string",argument_list);. In the function, if we are using an integer, character, string or float as argument, then in the format string we have to write %d (integer), %c (character), %s (string), %f (float) respectively.

The scanf() function reads the input data from the console. The syntax is scanf("format string",argument_list);. For ex: The scanf("%d",&number) statement reads integer number from the console and stores the given value in variable number.

To input two integers separated by a space on a single line, the command is scanf("%d %d", &n, &m), where n and m are the two integers.

Task

Your task is to take two numbers of int data type, two numbers of float data type as input and output their sum:

Declare 4 variables: two of type int and two of type float.
Read 2 lines of input from stdin (according to the sequence given in the 'Input Format' section below) and initialize your 4 variables.
Use the + and - operator to perform the following operations:
Print the sum and difference of two int variable on a new line.
Print the sum and difference of two float variable rounded to one decimal place on a new line.
**Input**

The first line contains two integers.
The second line contains two floating point numbers.

**Constraints**

1 ≤ integer variables ≤ 10⁴
1 ≤ float variables ≤ 10⁴
 
**Output**

Print the sum and difference of both integers separated by a space on the first line, and the sum and difference of both float (scaled to 1 decimal place) separated by a space on the second line.

Sample Input

10 4
4.0 2.0
Sample Output

14 6
6.0 2.0

# [**Functions in C**](https://www.hackerrank.com/challenges/functions-in-c/problem?isFullScreen=true)
**Objective**

In this challenge, you will learn simple usage of functions in C. Functions are a bunch of statements grouped together. A function is provided with zero or more arguments, and it executes the statements on it. Based on the return type, it either returns nothing (void) or something.

A sample syntax for a function is

	return_type function_name(arg_type_1 arg_1, arg_type_2 arg_2, ...) {
    	...
        ...
        ...
        [if return_type is non void]
        	return something of type `return_type`;
    }
For example, a function to read four variables and return the sum of them can be written as

	int sum_of_four(int a, int b, int c, int d) {
    	int sum = 0;
        sum += a;
        sum += b;
        sum += c;
        sum += d;
        return sum;
    }
+= : Add and assignment operator. It adds the right operand to the left operand and assigns the result to the left operand.

a += b is equivalent to a = a + b;
Task

Write a function int max_of_four(int a, int b, int c, int d) which reads four arguments and returns the greatest of them.

Note

There is not built in max function in C. Code that will be reused is often put in a separate function, e.g. int max(x, y) that returns the greater of the two values.

**Input **

Input will contain four integers - a,b,c,d, one on each line.

**Output **

Print the greatest of the four integers.
Note: I/O will be automatically handled.

Sample Input

3
4
6
5

Sample Output

6

# [**Pointers in C**](https://www.hackerrank.com/challenges/pointer-in-c/problem?isFullScreen=true)
**Objective**

In this challenge, you will learn to implement the basic functionalities of pointers in C. A pointer in C is a way to share a memory address among different contexts (primarily functions). They are primarily used whenever a function needs to modify the content of a variable that it does not own.

In order to access the memory address of a variable,val , prepend it with & sign. For example, &val returns the memory address of val.

This memory address is assigned to a pointer and can be shared among various functions. For example, int * p = &val  will assign the memory address of val to pointer p. To access the content of the memory to which the pointer points, prepend it with a *. For example, *p will return the value reflected by val and any modification to it will be reflected at the source (val).

	void increment(int *v) {
        (*v)++; 
    }
      	int main() {
        int a;
        scanf("%d", &a);
        increment(&a);
        printf("%d", a);
    	return 0;      
    }     
Task
a' = a + b
b' = |a - b|

Complete the function void update(int *a,int *b). It receives two integer pointers, int* a and int* b. Set the value of  to their sum, and  to their absolute difference. There is no return value, and no return statement is needed.

**Input**

The input will contain two integers,  and , separated by a newline.

**Output**

Modify the two values in place and the code stub main() will print their values.

Note: Input/ouput will be automatically handled. You only have to complete the function described in the 'task' section.

Sample Input

4
5
Sample Output

9
1

# [**Say "Hello, World!" With C++**](https://www.hackerrank.com/challenges/cpp-hello-world/problem?isFullScreen=true)
**Objective**

This is a simple challenge to help you practice printing to stdout. You may also want to complete Solve Me First in C++ before attempting this challenge.

We're starting out by printing the most famous computing phrase of all time! In the editor below, use either printf or cout to print the string Hello, World! to stdout.

The more popular command form is cout. It has the following basic form:

cout<<value_to_print<<value_to_print;

Any number of values can be printed using one command as shown.

The printf command comes from C language. It accepts an optional format specification and a list of variables. Two examples for printing a string are:

printf("%s", string); printf(string);

Note that neither method adds a newline. It only prints what you tell it to.

**Output**

Print Hello, World! to stdout.

Sample Output

Hello, World!

# [**Input and Output**](https://www.hackerrank.com/challenges/cpp-input-and-output/problem?isFullScreen=true)
**Objective**

In this challenge, we practice reading input from stdin and printing output to stdout.

In C++, you can read a single whitespace-separated token of input using cin, and print output to stdout using cout. For example, let's say we declare the following variables:

string s;
int n;
and we want to use cin to read the input "High 5" from stdin. We can do this with the following code:

cin >> s >> n;
This reads the first word ("High") from stdin and saves it as string s, then reads the second word ("5") from stdin and saves it as integer n. If we want to print these values to stdout, separated by a space, we write the following code:

cout << s << " " << n << endl;
This code prints the contents of string s, a single space (" "), then the integer n. We end our line of output with a newline using endl. This results in the following output:

High 5
Task
Read 3 numbers from stdin and print their sum to stdout.

**Input **

One line that contains 3 space-separated integers: a, b, and c.

**Constraints**
1 ≤  a,b,c ≤ 1000

**Output**

Print the sum of the three numbers on a single line.

Sample Input

1 2 7
Sample Output

10

# [**Basic Data Types**](https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem?isFullScreen=true)
**Objective**

Some C++ data types, their format specifiers, and their most common bit widths are as follows:

Int ("%d"): 32 Bit integer
Long ("%ld"): 64 bit integer
Char ("%c"): Character type
Float ("%f"): 32 bit real value
Double ("%lf"): 64 bit real value
Reading
To read a data type, use the following syntax:

scanf("`format_specifier`", &val)
For example, to read a character followed by a double:

char ch;
double d;
scanf("%c %lf", &ch, &d);
For the moment, we can ignore the spacing between format specifiers.

Printing
To print a data type, use the following syntax:

printf("`format_specifier`", val)
For example, to print a character followed by a double:

char ch = 'd';
double d = 234.432;
printf("%c %lf", ch, d);
Note: You can also use cin and cout instead of scanf and printf; however, if you are taking a million numbers as input and printing a million lines, it is faster to use scanf and printf.

**Input **

Input consists of the following space-separated values: int, long, char, float, and double, respectively.

**Output **

Print each element on a new line in the same order it was received as input. Note that the floating point value should be correct up to 3 decimal places and the double to 9 decimal places.

Sample Input

3 12345678912345 a 334.23 14049.30493
Sample Output

3
12345678912345
a
334.230
14049.304930000

# [**Conditional Statements**](https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem?isFullScreen=true)
if and else are two of the most frequently used conditionals in C/C++, and they enable you to execute zero or one conditional statement among many such dependent conditional statements. We use them in the following ways:

if: This executes the body of bracketed code starting with statement1 if condition evaluates to true.

if (condition) {
    statement1;
    ...
}
if - else: This executes the body of bracketed code starting with statement1 if condition evaluates to true, or it executes the body of code starting with statement2 if condition evaluates to false. Note that only one of the bracketed code sections will ever be executed.

if (condition) {
    statement1;
    ...
}
else {
    statement2;
    ...
}
if - else if - else: In this structure, dependent statements are chained together and the condition for each statement is only checked if all prior conditions in the chain evaluated to false. Once a condition evaluates to true, the bracketed code associated with that statement is executed and the program then skips to the end of the chain of statements and continues executing. If each condition in the chain evaluates to false, then the body of bracketed code in the else block at the end is executed.

if(first condition) {
    ...
}
else if(second condition) {
    ...
}
.
.
.
else if((n-1)'th condition) {
    ....
}
else {
    ...
}
Given a positive integer n, do the following:

If 1 ≤ n ≤ 9, print the lowercase English word corresponding to the number (e.g., one for , two for , etc.).
If n > 9 , print Greater than 9.
Input Formatn ≤ 9

A single integer,n .

**Constraints**

1 ≤ n ≤ 10⁹

**Output **

If 1 ≤ n ≤ 9, then print the lowercase English word corresponding to the number (e.g., one for 1, two for 2, etc.); otherwise, print Greater than 9.

Sample Input 0

5
Sample Output 0

five

Explanation 0

five is the English word for the number 5.

Sample Input 1

8
Sample Output 1

eight

Explanation 1

eight is the English word for the number 8.

Sample Input 2

44
Sample Output 2

Greater than 9

# [**For Loop**](https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem?isFullScreen=true)
A for loop is a programming language statement which allows code to be repeatedly executed.

The syntax is

for ( <expression_1> ; <expression_2> ; <expression_3> )
    <statement>
expression_1 is used for intializing variables which are generally used for controlling the terminating flag for the loop.
expression_2 is used to check for the terminating condition. If this evaluates to false, then the loop is terminated.
expression_3 is generally used to update the flags/variables.
A sample loop is

for(int i = 0; i < 10; i++) {
    ...
}
In this challenge, you will use a for loop to increment a variable through a range.

**Input **

You will be given two positive integers,  and  (), separated by a newline.

**Output **

For each integer  in the inclusive interval [ a, b]:

If 1 ≤ n ≤ 9, then print the English representation of it in lowercase. That is "one" for 1, "two" for 2, and so on.
Else if n > 9 and it is an even number, then print "even".
Else if n > 9 and it is an odd number, then print "odd".
Note: [a,b] = {x ∈ Z | a ≤ x ≤ b } = { a + a + 1 ..., b}

Sample Input

8
11
Sample Output

eight
nine
even
odd

# [**Functions**](https://www.hackerrank.com/challenges/c-tutorial-functions/problem?isFullScreen=true)
Functions are a bunch of statements glued together. A function is provided with zero or more arguments, and it executes the statements on it. Based on the return type, it either returns nothing (void) or something.

The syntax for a function is

return_type function_name(arg_type_1 arg_1, arg_type_2 arg_2, ...) {
    ...
    ...
    ...
    [if return_type is non void]
        return something of type `return_type`;
}
For example, a function to return the sum of four parameters can be written as

int sum_of_four(int a, int b, int c, int d) {
    int sum = 0;
    sum += a;
    sum += b;
    sum += c;
    sum += d;
    return sum;
}
Write a function int max_of_four(int a, int b, int c, int d) which returns the maximum of the four arguments it receives.

+= : Add and assignment operator. It adds the right operand to the left operand and assigns the result to the left operand.
a += b is equivalent to a = a + b;
Input Format

Input will contain four integers -  a,b,c,d, one per line.

Output Format

Return the greatest of the four integers.
PS: I/O will be automatically handled.

Sample Input

3
4
6
5
Sample Output

6

# [**Pointer**](https://www.hackerrank.com/challenges/c-tutorial-pointer/problem?isFullScreen=true)	
A pointer in C++ is used to share a memory address among different contexts (primarily functions). They are used whenever a function needs to modify the content of a variable, but it does not have ownership.
	
In order to access the memory address of a variable,val , prepend it with & sign. For example, &val returns the memory address of val.

This memory address is assigned to a pointer and can be shared among various functions. For example, int * p = &val  will assign the memory address of val to pointer p. To access the content of the memory to which the pointer points, prepend it with a *. For example, *p will return the value reflected by val and any modification to it will be reflected at the source (val).

	void increment(int *v) {
        (*v)++; 
    }
      	int main() {
        int a;
        scanf("%d", &a);
        increment(&a);
        printf("%d", a);
    	return 0;      
    }     
Task
a' = a + b
b' = |a - b|

Complete the function void update(int *a,int *b). It receives two integer pointers, int* a and int* b. Set the value of  to their sum, and  to their absolute difference. There is no return value, and no return statement is needed.

**Input**

The input will contain two integers,  and , separated by a newline.

**Output**

Modify the two values in place and the code stub main() will print their values.

Note: Input/ouput will be automatically handled. You only have to complete the function described in the 'task' section.

Sample Input

4
5
Sample Output

9
1

