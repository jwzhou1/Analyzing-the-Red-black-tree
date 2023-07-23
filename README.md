# Research Paper
* Name: Jiawei Zhou
* Semester: Summer 2023
* Topic: Red–black tree
* Link The Repository: https://github.com/jwzhou1/FinalResearchPaper.git


## Introduction
- Provide an introduction to the rest of the paper. 

In the domain of computer science, the significance of data structures cannot be overstated when it comes to effectively organizing and managing extensive volumes of data. Within the wide spectrum of available data structures, Red-Black Trees emerge as a sophisticated and highly efficient solution for maintaining ordered data while guaranteeing balanced performance. In this final research paper, we will delve into the complexities of Red-Black Trees, their role in addressing fundamental problems, and embark on an intriguing journey through their historical evolution.

Red-Black Trees are a type of self-balancing binary search trees (BSTs) that offer a systematic and flexible approach to organizing data, especially in scenarios involving dynamic insertion and deletion operations. These trees enhance the standard BST structure by incorporating additional properties and operations to maintain balance, resulting in efficient and predictable runtime complexity.

The most notable characteristic of Red-Black Trees is the color assigned to each of their nodes, which can be either red or black. This color scheme plays a crucial role in achieving a balanced tree structure in terms of depth and height, thereby ensuring efficient search, insertion, and deletion operations. Through adherence to specific rules and constraints, Red-Black Trees maintain a balance that guarantees a worst-case time complexity of O(log n) for fundamental operations.

Example of a red–black tree:  

<img src="images/example1fromwiki.png" alt="redblacktreeexample1" width="500"/>

Figure 1: A red–black tree with explicit NIL leaves [1]

<img src="images/example2fromwiki.png" alt="redblacktreeexample1" width="500"/>  

Figure 2: A red–black tree with implicit left and right docking points [1]  

Red-Black Trees are designed to address the challenge of maintaining a balanced binary search tree while accommodating dynamic updates. Although standard binary search trees offer efficient search, insertion, and deletion operations on average, their worst-case time complexity can deteriorate to O(n) when the tree becomes highly unbalanced. This imbalance typically occurs when elements are inserted or deleted in a sorted order, resulting in a skewed tree.

Red-Black Trees mitigate this issue by implementing a set of rules and operations that ensure structural balance. These trees guarantee that the longest path from the root to any leaf node is no more than twice as long as the shortest path, thus promoting a balanced and effective search tree for various applications.

The concept of Red-Black Trees emerged from the pioneering work of Rudolf Bayer, who introduced this tree structure in 1972 during his Ph.D. studies at the University of Karlsruhe, Germany. Bayer's innovative idea involved annotating nodes with color information to achieve balance, giving birth to the red-black paradigm. [2]

Building upon Bayer's initial concept, he collaborated with his colleague Volker Günter and published a seminal paper in 1978 titled "Symmetric Binary B-Trees: Data Structure and Maintenance Algorithms." This influential publication provided a comprehensive exploration of red-black trees, delving into the intricate details of maintaining the tree's balance. The paper outlined the rules for ensuring the correct coloring and structural properties of red-black trees, along with efficient algorithms for performing insertion and deletion operations.

Since their inception, Red-Black Trees have gained widespread recognition and adoption within the realms of computer science and software engineering. They have become integral components of numerous programming languages and libraries, serving as the fundamental building blocks for various essential operations such as associative arrays, ordered sets, and dictionaries.

Red-Black Trees, as a foundational data structure in computer science, offer an elegant and efficient solution to the challenge of maintaining balanced binary search trees. By employing a clever color-coding scheme and adhering to specific rules, these trees provide fast search, insertion, and deletion operations. They exhibit a guaranteed worst-case time complexity of O(log n), ensuring reliable performance even for large datasets. The historical significance of Red-Black Trees, stemming from the groundbreaking work of Rudolf Bayer and Volker Günter, has solidified their position as a cornerstone in the field of algorithms and data structures.

Through their balanced efficiency, Red-Black Trees continue to empower developers in effectively managing and organizing data for a wide range of applications. Their elegant design and practicality have made them an indispensable tool for efficient and reliable data storage and retrieval. As the field of computer science advances, Red-Black Trees maintain their relevance and remain a crucial resource for optimizing algorithmic performance and data management in various domains.  

In this comprehensive study, we embark on an exploration to gain a deep understanding of Red-Black Trees, uncovering their construction, maintenance, and the theoretical principles that underpin their exceptional properties. Our investigation will extensively cover balancing algorithms and intricacies like color propagation, essential for comprehending how these trees maintain their balance.

