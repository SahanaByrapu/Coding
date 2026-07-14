#!/bin/bash

# -------- Week 1: Arrays --------
week1=(
"Day_01_Array_Fundamentals:Contains Duplicate;Remove Duplicates from Sortted Array;Two Sum"
"Day_02_Two_Pointer:Valid Palindrome;Two Sum II;Three Sum"
"Day_03_Sliding_Window:Max Consecutive Ones III;Minimum Size Subarray Sum;Longest Substring Without Repeating Characters"
"Day_04_Advanced_Arrays:Container With Most Water;Trapping Rain Water"
"Day_05_Binary_Search_Technique:Search in Rotated Sorted Array;Find Peak Element;Search Insert Position"
)

# -------- Week 2: Strings --------
week2=(
"Day_01_String_Fundamentals:Valid Anagram;Reverse String;Implement strStr"
"Day_02_Character_Counting:First Unique Character;Ransom Note"
"Day_03_Valid_Parentheses_and_Stacks:Valid Parentheses;Remove Outermost Parentheses"
"Day_04_String_Manipulation:Longest Common Prefix;Add Strings"
"Day_05_String_Search:Repeated Substring Pattern;Count and Say"
)

# -------- Week 3: Linked List --------
week3=(
"Day_01_LL_Fundamentals:Reverse Linked List;Middle of the Linked List"
"Day_02_LL_Operations:Merge Two Sorted Lists;Linked List Cycle"
"Day_03_LL_Algorithms:Remove Nth Node;Add Two Numbers"
"Day_04_Dummy_Node_Problems:Palindrome Linked List;Intersection of Two Linked Lists"
"Day_05_LL_Fast_Slow:Reorder List;Sort List"
)

# -------- Week 4: Binary Trees --------
week4=(
"Day_01_Tree_Traversals:Binary Tree Inorder Traversal;Binary Tree Preorder Traversal;Binary Tree Postorder Traversal"
"Day_02_Level_Order:Binary Tree Level Order Traversal;Average of Levels"
"Day_03_Tree_Properties:Is Balanced;Diameter of Binary Tree"
"Day_04_Tree_Applications:Path Sum;Invert Binary Tree"
"Day_05_Construct_Trees:Construct Binary Tree;Construct BST from Preorder"
)

# -------- Week 5: Graphs Fundamentals --------
week5=(
"Day_01_Graph_Basics:Find if Path Exists;Number of Provinces"
"Day_02_BFS_DFS:Rotting Oranges;Open the Lock"
"Day_03_Graph_Problems:Course Schedule;Course Schedule II"
"Day_04_Grid_Problems:Number of Islands;Max Area of Island"
"Day_05_Graph_Advanced:Word Ladder;Clone Graph"
)

# -------- Week 6: Graph Algorithms --------
week6=(
"Day_01_Topological_Sort:Alien Dictionary;Topological Sort Practice"
"Day_02_Dijkstra:Network Delay Time;Cheapest Flights Within K Stops"
"Day_03_Bellman_Ford:Negative Weight Cycle;Bellman-Ford Practice"
"Day_04_Floyd_Warshall:All Pairs Shortest Path"
"Day_05_MST:Kruskal;Prim"
)

# -------- Week 7: Binary Search & Greedy --------
week7=(
"Day_01_Binary_Search_Advanced:Search Range;Find Minimum in Rotated Array"
"Day_02_Parametric_Search:Koko Eating Bananas;Minimize Max Distance"
"Day_03_Greedy:Jump Game;Gas Station"
"Day_04_Greedy_Advanced:Non Overlapping Intervals;Partition Labels"
"Day_05_Greedy_Optimization:Maximum Subarray;Best Time to Buy and Sell Stock"
)

# -------- Week 8: Backtracking --------
week8=(
"Day_01_Backtracking_Fundamentals:Subsets;Combinations"
"Day_02_Permutations:Permutations;Letter Case Permutation"
"Day_03_Combination_Sum:Combination Sum;Combination Sum II"
"Day_04_Backtracking_Trees:Word Search;Palindrome Partitioning"
"Day_05_Advanced_Backtracking:N-Queens;Sudoku Solver"
)

