# Climbing Stairs

## 🚀 Problem Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

---

## 🔗 LeetCode Problem Link

[Climbing Stairs - LeetCode](https://leetcode.com/problems/climbing-stairs/)

---

## 🧠 Problem Explanation

- The goal is to determine how many **distinct ways** you can reach the top of the staircase.
- You are allowed to take either **1 step** or **2 steps** at a time.
- This is a classic **dynamic programming** problem.
- It can be solved by observing that to reach step `n`, you could have:
  - Come from step `n - 1` (by taking 1 step), or
  - Come from step `n - 2` (by taking 2 steps).
- So the recurrence is:
  `ways(n) = ways(n - 1) + ways(n - 2)`

```plaintext
Input: 3
Output: 3
Explanation: The distinct ways are:
  1. 1 + 1 + 1
  2. 1 + 2
  3. 2 + 1