The objectives of this research are diverse. Our primary aim is to provide readers with a comprehensive understanding of the fundamental principles and unique characteristics that distinguish Red-Black Trees from other balanced binary search trees. We will thoroughly examine the rules governing their construction and explore how the insertion and deletion processes dynamically adapt to maintain balance.

As part of our investigation, we will conduct a comparative analysis of Red-Black Trees against other balancing techniques, critically assessing their strengths and weaknesses. By contrasting them with alternatives such as AVL Trees, B-Trees, and Splay Trees, our study aims to offer valuable insights to aid readers in selecting the most suitable data structure for specific use cases.

In conclusion, this study seeks to be a comprehensive and informative resource for students, researchers, and professionals keen on exploring the elegance and efficiency of Red-Black Trees. By grasping the inner workings of these trees, we can leverage their power to develop faster, more reliable algorithms and applications that will undoubtedly shape the future of computer science and software engineering.


## Analysis of Algorithm/Datastructure
A Red-Black Tree is a type of self-balancing binary search tree that ensures the tree remains approximately balanced during insertions and deletions. It achieves this balance through a set of rules and operations that maintain certain properties of the tree. These properties include [3]:

1. The tree is a self-balancing Binary Search Tree, which means it automatically maintains balance through rotations or node recoloring.

2. This tree data structure goes by the name "Red-Black tree" since each node is either Red or Black. A unique bit is used to represent the color of each node - 0 for black and 1 for red. Apart from this, nodes in the tree store typical binary tree information like data, left pointer, and right pointer.

3. The root node of the Red-Black tree is always colored black.

4. Unlike regular binary trees where leaf nodes have no children, in the Red-Black tree, nodes without children are considered internal nodes. These internal nodes are connected to special NIL nodes, which are always colored black, and these NIL nodes act as the leaf nodes in the Red-Black tree.

5. A crucial property of the Red-Black tree is that if a node is colored red, then its children must be colored black. Essentially, there are no red-red parent-child relationships allowed.

6. Another important property of the Red-Black tree is that every path from a node to any of its descendant NIL nodes should have the same number of black nodes. This ensures that the tree remains balanced and guarantees logarithmic height.

While every AVL tree can be transformed into a Red-Black tree by assigning each node a color, it's important to note that not every Red-Black tree can be considered an AVL tree. The reason for this distinction lies in their respective balancing properties. AVL trees adhere to strict height-balance conditions, ensuring that the height difference between the left and right subtrees of any node is no more than one. On the other hand, Red-Black trees, while self-balancing, do not enforce complete height-balance and may have a greater height difference between subtrees. As a result, a Red-Black tree might not meet the criteria to be classified as an AVL tree.

Let's begin with a comprehensive overview of the time and space complexity of Red-Black Tree operations[4]:
| OPERATION | AVERAGE CASE | WORST CASE |
|-----------|--------------|------------|
| Space     | O(n)         | O(n)       |
| Search    | O(log n)     | O(log n)   |
| Insert    | O(log n)     | O(log n)   |
| Delete    | O(log n)     | O(log n)   |

**Insertion in Red Black tree**

Below are the rules used to construct a Red-Black tree [3]:

1. If the tree is empty, a new node is created as the root node with a black color.
2. If the tree is not empty, a new node is added as a leaf node with a red color.
3. If the parent of a new node is black, no further adjustments are needed, and the insertion process exits.
4. If the parent of a new node is red, the color of the parent's sibling is checked:
   - If the sibling's color is black, rotations and recoloring are performed to maintain the Red-Black tree properties.
   - If the sibling's color is red, the node is recolored. Additionally, if the parent's parent of the new node is not the root node, the process is repeated by recoloring and rechecking the node until the Red-Black tree properties are satisfied.

Let's explore the insertion process in the Red-Black tree using the following elements from javatpoint.com [3]:

**10, 18, 7, 15, 16, 30, 25, 40, 60**

Step 1: At the beginning, the tree is empty, and we introduce a new node with a value of 10. Since this is the first node in the tree, it becomes the root node. As mentioned earlier, the root node must always be colored black, as illustrated below:

<img src="images/insert1.png" alt="insert1" width="100"/>

Step 2: The subsequent node is 18. Since 18 is greater than 10, it will be placed to the right of 10, as demonstrated below:

<img src="images/insert2.png" alt="insert2" width="120"/>

Following the second rule of the Red-Black tree, when the tree is not empty, the newly created node will have the color Red. Therefore, node 18 is given the Red color.

Next, we proceed to check the third rule of the Red-Black tree, which requires that the parent of the new node must be black. In the previous figure, it can be observed that the parent of node 18 is indeed black, thereby confirming that the tree maintains the properties of a valid Red-Black tree.  