# -------- Week 9: Stacks, Queues & Heaps --------
week9=(
"Day_01_Stacks:Min Stack;Valid Parentheses"
"Day_02_Queues:Implement Queue;Sliding Window Maximum"
"Day_03_Heaps:Kth Largest Element;Top K Frequent Elements"
"Day_04_Priority_Queues:Merge K Sorted Lists;Task Scheduler"
"Day_05_Monotonic_Stacks:Daily Temperatures;Largest Rectangle in Histogram"
)

# -------- Week 10: Hashmap --------
week10=(
"Day_01_Hashmap_Fundamentals:Two Sum;Contains Duplicate"
"Day_02_Hashmap_Counting:Majority Element;Isomorphic Strings"
"Day_03_Hashmap_Sets:Happy Number;Intersection of Two Arrays"
"Day_04_Hashmap_Frequency:Top K Frequent Words;Group Anagrams"
"Day_05_Hashmap_Advanced:Subarray Sum Equals K;Longest Consecutive Sequence"
)

# -------- Week 11: Tries --------
week11=(
"Day_01_Trie_Basics:Implement Trie;Search Suggestions System"
"Day_02_Trie_Advanced:Word Dictionary;Replace Words"
"Day_03_Trie_Optimization:Longest Word in Dictionary;Prefix Score"
"Day_04_Pattern_Matching:Word Search II;Add and Search Word"
"Day_05_Trie_Applications:Phone Directory;Maximum XOR"
)

# -------- Week 12: Segment Trees --------
week12=(
"Day_01_ST_Basics:Range Sum Query;Range Minimum Query"
"Day_02_ST_Build:Segment Tree Build;Lazy Propagation Intro"
"Day_03_ST_Updates:Point Update;Range Update"
"Day_04_ST_Problems:Minimum in Range;Range Query 2D"
"Day_05_ST_Advanced:Advanced ST Problems;Fenwick Tree Basics"
)

# -------- Week 13: Dynamic Programming --------
week13=(
"Day_01_DP_Fundamentals:Climbing Stairs;House Robber"
"Day_02_DP_1D:Longest Increasing Subsequence;Coin Change"
"Day_03_DP_2D:Edit Distance;Interleaving String"
"Day_04_DP_Knapsack:0/1 Knapsack;Partition Equal Subset Sum"
"Day_05_DP_Advanced:Longest Palindromic Subsequence;Catalan Numbers"
)

# All weeks in one array
all_weeks=(
  "Week_01_Arrays:${week1[*]}"
  "Week_02_Strings:${week2[*]}"
  "Week_03_LinkedList:${week3[*]}"
  "Week_04_BinaryTrees:${week4[*]}"
  "Week_05_Graphs_Basics:${week5[*]}"
  "Week_06_Graphs_Algorithms:${week6[*]}"
  "Week_07_BinarySearch_Greedy:${week7[*]}"
  "Week_08_Backtracking:${week8[*]}"
  "Week_09_Stacks_Queues_Heaps:${week9[*]}"
  "Week_10_Hashmap:${week10[*]}"
  "Week_11_Tries:${week11[*]}"
  "Week_12_SegmentTrees:${week12[*]}"
  "Week_13_DP:${week13[*]}"
)

# -------- Folder Generation --------
for week_data in "${all_weeks[@]}"; do
    week_name="${week_data%%:*}"
    days_string="${week_data#*:}"

    mkdir -p "$week_name"

    IFS=' ' read -r -a days <<< "$days_string"

    for day_entry in "${days[@]}"; do
        day_name="${day_entry%%:*}"
        problems_string="${day_entry#*:}"

        day_path="$week_name/$day_name"
        mkdir -p "$day_path"

        IFS=';' read -r -a problems <<< "$problems_string"
        for prob in "${problems[@]}"; do
            sanitized=$(echo "$prob" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd 'a-z0-9_')
            mkdir -p "$day_path/$sanitized"
        done
    done
done

echo "🎉 Folder structure generated successfully!"