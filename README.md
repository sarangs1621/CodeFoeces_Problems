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

# A. Watermelon
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

**Input**

The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

**Output**

Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