Step 3: Moving forward, we introduce a new node with a value of 7 and assign it the color Red. Since 7 is less than 10, it is placed to the left of node 10, as illustrated below:

<img src="images/insert3.png" alt="insert3" width="130"/>

Now, let's proceed to validate the third rule of the Red-Black tree, which ensures that the parent of the new node is black. Upon observation, we can confirm that the parent of node 7 is indeed black in color, thus adhering to the properties of the Red-Black tree.

Step 4: Moving on to the next element, which is 15, we find that it is greater than 10 but less than 18. Consequently, a new node is created to the left of node 18. As per the Red-Black tree rules, the node 15 will be colored Red since the tree is not empty.

The preceding tree exhibits a violation of the Red-Black tree property due to the presence of a Red-red parent-child relationship. To rectify this, we need to apply specific rules to maintain a valid Red-Black tree structure.

Rule 4 of Red-Black trees states that if the new node's parent is Red, we must examine the color of the parent's sibling node. In this case, the new node is node 15, its parent is node 18, and the sibling of the parent node is node 7. Since the color of the parent's sibling (node 7) is Red, we apply Rule 4a. According to Rule 4a, we need to recolor both the parent and the parent's sibling node. Consequently, both nodes 7 and 18 will be recolored, resulting in the updated figure below:

<img src="images/insert4.png" alt="insert4" width="140"/>

Another crucial check we need to perform is whether the parent's parent of the new node is the root node or not. Upon observation in the above figure, it is evident that the parent's parent of the new node (node 15) is indeed the root node (node 10). As a result, there is no need to recolor the root node in this scenario.

Step 5: Proceeding with the next element, which is 16, we observe that it is greater than 10, but less than 18 and greater than 15. Consequently, node 16 will be placed to the right of node 15. As the tree is not empty, node 16 will be colored Red.

<img src="images/insert5.png" alt="insert5" width="180"/>

In the previous figure, it is evident that a violation of the parent-child relationship exists due to the presence of a red-red parent-child relationship. To address this issue and create a valid Red-Black tree, we need to apply certain rules. Since the new node's parent is red and the parent has no sibling, we will apply rule 4a, which involves performing rotations and recoloring on the tree.

As node 16 is to the right of node 15, and the parent of node 15 is node 18, we encounter an LR (Left-Right) relationship, which requires two rotations. Initially, a left rotation is performed on nodes 15 and 16, resulting in node 16 moving upward, and node 15 moving downward. The tree after the left rotation appears as shown below:  

<img src="images/insert6.png" alt="insert6" width="200"/>

In the previous figure, we can observe that there exists an LL (Left-Left) relationship. Due to the Red-red conflict in the tree, we need to perform a right rotation to resolve it. After executing the right rotation, the median element, which is node 16, will become the root node. Consequently, nodes 15 and 18 will be placed as the left child and right child, respectively, as illustrated in the following figure:

<img src="images/insert7.png" alt="insert7" width="200"/>

Following the rotation, both node 16 and node 18 will undergo recoloring. Node 16, which is currently red, will change to black, while node 18, which is black, will change to red. The resulting tree structure is illustrated in the figure below:

<img src="images/insert8.png" alt="insert8" width="200"/>

Step 6: Moving forward, the next element to insert is 30. Node 30 will be added to the right of node 18. Since the tree is not empty, the color of node 30 will be red.

<img src="images/insert9.png" alt="insert9" width="200"/>



Make sure to include the following:
- Time Complexity
- Space Complexity
- General analysis of the algorithm/datastructure

## Empirical Analysis
- What is the empirical analysis?
- Provide specific examples / data.


## Application
- What is the algorithm/datastructure used for?
- Provide specific examples
- Why is it useful / used in that field area?
- Make sure to provide sources for your information.


## Implementation
- What language did you use?
- What libraries did you use?
- What were the challenges you faced?
- Provide key points of the algorithm/datastructure implementation, discuss the code.
- If you found code in another language, and then implemented in your own language that is fine - but make sure to document that.


## Summary
- Provide a summary of your findings
- What did you learn?

## Reference
[1] Red-black tree. In Wikipedia. Retrieved July 15, 2023, from https://en.wikipedia.org/wiki/Red%E2%80%93black_tree   
[2] Huja, H. Red-Black Tree. Medium. Retrieved July 15, 2023, from https://hardikahuja99.medium.com/red-black-tree-8cf904034a90  
[3] JavaTpoint. Red-Black Tree. Retrieved July 15, 2023, from https://www.javatpoint.com/red-black-tree  
[4] OpenGenus IQ. Time and Space Complexity of Red-Black Tree. Retrieved July 15, 2023, from https://iq.opengenus.org/time-and-space-complexity-of-red-black-tree/  