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
| Space     | $O(n)$       | $O(n)$     |
| Search    | $O(log n)$   | $O(log n)$ |
| Insert    | $O(log n)$   | $O(log n)$ |
| Delete    | $O(log n)$   | $O(log n)$ |


**Search in Red-Black tree**

A Red-Black tree takes O(log n) time for search because it is a type of self-balancing binary search tree. The Red-Black tree maintains its balance by enforcing certain properties that ensure its height remains logarithmic with respect to the number of nodes (n) in the tree.

Because of properties of red-black trees, the longest path from the root to any leaf node cannot be more than twice the length of the shortest path from the root to any leaf node. This guarantees that the tree is balanced, and the height of the tree remains logarithmic with respect to the number of nodes (O(log n)).

As a result, the search operation in a Red-Black tree takes O(log n) time complexity, which is very efficient for large datasets, making it a preferred data structure for various applications.

Since the Red-Black tree is a type of binary search tree, the search operation in a Red-Black tree is analogous to the search operation in a binary search tree.

To better grasp the search operation in a Red-Black tree, let's consider the below binary search tree from Javatpoint.com [3]:

<img src="images/search1.png" alt="search1" />

In the above tree, if we want to search for the value 80, the search process proceeds as follows:

1. We start by comparing 80 with the root node, which is 10. Since 80 is greater than 10, we continue the search on the right subtree.
2. Next, we compare 80 with the node 15. As 80 is greater than 15, we move to the right child of 15, which is 20.
3. We reach the leaf node 20, but since 20 is not equal to 80, the search concludes, indicating that the element 80 is not found in the tree.

Throughout each step of the search operation, the tree effectively divides in half. As a result, the Binary Search Tree (BST) structure enables the search to take O(log n) time complexity, making it an efficient search operation for balanced trees like the one shown above.


**Insertion in Red-Black tree**

A Red-Black tree takes O(log n) time for insertion because it is designed as a self-balancing binary search tree. The Red-Black tree maintains its balanced structure through a series of color adjustments and rotations during the insertion process.

When inserting a new node into the Red-Black tree, it starts as an ordinary binary search tree insertion. The new node is initially colored as red to preserve the other properties of the Red-Black tree. Once the node is inserted, a series of color adjustments and rotations are performed to restore and maintain the Red-Black tree properties.

Firstly, below are the rules used to construct a Red-Black tree [3]:

1. If the tree is empty, a new node is created as the root node with a black color.
2. If the tree is not empty, a new node is added as a leaf node with a red color.
3. If the parent of a new node is black, no further adjustments are needed, and the insertion process exits.
4. If the parent of a new node is red, the color of the parent's sibling is checked:  
   a. If the sibling's color is black, rotations and recoloring are performed to maintain the Red-Black tree properties.  
   b. If the sibling's color is red, the node is recolored. Additionally, if the parent's parent of the new node is not the root node, the process is repeated by recoloring and rechecking the node until the Red-Black tree properties are satisfied.

Let's explore the insertion process in the Red-Black tree using the following elements from javatpoint.com [3]:

**10, 18, 7, 15, 16, 30, 25**

**Step 1:** At the beginning, the tree is empty, and we introduce a new node with a value of 10. Since this is the first node in the tree, it becomes the root node. As mentioned earlier, the root node must always be colored black, as illustrated below:

<img src="images/insert1.png" alt="insert1" width="100"/>

**Step 2:** The subsequent node is 18. Since 18 is greater than 10, it will be placed to the right of 10, as demonstrated below:

<img src="images/insert2.png" alt="insert2" width="120"/>

Following the second rule of the Red-Black tree, when the tree is not empty, the newly created node will have the color Red. Therefore, node 18 is given the Red color.

Next, we proceed to check the third rule of the Red-Black tree, which requires that the parent of the new node must be black. In the previous figure, it can be observed that the parent of node 18 is indeed black, thereby confirming that the tree maintains the properties of a valid Red-Black tree.  

**Step 3:** Moving forward, we introduce a new node with a value of 7 and assign it the color Red. Since 7 is less than 10, it is placed to the left of node 10, as illustrated below:

<img src="images/insert3.png" alt="insert3" width="130"/>

Now, let's proceed to validate the third rule of the Red-Black tree, which ensures that the parent of the new node is black. Upon observation, we can confirm that the parent of node 7 is indeed black in color, thus adhering to the properties of the Red-Black tree.

**Step 4:** Moving on to the next element, which is 15, we find that it is greater than 10 but less than 18. Consequently, a new node is created to the left of node 18. As per the Red-Black tree rules, the node 15 will be colored Red since the tree is not empty.

The preceding tree exhibits a violation of the Red-Black tree property due to the presence of a Red-red parent-child relationship. To rectify this, we need to apply specific rules to maintain a valid Red-Black tree structure.

Rule 4 of Red-Black trees states that if the new node's parent is Red, we must examine the color of the parent's sibling node. In this case, the new node is node 15, its parent is node 18, and the sibling of the parent node is node 7. Since the color of the parent's sibling (node 7) is Red, we apply Rule 4a. According to Rule 4a, we need to recolor both the parent and the parent's sibling node. Consequently, both nodes 7 and 18 will be recolored, resulting in the updated figure below:

<img src="images/insert4.png" alt="insert4" width="140"/>

Another crucial check we need to perform is whether the parent's parent of the new node is the root node or not. Upon observation in the above figure, it is evident that the parent's parent of the new node (node 15) is indeed the root node (node 10). As a result, there is no need to recolor the root node in this scenario.

**Step 5:** Proceeding with the next element, which is 16, we observe that it is greater than 10, but less than 18 and greater than 15. Consequently, node 16 will be placed to the right of node 15. As the tree is not empty, node 16 will be colored Red.

<img src="images/insert5.png" alt="insert5" width="180"/>

In the previous figure, it is evident that a violation of the parent-child relationship exists due to the presence of a red-red parent-child relationship. To address this issue and create a valid Red-Black tree, we need to apply certain rules. Since the new node's parent is red and the parent has no sibling, we will apply rule 4a, which involves performing rotations and recoloring on the tree.

As node 16 is to the right of node 15, and the parent of node 15 is node 18, we encounter an LR (Left-Right) relationship, which requires two rotations. Initially, a left rotation is performed on nodes 15 and 16, resulting in node 16 moving upward, and node 15 moving downward. The tree after the left rotation appears as shown below:  

<img src="images/insert6.png" alt="insert6" width="200"/>

In the previous figure, we can observe that there exists an LL (Left-Left) relationship. Due to the Red-red conflict in the tree, we need to perform a right rotation to resolve it. After executing the right rotation, the median element, which is node 16, will become the root node. Consequently, nodes 15 and 18 will be placed as the left child and right child, respectively, as illustrated in the following figure:

<img src="images/insert7.png" alt="insert7" width="200"/>

Following the rotation, both node 16 and node 18 will undergo recoloring. Node 16, which is currently red, will change to black, while node 18, which is black, will change to red. The resulting tree structure is illustrated in the figure below:

<img src="images/insert8.png" alt="insert8" width="200"/>

**Step 6:** Moving forward, the next element to insert is 30. Node 30 will be added to the right of node 18. Since the tree is not empty, the color of node 30 will be red.

<img src="images/insert9.png" alt="insert9" width="200"/>

The new node's parent and its parent's sibling are both initially Red in color, leading to the application of rule 4b. Rule 4b solely involves recoloring without any need for rotations. Consequently, both the parent (node 18) and its sibling (node 15) change their color to black, as depicted in the image below.

<img src="images/insert10.png" alt="insert10" width="200"/>

Additionally, we need to verify the status of the parent's parent of the new node to determine if it is the root node. In this case, the parent's parent of the new node (node 30) is node 16, and node 16 is not the root node. Consequently, we will reassign the color of node 16 to Red. The parent of node 16 is node 10, and it is not Red in color, thus ensuring there is no Red-red conflict in the tree structure.

<img src="images/insert11.png" alt="insert11" width="200"/>

**Step 7:** Let's now insert the next element, 25, into the tree. Considering the values of existing nodes, we find that 25 falls between 10, 16, 18, and 30. Therefore, it will be placed to the left of node 30. Since the tree is not empty, we'll mark node 25 as Red.

Here comes the tricky part, a Red-red conflict arises since the parent of the newly inserted node is also Red.

To resolve this, we apply rule 4a, which involves both rotation and recoloring. Since there's no parent's sibling in this scenario, we proceed with the rotations first.

Given that the newly inserted node is on the left of its parent, and the parent node is on the right of its parent, a "RL" relationship is formed. As a result, we perform a right rotation, which moves node 25 upwards, while node 30 goes downwards. The figure below illustrates this transformation.

<img src="images/insert12.png" alt="insert12" width="200"/>

Following the initial rotation, an RR relationship is established, prompting a subsequent left rotation. As a result of the right rotation, the central element, 25, assumes the position of the root node. Node 30 will be situated to the right of 25, while node 18 will find its place on the left side of node 25.

<img src="images/insert13.png" alt="insert13" width="220"/>

Now, we proceed with the recoloring step. Nodes 25, 18 and 15 will undergo recoloring. Specifically, node 25 and 15 will change its color to black, while node 18 will assume a red color.

<img src="images/insert14.png" alt="insert14"/>

The tree depicted above adheres to all the properties of a Red-Black tree, making it a valid Red-Black tree. This example has been sourced from javatpoint.com [3].

Let's explore another insertion example in the Red-Black tree using the following elements from catherine-leung.gitbook [3]:

**30 50 40 20 10**

Let's start with an empty tree. The images presented below represent null nodes (empty subtrees), which are indicated by black circles.

<img src="images/insert15.png" alt="insert15"/>

We will now insert the node with a value of 30 into the red-black tree. During the insertion process, all nodes are initially added as red nodes.

<img src="images/insert16.png" alt="insert16"/>

When inserting a node into the red-black tree, if the root node turns out to be red, we need to change its color to black to satisfy the red-black tree properties.

<img src="images/insert17.png" alt="insert17"/>

Let's proceed with the insertion of a node with a value of 50 into the red-black tree. Since the parent node is black, we can directly insert the new node as a red node without making any further adjustments.

<img src="images/insert18.png" alt="insert18"/>

We will now insert a node with a value of 40 into the red-black tree. This new node will be inserted as a red node.

<img src="images/insert19.png" alt="insert19"/>

We have two red nodes in a row in the red-black tree. Let's identify the nodes involved:

- P (Parent - Upper red) = 50
- C (Child - Lower red) = 40
- G (Grandparent) = 30
- PS (Parent's Sibling) = Null node to the left of 30

Since the parent's sibling (PS) is black, we need to fix this by performing a rotation. The type of rotation required depends on the configuration of G, P, and C. If the path from G to C is straight (both left or both right), we perform a zigzag (single) rotation. If it is angled (left then right or right then left), we need to do a zigzag (double) rotation.

<img src="images/insert20.png" alt="insert20"/>

In this particular scenario, we must perform a zigzag (double) rotation. Let's start by rotating nodes 40 and 50.

<img src="images/insert21.png" alt="insert21"/>

After the initial zigzag (double) rotation with nodes 40 and 50, we need to perform another rotation, this time involving nodes 30 and 40. During this rotation, we will also swap the colors of nodes 30 and 40. The zigzag rotation is an additional step that ensures the insertion path follows the same direction.

<img src="images/insert22.png" alt="insert22"/>

Once the rotations are completed, we proceed to exchange the colors between the node that has taken over G's spot (40 in this case) and G (30). Consequently, node 40 will become black, and node 30 will become red. This color exchange ensures that the red-black tree properties are maintained after the insertion process.

<img src="images/insert23.png" alt="insert23"/>

Let's insert a new node with a value of 20 into the red-black tree. This node will be inserted as a red node, and we will proceed with the necessary adjustments to maintain the red-black tree properties.

<img src="images/insert24.png" alt="insert24"/>

We have two red nodes in a row in the red-black tree. Let's identify the nodes involved:

- P (Parent - Upper red) = 30
- C (Child - Lower red) = 20
- G (Grandparent) = 40
- PS (Parent's Sibling) = Null node to the left of 50

Since the parent's sibling (PS) is red, we need to perform an operation called color exchange. We exchange colors between G and its two children (P and PS) to satisfy the red-black tree properties.

<img src="images/insert25.png" alt="insert25"/>

Performing the color exchange in this case violates properties of red-black trees, which states that roots must be black. To rectify this, we simply change the color of the root node (G, which is currently 40) to black. This adjustment ensures that all red-black tree properties are upheld without causing any further issues.

<img src="images/insert26.png" alt="insert26"/>

Let's insert a new node with a value of 10 into the red-black tree. This node will be inserted as a red node, and we will proceed with the necessary adjustments to maintain the red-black tree properties.

<img src="images/insert27.png" alt="insert27"/>

We have two red nodes in a row in the red-black tree. Let's identify the nodes involved:

- P (Parent - Upper red) = 20
- C (Child - Lower red) = 10
- G (Grandparent) = 30
- PS (Parent's Sibling) = Null node to the right of 30

Since the parent's sibling (PS) is black (null nodes are considered black in red-black trees), we need to fix this by performing a rotation. The rotation will always be done with G (30) as the root of the rotation (the A in the rotation diagram).

This time, the path from G to P to C is "left" then "left," so we only need to perform a single rotation. After the rotation, we will swap the colors between G (30) and the node that took G's spot. This adjustment ensures that the red-black tree properties are maintained after the insertion process.

<img src="images/insert28.png" alt="insert28"/>

After completing the necessary adjustments and rotations, the final red-black tree structure will look like this:

<img src="images/insert29.png" alt="insert29" width = "500"/>


**Deletion in Red-Black tree**  

A Red-Black tree takes O(log n) time for deletion because it is a self-balancing binary search tree that maintains its balanced structure during the deletion process. When a node is deleted from the Red-Black tree, a series of color adjustments and rotations are performed to restore and preserve the Red-Black tree properties.

The deletion process in a Red-Black tree begins with a standard binary search tree deletion. Once the node is removed from the tree, the tree's properties may be violated, specifically the properties related to color balance and black height. To maintain these properties, a set of restructuring operations, including color adjustments and rotations, are performed.

Now, let's explore the process of deleting a specific node from the Red-Black tree. We will be employing the following steps to achieve the deletion from GeeksforGeeks [6]:

**1.** To delete a node in the Red-Black Tree, we first perform the standard Binary Search Tree (BST) delete operation. This operation results in the deletion of a node that is either a leaf or has only one child. In the case of an internal node, we copy the successor and then recursively call the delete function for the successor. It is important to note that the successor node is always a leaf node or a node with one child. Let's assume that we want to delete node v, and u represents the child that will replace v. If v is a leaf node, then u is set to NULL (considered as Black in terms of color representation).

**2.** In the simple case where either u or v is red, we mark the replaced child as black. This operation does not affect the black height of the tree. It is worth mentioning that both u and v cannot be red simultaneously, as u is the child of v, and having two consecutive red nodes is not permitted in a Red-Black Tree.

<img src="images/delete1.png" alt="delete1"/>

**3.** When both u and v are Black:  
**3.1** We color u as "double black." This means that after the standard delete operation in a Red-Black Tree, u takes on the double black color. Our goal now is to convert this double black node back to a single black node, maintaining the Red-Black Tree properties. It is important to mention that if v is a leaf node, then u is set to NULL, and in terms of color representation, NULL is considered to be black. Hence, the deletion of a black leaf node also results in a double black situation.

<img src="images/delete2.png" alt="delete2"/>


**3.2** While the current node u is in a double black state and is not the root, the following steps are taken. Let the sibling of the node u be denoted as s.

(a) **If the sibling s is black and at least one of its children is red**, a rotation is performed on s. Let the red child of s be denoted as r. This case can be further divided into four subcases, based on the positions of s and r.

   i. Left-Left Case: In this scenario, s is the left child of its parent, and r is the left child of s, or both children of s are red. This subcase can be visualized as a mirror image of the right-right case.

   ii. Left-Right Case: Here, s is the left child of its parent, and r is the right child of s. This subcase can be envisioned as a mirror image of the right-left case.

   iii. Right-Right Case: In this situation, s is the right child of its parent, and r is the right child of s, or both children of s are red.

   <img src="images/delete3.png" alt="delete3"/>
   
   iv. Right-Left Case: In this scenario, the sibling s is the right child of its parent, and r is the left child of s.

   <img src="images/delete4.png" alt="delete4"/>

(b) If the sibling s is black and both of its children are black, a recoloring is performed, and the process is recursively applied to the parent node if the parent is black.

   <img src="images/delete5.png" alt="delete5"/>

   
   In this case, if the parent was red, there would be no need to recur for the parent; instead, we can simply change its color to black, as combining red and double black results in a single black node.

(c) If the sibling s is red, a rotation is performed to move the old sibling up, followed by recoloring the old sibling and the parent. As a result of this operation, the new sibling becomes black. This transformation mainly converts the tree to a situation with a black sibling (achieved through rotation) and then leads to either case (a) or case (b). This case can be further divided into two subcases:

   i. Left Case: When s is the left child of its parent, a right rotation is applied to the parent node p.

   ii. Right Case: If s is the right child of its parent, a left rotation is performed on the parent node p.

   <img src="images/delete6.png" alt="delete6"/>

   
**3.3** If u is the root, we simply make it a single black node, reducing the black height of the complete tree by 1.



## Empirical Analysis
- What is the empirical analysis?
- Provide specific examples / data.


## Application

Now let's explore various fields and areas where red-black trees are commonly used and why they are preferred for those specific applications:

1. **Dynamic Set Operations:**
   One of the primary applications of red-black trees is to implement dynamic set operations[7], such as searching, insertion, and deletion of elements while maintaining a balanced data structure. The self-balancing property of red-black trees ensures that these operations take O(log n) time, making them efficient for dynamic data sets with frequent updates.

   **Example:** A spell-checker application can use a red-black tree to store a dictionary of words, allowing quick word lookups, insertions of new words, and removal of incorrect words while ensuring the dictionary remains sorted for efficient search operations.

2. **Compiler and Symbol Table:**
   Red-black trees are widely used in compilers and interpreters to build and maintain symbol tables efficiently[8]. A symbol table is a data structure that stores information about variables, functions, and other symbols used in a program. The balanced nature of red-black trees makes them ideal for implementing symbol tables, as they offer efficient insertion and retrieval of symbols.

   **Example:** In a programming language compiler, red-black trees can be used to store the symbols encountered during the parsing phase, allowing the compiler to quickly look up and update symbol information during later stages of compilation.

3. **Operating Systems:**
   Red-black trees find applications in various operating system components, such as process scheduling, file system management, and memory management[9]. They are used to organize and maintain data structures that require fast search and insertion operations while ensuring balanced resource allocation.

   **Example:** In process scheduling, a red-black tree can be utilized to maintain a ready queue of processes, where the nodes represent processes with their respective priorities. The scheduler can quickly find the process with the highest priority, allowing for efficient context switching.

4. **Interval Trees:**
   An interval tree is a specialized form of a red-black tree that stores intervals of values and is used in applications that involve searching for overlapping or intersecting intervals efficiently[10]. Interval trees allow efficient range queries, insertion, and deletion operations.

   **Example:** In a calendar application, an interval tree can be used to store and manage events. The intervals represent the start and end times of events, allowing the application to find overlapping events or retrieve events within a specific time range quickly.

5. **Database Indexing:**
   In databases, red-black trees are often used to implement balanced search trees for indexing[11]. Indexes speed up query processing by allowing rapid data retrieval based on specific attributes or fields, and red-black trees efficiently handle insertions and deletions to maintain the index's balance.

   **Example:** In a relational database management system, a red-black tree index can be used to accelerate search operations on a specific column, reducing the time needed for retrieving relevant rows from large tables.

6. **Network Routing Algorithms:**
   Red-black trees can be applied in network routing algorithms, where they are used to organize and maintain routing information efficiently[12]. The balanced nature of red-black trees ensures that routing tables can be updated and queried quickly.

   **Example:** In computer networks, red-black trees can be used in link-state routing protocols like OSPF (Open Shortest Path First) to maintain and manage the network's topology information. The trees can store and update routing table entries, which are essential for packet forwarding decisions.

7. **Counting and Ranking Operations:**
   Red-black trees can be augmented to support counting and ranking operations on a dynamic set of elements[13]. Augmentation involves adding extra information to each node, enabling efficient counting or ranking queries.

   **Example:** An e-commerce platform can use an augmented red-black tree to maintain the list of products sorted by their popularity or sales count. The tree's augmentation allows the platform to quickly determine the most popular products or provide ranked product lists to users.

   Let's now delve into the benefits and drawbacks of the red-black tree data structure.

   **Advantages of Red-Black Tree:**  
   1. Balancing: Red-black trees maintain a balanced parallel tree, which ensures efficient operations and prevents the tree from becoming skewed.
   2. Efficient Search: The time complexity for search operations is O(log n), making it fast and suitable for large datasets.
   3. Low Constants: Red-black trees have relatively low constants in a wide range of scenarios, leading to efficient performance in practical use cases.
   4. Dynamic Nature: They support dynamic operations like insertion and deletion efficiently while maintaining the balanced property.
   5. Ease of Implementation: Red-black trees are relatively easy to understand and implement, making them accessible for developers.
   6. Flexibility: Suitable for various applications, including database indexing, memory management, and network routing. They handle ordered and unordered data effectively, making them versatile for different data structures.  

   **Disadvantages of Red-Black Tree:**  
   1. Complexity: Managing edge cases and implementing a red-black tree from scratch can be complex, and using standard library implementations is often preferred.
   2. Performance: For scenarios where the tree is built once and only read operations are performed, AVL trees may offer better performance.
   3. Not Ideal for Disk Storage: B-trees are preferred for storing large amounts of data on disks due to their ability to limit disk operations.
   4. Inefficient Concurrent Access: Locking red-black trees perform poorly with simultaneous access compared to locking skip lists, which offer better concurrent performance.
   5. Scalability: As the number of nodes in the tree increases, managing a red-black tree can become challenging and impact performance.
   6. Slow Insertions: Insertions in red-black trees can be relatively slow compared to other data structures like AVL trees.
   7. Not Suitable for Large Datasets: Red-black trees may not be the best choice for handling large datasets efficiently.
   8. Overhead: The self-balancing nature of red-black trees adds overhead to insertion and deletion operations, making them slightly slower compared to non-self-balancing structures.
   9. Worst-case Performance: While red-black trees have good average-case performance, their worst-case performance can be slow compared to other data structures.


## Implementation
- What language did you use?
- What libraries did you use?
- What were the challenges you faced?
- Provide key points of the algorithm/datastructure implementation, discuss the code.

**You can run `RBTreeImp.py` for the Implementation of the Red-Black Tree. You can insert nodes, delete nodes and print the Red-Black Tree in the `RBTreeImp.py` by calling `bst.insert()`, `bst.delete_node()` and `bst.print_tree()` in the main function. My code is inspired from AskPython.com [17].**

I use Python for the implementation of a Red-Black Tree because Python offers several advantages, making it an excellent choice for this purpose. Python is a high-level, interpreted, and dynamically-typed programming language known for its simplicity, ease of use, and rich standard library. These characteristics make Python an attractive choice for developing data structures like the Red-Black Tree. 

One of Python's key strengths is its expressive syntax, which allows developers to write clear and concise code. When implementing complex data structures like the Red-Black Tree, code readability is of paramount importance, especially considering the intricacies involved in maintaining tree balance and color properties. Python's clean and easily understandable syntax aids in implementing the Red-Black Tree algorithms in a more natural and intuitive way. This results in reduced development time, better maintainability, and improved collaboration among team members.

Furthermore, Python's dynamic typing enables flexibility during the implementation process. Red-Black Trees often involve complex data manipulations, such as pointer management and recursive operations. Python's dynamic typing allows developers to focus more on the algorithmic aspects of the Red-Black Tree rather than being encumbered by low-level data type declarations. This enhanced flexibility allows for more efficient experimentation and easier adaptation of the code to different use cases.

Moreover, Python's popularity and large community support ensure the availability of numerous libraries and packages that can enhance the implementation of the Red-Black Tree. For example, developers can use third-party libraries for visualization and debugging, enabling them to gain valuable insights into the tree's structure and properties during development and testing. Additionally, the vast Python community provides ample learning resources, tutorials, and documentation, which can assist graduate students and developers in comprehending the intricacies of Red-Black Trees and improving their implementation skills.

I only use the 'import sys' library. This is a built-in Python module that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter. In my code, it is used to access sys.stdout.write() function, which allows printing output to the console without adding a newline character.

Let's explore the pseudocode for the implementation of Red-Black trees.

The first operation is insertion, which involves adding a new node to a tree. This is accomplished using the insert method with the following algorithm based on CLRS[14] pseudocode for RB-Insert:
```
   RB-Insert(T,z)
      y = nil[T]
      x = root[T]
      while x != nil[T]
            y = x
            if key[z] < key[x] then
               x = left[x]
            else
               x = right[x]
      p[z] = y
      if y = nil[T]
            root[T] = z
      else
         if key[z] < key[y] then
            left[y] = z
         else
            right[y] = z
      left[z] = nil[T]
      right[z] = nil[T]
      color[z] = RED
      RB-Insert-fixup(T,z)

   Parameters:
   value - is an integer to be inserted
```
Here is the insertion function in Python.  
```
  def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)
```
Let's explain the above code step by step: 
1. The code starts with defining a method named `insert`, which takes a single parameter `key`, representing the value to be inserted into the red-black tree.
2. A new node is created using the `Node` class, and the `key` value is assigned to the `item` attribute of the node. The `color` attribute is set to 1 (red). `self.TNULL` likely represents a sentinel node (a special node representing NULL/empty leaves) used in the red-black tree implementation.
3. The variables `y` and `x` are initialized to `None` and `self.root`, respectively. `y` will be used to keep track of the parent of the newly inserted node, and `x` is used to traverse the tree to find the correct position for the new node.
4. A while loop is used to find the correct position in the red-black tree for the new node. It compares the value of the new node with the values of the existing nodes in the tree and decides whether to move left or right based on the comparison. The loop terminates when `x` becomes the sentinel node (`self.TNULL`) indicating that the correct position for insertion has been found.
5. After finding the correct position, the parent of the new node is set to `y`.
6. If `y` is `None`, it means the tree was empty, and the new node becomes the root of the tree.
7. Otherwise, if the value of the new node is less than the value of `y`, it means the new node should be placed as the left child of `y`, and it is assigned as such.
8. Otherwise, the new node is placed as the right child of `y`.
9. If the parent of the new node is `None`, it means the new node is the root of the tree and is colored black (`node.color = 0`), and the insertion process is complete. A black root is one of the properties of a red-black tree.
10. If the grandparent of the new node (`node.parent.parent`) is `None`, it means the new node's parent is the root of the tree. Since the parent of the new node is already black (set in the previous step), all the properties of the red-black tree are satisfied, and the insertion process is complete.
11. If neither of the above conditions is met, it means the new node has a grandparent and requires further adjustments to maintain the red-black tree properties. The method `fix_insert(node)` is then called to handle the fix-up operations necessary to maintain the properties of a red-black tree.

Next, we will have the RBInsertFixup method. It is responsible for ensuring that the Red-Black Properties of the tree are preserved after performing an insertion. Typically, this method would be marked as private since it serves as a helper function. I will follow Andrew's pseudocode [15] which will provide two pseudocode descriptions: the first one is more for understanding, while the second one is closer to an implementation.

```
  RB-Insert-fixup(T,z) {
  while(z's parent is Red) {
      set y to be z's uncle
      if uncle y is Red {
               color parent and uncle black
               color grandparent red
               set z to grandparent
      }
      else {  // the uncle is black
              if (zig zag) { // make it a zig zig
                             set z to parent
                             rotate to zig zig
                           }
              // rotate the zig zig and finish
              color parent of z black
              color grandparent of z red
              rotate grand parent of z
           }
   } // end while
  color root black
 }

  Low-level Pseudo-code for RB-Insert-fixup
  RB-Insert-fixup(T,z)
  while color[p[z]] = RED {
    if p[z] == left[p[p[z]]] {
         y = right[p[p[z]]]
         if color[y] = RED {
             color[p[z]] = BLACK
             color[y] = BLACK
             color[p[p[z]]] = RED
             z = p[p[z]]
         }
         else {
             if z = right[p[z]] {
                  z = p[z]
                  LEFT-Rotate(T,z)
             }
             color[p[z]] = BLACK
             color[p[p[z]]] = RED
             RIGHT-Rotate(T,p[p[z]])
         }
    }
    else {
         y = left[p[p[z]]]
         if color[y] = RED {
             color[p[z]] = BLACK
             color[y] = BLACK
             color[p[p[z]]] = RED
             z = p[p[z]]
         }
         else
             {
             if z = left[p[z]] {
                  z = p[z]
                  RIGHT-Rotate(T,z)
             }
             color[p[z]] = BLACK
             color[p[p[z]]] = RED
             LEFT-Rotate(T,p[p[z]])
         }
    }
    color[root[T]] = BLACK
  }
  
Parameters:
z - is the new node
```

Here is the RBInsertFixup function in Python.  
```
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
```
Let's explain the above code step by step:  
1. The method `fix_insert` takes a single parameter `k`, which represents the newly inserted node that may cause violations in the red-black tree properties.
2. The method uses a `while` loop that continues as long as the parent of node `k` is red (color == 1). This indicates a violation of the red-black tree property that no red node can have a red parent.
3. The code checks whether the parent of node `k` is the right child of its grandparent. This check is to determine whether `k`'s parent is a left child or a right child in its grandparent's subtree.
4. If `k`'s parent is a right child, the code assigns `u` to be the left sibling of `k`'s parent (i.e., `k`'s uncle).
5. If the uncle `u` is red (color == 1), the code performs a series of recoloring operations. The recoloring aims to "push down" the black color to the grandparent and make the parent and uncle black, while the grandparent becomes red. This recoloring allows the fix-up process to move up the tree towards the root to check for further violations.
6. After recoloring, the `k` pointer moves up the tree to the grandparent, as it has now become red due to the recoloring of its child nodes. The loop continues to check if the parent of `k` is red and if the loop should proceed.
7. If the uncle `u` is black (color == 0), the code performs rotations to balance the tree and satisfy the red-black tree properties. The specific rotation depends on the position of `k` and its parent in the grandparent's subtree.
8. If `k` is the left child of its parent and its parent is the right child of the grandparent, a right rotation is performed on the parent to "flip" the subtree and make it a left-left case.
9. After the rotation, the color of the parent and grandparent is adjusted to maintain the properties of the red-black tree.
10. If `k` is the right child of its parent and its parent is the left child of the grandparent, a left rotation is performed on the parent to "flip" the subtree and make it a right-right case.
11. After the rotation, the color of the parent and grandparent is adjusted as before.
12. The loop continues, and the process repeats until the parent of `k` is no longer red or until the root is reached.
13. Finally, the color of the root node is set to black (color == 0), as one of the properties of a red-black tree is that the root must always be black.
Overall, this `fix_insert` method ensures that after inserting a new node into a red-black tree, the tree remains balanced and satisfies all the properties of a red-black tree.




The second operation is deletion. Firstly, we need the `RB-TRANSPLANT` function to handle the replacement of a subtree rooted at node u with a subtree rooted at node v. This function is essential during node deletion in a red-black tree.

The purpose of the RB-TRANSPLANT function is to maintain the integrity of the tree structure and the parent-child relationships after removing a node during the deletion process. The function helps ensure that the red-black tree properties are preserved after a node is removed. Here is the pseudocode for the `RB-TRANSPLANT` function.
```
RB-TRANSPLANT(T,u,v)

if u.p == T.nil
	T.root = v
else if u == u.p.left
	u.p.left = v
else
	u.p.right = v
v.p = u.p
```
Here is the `RB-TRANSPLANT` function in Python.  
```
 def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
```

Let's go through the code step by step to understand the `__rb_transplant` function:

1. The function takes two parameters: `u` (the node to be replaced) and `v` (the node that will replace `u` in the tree).
2. The function first checks if `u.parent` is `None`. If it is, it means that `u` is the root of the entire tree.
3. If `u` is the root, the function directly sets the root of the entire tree to be `v`. This operation effectively replaces the entire tree with the subtree rooted at `v`.
4. If `u` is not the root, the function continues to check if `u` is the left child or the right child of its parent.
5. If `u` is the left child of its parent (`u == u.parent.left`), the function updates the left child reference of the parent to point to `v`. This operation effectively removes `u` from its current position in the tree and replaces it with the subtree rooted at `v`.
6. If `u` is the right child of its parent, the function updates the right child reference of the parent to point to `v`. This operation effectively removes `u` from its current position in the tree and replaces it with the subtree rooted at `v`.
7. Finally, the function updates the parent reference of `v` to be the parent of `u`. This step ensures that the grandparent of the subtree rooted at `v` is properly adjusted to maintain the correct parent-child relationship.

After executing this function, the subtree rooted at node `u` is replaced by the subtree rooted at node `v`, and the parent-child relationships in the tree are correctly updated to maintain the structure and properties of the red-black tree. The `__rb_transplant` function plays a critical role in maintaining the integrity of the tree during node deletion operations and helps ensure that the red-black tree properties are preserved.

Then, we need to have the RB-DELETE(T, z) function to delete nodes which is similar to the deletion process in a normal Binary Search Tree (BST). The core deletion process in the below pseudocode is based on the presence and absence of left and right children of the node to be deleted, z.
```
RB-DELETE(T, z)
  y = z
  y_orignal_color = y.color
  if z.left == T.NIL //no children or only right
      x = z.right
      RB-TRANSPLANT(T, z, z.right)
  else if z.right == T.NIL // only left child
      x = z.left
      RB-TRANSPLANT(T, z, z.left)
  else // both children
      y = MINIMUM(z.right)
      y_orignal_color = y.color
      x = y.right
      if y.parent == z // y is direct child of z
          x.parent = y
      else
          RB-TRANSPLANT(T, y, y.right)
          y.right = z.right
          y.right.parent = y
      RB-TRANSPLANT(T, z, y)
      y.left = z.left
      y.left.parent = y
      y.color = z.color
  if y_orignal_color == black
```

Here is the delete function in Python. 

```
 def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)
```

Let's explain the above code step by step:  

1. The method takes two parameters: `node`, representing the current node being examined during the deletion process, and `key`, the key value of the node that needs to be deleted.
2. A sentinel node `z` is initialized to `self.TNULL`, which is likely a special node representing NULL or empty leaves in the red-black tree.
3. A while loop is used to search for the node with the specified key in the tree starting from the given `node`. If the node with the key is found, it is assigned to `z`, and the loop continues to search further in the appropriate direction.
4. Once the loop ends, the code checks if `z` is still the sentinel node `self.TNULL`. If it is, it means the key was not found in the tree, so a message is printed, and the method returns, indicating that the deletion cannot be performed.
5. If the node with the key is found (stored in `z`), the code continues with the deletion process.
6. `y` is set to `z`, and `y_original_color` is used to store the original color of `y` before deletion. This is done to determine if the color of `y` changes during the deletion process and if further adjustments are needed to maintain the properties of the red-black tree.
7. The code checks if the left child of `z` is the sentinel node (`self.TNULL`). If it is, it means that `z` has no left child or only has a right child.
8. If the left child of `z` is the sentinel node, `x` is set to `z.right`. This will be the node that replaces `z` in the tree.
9. The `__rb_transplant(z, z.right)` method is called to replace node `z` with node `x` in the tree. The `__rb_transplant` method likely handles the removal of a node and ensures the proper adjustment of parent-child relationships.
10. If the right child of `z` is the sentinel node, it means that `z` has only a left child.
11. If the right child of `z` is the sentinel node, `x` is set to `z.left`. Again, this will be the node that replaces `z` in the tree.
12. The `__rb_transplant(z, z.left)` method is called to replace node `z` with node `x` in the tree.
13. If `z` has both left and right children, it enters the `else` block.
14. `y` is set to the minimum node in the right subtree of `z`. This is done to find the successor of `z`, which is the node with the smallest value greater than `z`. The minimum node in the right subtree can replace `z` without violating the order properties of the binary search tree.
15. `y_original_color` is used to store the original color of `y` before deletion.
16. `x` is set to `y.right`, as this will be the node that replaces `y` in the tree.
17. If `y.parent` is equal to `z`, it means that `y` is the direct right child of `z`. In this case, `x.parent` is set to `y`.
18. If `y.parent` is not equal to `z`, it means that `y` is not the direct right child of `z`. In this case, the `__rb_transplant(y, y.right)` method is called to replace node `y` with node `y.right`. This step ensures that `y` is removed from its current position in the tree.
19. After `y` has been removed from its current position, `y.right` is updated to point to `z.right`, and `z.right.parent` is set to `y`. This step preserves the right subtree of `z` when `y` is replaced in the tree.
20. The `__rb_transplant(z, y)` method is called to replace node `z` with node `y` in the tree. This step effectively removes `z` from its current position and replaces it with `y`.
21. `y.left` is updated to point to `z.left`, and `z.left.parent` is set to `y`. This step preserves the left subtree of `z` when `y` is replaced in the tree.
22. The color of `y` is set to the color of `z`. This is done because the color of `y` might change during the deletion process, and we want to ensure that the properties of the red-black tree are maintained.
23. Finally, the code checks if the original color of `y` (`y_original_color`) was black. If it was black, then it means that a black node was removed from the tree, which might lead to a violation of the red-black tree properties. Further adjustments or "fix-ups" may be needed to restore the properties of the red-black tree. The `delete_fix(x)` method (not shown in this code snippet) is likely responsible for handling the necessary fix-up operations.

However, the key difference for Red-Black tree is the RB-DELETE-FIXUP(T, x) function. This is the function responsible for restoring the Red-Black Tree properties after the deletion of a node. In a Red-Black Tree, after a node is deleted (as shown in the given code), the tree might violate one or more Red-Black properties, such as the Red-Black color property and the Black Height property. The RB-DELETE-FIXUP(T, x) function will handle these violations and apply various rotation and recoloring operations to rebalance the tree and ensure that it maintains its Red-Black properties. The fix-up process is what makes the deletion in a Red-Black Tree different from a regular BST deletion. Below is the RB-DELETE-FIXUP(T, x) function pseudocode [16].

```
RB-DELETE-FIXUP(T, x)
  while x!= T.root and x.color == black
      if x == x.parent.left
          w = x.parent.right
          if w.color == red 
              w.color = black
              x.parent.color = red
              LEFT-ROTATE(T, x.parent)
              w = x.parent.right
          if w.left.color == black and w.right.color == black 
              w.color = red
              x = x.parent
          else 
              if w.right.color == black 
                  w.left.color = black
                  w.color = red
                  RIGHT-ROTATE(T, w)
                  w = x.parent.right
              
              w.color = x.parent.color
              x.parent.color = black
              w.right.color = black
              LEFT-ROTATE(T, x.parent)
              x = T.root
      else
          code will be symmetric
  x.color = black
```

Here is the `RB-DELETE-FIXUP(T, x)` function in Python.  

```
 def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
```

Let's break down the above code step by step:

1. The function uses a while loop to traverse up the tree from node `x` (the node that replaced the deleted node) to the root, as long as `x` is not the root and its color is black (`x.color == 0`). This is because violating properties can propagate upward in the tree after deletion, so we need to fix the tree from the bottom up.
2. Within the loop, the function checks if `x` is the left child of its parent. Based on this, it performs different fix-up steps for the left and right cases.
3. If `x` is the left child (`x == x.parent.left`), the function sets `s` to be the sibling of `x` (the right child of `x.parent`).
4. If the sibling `s` is red (`s.color == 1`), it means that the sibling has two black children. To resolve this, the function performs some color changes and rotations:
   - `s.color` is set to black (`0`).
   - `x.parent.color` is set to red (`1`).
   - A left rotation is performed on `x.parent` to make the left child of `x.parent` (previously `s`) become the new sibling.
   - `s` is updated to the new sibling (right child of `x.parent`).
5. Now, `s` (the sibling) is guaranteed to be black. The function then checks the colors of `s`'s children.
   - If both children of `s` are black (`s.left.color == 0 and s.right.color == 0`), the function makes `s` red (`s.color = 1`) and moves up the tree to its parent (`x = x.parent`).
   - If at least one of `s`'s children is red, additional rotations and color changes are required to restore the red-black tree properties:
     - If `s.right` is black (`s.right.color == 0`), the function makes `s.left` black (`s.left.color = 0`), and `s` itself red (`s.color = 1`).
     - A right rotation is performed on `s` to make the left child of `s` (previously `s.left`) become the new sibling.
     - `s` is updated to the new sibling (left child of `x.parent`).
   - `s` is given the same color as its parent `x.parent`, and `x.parent` is made black (`x.parent.color = 0`).
   - `s.right` is made black (`s.right.color = 0`).
   - A left rotation is performed on `x.parent`.
6. After exiting the while loop, `x` is set to be the root of the tree, and its color is set to black (`x.color = 0`) to ensure that the root of the tree is always black.

By performing these rotations and color changes while traversing up the tree, the `delete_fix` function restores the red-black tree properties, ensuring that the tree remains balanced and satisfies all the necessary constraints after a node deletion.

Next, we have the leftRotate() operation, which is responsible for performing a single left rotation. Typically, this method would be marked as private since it serves as a helper function. It follows the algorithm CLRS [14] as described below:

```
 pseudocode for left rotations
 pre: right[x] != nil[T]
 pre: root's parent is nill[T]

 Left-Rotate(T,x)
    y = right[x]
    right[x] = left[y]
    p[left[y]] = x
    p[y] = p[x]


    if p[x] == nil[T] then root[T] = y
    else
       if x == left[p[x]] then left[p[x]] = y
       else
          right[p[x]] = y
    left[y] = x
    p[x] = y
```
Here is the `leftRotate()` function in Python.  
```
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
```
Let's explain the above code step by step:  
1. The method `left_rotate` takes a single parameter `x`, which represents the pivot node (or the node around which the left rotation will occur).
2. A temporary variable `y` is used to store the right child of node `x`, which will become the new root of the subtree after the left rotation.
3. The left child of node `y` is assigned to be the right child of node `x`. This step ensures that the left subtree of `y` (if any) becomes the right subtree of `x`.
4. The code then checks if the left child of `y` is not a sentinel node (`self.TNULL`). If it is not a sentinel node, it means that `y` had a left child, and we need to update the parent reference of that left child to point to `x`. This step is necessary to maintain the parent-child relationships in the tree after the rotation.
5. The parent of node `y` is updated to point to the parent of node `x`. This step ensures that the parent of the original subtree rooted at `x` (which could be the root of the entire tree or another subtree) now correctly points to `y` as its child.
6. The code checks if the parent of `x` is `None`. If it is, it means that `x` was the root of the tree before the rotation. In this case, the root of the entire tree is updated to be `y`.
7. If the parent of `x` is not `None`, then the code checks whether `x` was the left child or the right child of its parent. Depending on this information, the left or right child reference of the parent is updated to point to `y`. This ensures that the subtree rooted at `y` is correctly linked to its parent.
8. Now, `x` becomes the left child of `y` since `y` is now the new root of the subtree. The left rotation operation is completed by updating the parent of `x` to be `y`.

After executing this code, the subtree rooted at node `x` is rotated to the left, and `y` becomes the new root of the subtree, maintaining the red-black tree properties. The overall structure and order of the elements in the tree are preserved.  

Following the left rotation operation, we also have the rightRotate() operation, responsible for performing a single right rotation. Like the previous method, this one is typically marked as private since it serves as a helper function. The algorithm for the rightRotate() method, based on CLRS [14], is as follows:

```
 pseudocode for right rotation
 pre: left[x] != nil[T]
 pre: root's parent is nill[T]
 Right-Rotate(T,x)
    y = left[x]           // y now points to node to left of x
    left[x] = right[y]    // y's right subtree becomes x's left subtree
    p[right[y]] = x       // right subtree of y gets a new parent
    p[y] = p[x]           // y's parent is now x's parent

    // if x is at root then y becomes new root
    if p[x] == nil[T] then root[T] = y
    else
        // if x is a left child then adjust x's parent's left child or...

         if x == left[p[x]] then left[p[x]] = y
         else
         // adjust x's parent's right child
            right[p[x]] = y
    // the right child of y is now x
    right[y] = x
    // the parent of x is now y
    p[x] = y
 ```
 Here is the rightRotate function in Python.  
 ```
   def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
 ```
Let's explain the above code step by step:  
1. The method `right_rotate` takes a single parameter `x`, which represents the pivot node (or the node around which the right rotation will occur).
2. A temporary variable `y` is used to store the left child of node `x`, which will become the new root of the subtree after the right rotation.
3. The right child of node `y` is assigned to be the left child of node `x`. This step ensures that the right subtree of `y` (if any) becomes the left subtree of `x`.
4. The code then checks if the right child of `y` is not a sentinel node (`self.TNULL`). If it is not a sentinel node, it means that `y` had a right child, and we need to update the parent reference of that right child to point to `x`. This step is necessary to maintain the parent-child relationships in the tree after the rotation.
5. The parent of node `y` is updated to point to the parent of node `x`. This step ensures that the parent of the original subtree rooted at `x` (which could be the root of the entire tree or another subtree) now correctly points to `y` as its child.
6. The code checks if the parent of `x` is `None`. If it is, it means that `x` was the root of the tree before the rotation. In this case, the root of the entire tree is updated to be `y`.
7. If the parent of `x` is not `None`, then the code checks whether `x` was the right child or the left child of its parent. Depending on this information, the right or left child reference of the parent is updated to point to `y`. This ensures that the subtree rooted at `y` is correctly linked to its parent.
8. Now, `x` becomes the right child of `y` since `y` is now the new root of the subtree. The right rotation operation is completed by updating the parent of `x` to be `y`.

After executing rightRotate function code, the subtree rooted at node `x` is rotated to the right, and `y` becomes the new root of the subtree, maintaining the red-black tree properties. The overall structure and order of the elements in the tree are preserved.  

Throughout the process of implementing Red-Black Trees in Python, I encountered several significant challenges:

**Challenge 1: Node Color Representation**  
Effectively representing node colors in Python was one of the primary challenges. In Python, conventional boolean values (True and False) are typically used for binary color representations. However, Red-Black Trees require three colors - red, black, and a sentinel color for null leaves. Selecting a suitable color representation demanded careful consideration as it directly impacted the code's readability and maintainability.

**Challenge 2: Rotations and Parent-Child Relationships**  
The cornerstone of Red-Black Trees lies in rotation operations, specifically left and right rotations. These rotations are vital for maintaining tree balance during insertion and deletion operations. Understanding the intricacies of these rotations and ensuring accurate maintenance of parent-child relationships presented significant challenges. Additionally, it was crucial to implement these rotations efficiently, as they played a critical role in the overall performance of Red-Black Trees.

**Challenge 3: Node Insertion and Deletion**  
Implementing node insertion and deletion while preserving the Red-Black Tree properties proved to be the most demanding aspect of the project. Ensuring that the insertion and deletion processes maintained color balance and tree order required meticulous attention to detail. Handling various cases, including node colors, parent-child relationships, and tree balancing after insertions and deletions, demanded rigorous problem-solving and intellectual effort.

**Challenge 4: Handling Special Cases**  
Red-Black Trees are governed by specific rules to ensure balance and correctness. Managing special cases, such as root changes during insertion or maintaining balance after deletion, was challenging. These cases demanded a thorough understanding of the underlying principles and careful coding to ensure that all properties of Red-Black Trees were consistently preserved.

**Challenge 5: Recursion and Complexity Analysis**  
During the implementation of Red-Black Trees in Python, I encountered several situations where recursion was necessary. Understanding the depth of recursion and analyzing the time complexity of operations were essential to ensure that the implementation remained efficient and scalable.



## Summary
- Provide a summary of your findings
- What did you learn?

## Reference
[1] Red-black tree. In Wikipedia. Retrieved July 15, 2023, from https://en.wikipedia.org/wiki/Red%E2%80%93black_tree   
[2] Huja, H. Red-Black Tree. Medium. Retrieved July 15, 2023, from https://hardikahuja99.medium.com/red-black-tree-8cf904034a90  
[3] JavaTpoint. Red-Black Tree. Retrieved July 15, 2023, from https://www.javatpoint.com/red-black-tree  
[4] OpenGenus IQ. Time and Space Complexity of Red-Black Tree. Retrieved July 15, 2023, from https://iq.opengenus.org/time-and-space-complexity-of-red-black-tree/  
[5] Leung, C. Red-Black Trees. In Data Structures and Algorithms: A Comprehensive Guide. Retrieved July 15, 2023, from https://catherine-leung.gitbook.io/data-strutures-and-algorithms/red-black-trees  
[6] GeeksforGeeks. Deletion in Red-Black Tree. GeeksforGeeks. Retrieved July 15, 2023, from https://www.geeksforgeeks.org/deletion-in-red-black-tree/  
[7] Li, C. (2021, September 15). Algorithms and Data Structures - Chapter 14. University of Science and Technology of China. http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap14.htm  
[8] Sanjiv, K. Search Algorithms. Retrieved July 15, 2023, from http://www.cs.umsl.edu/~sanjiv/classes/cs3130/lectures/search1.pdf  
[9] Coding Ninjas. Introduction to Red-Black Trees. Coding Ninjas Studio. Retrieved July 15, 2023, from https://www.codingninjas.com/studio/library/introduction-to-red-black-trees  
[10] Borzoo Esmailloo. (2020, May 3). Augmenting Red-Black Trees. Medium. Retrieved July 15, 2023, from https://medium.com/swlh/augmenting-red-black-trees-d9b4cd7635f8  
[11] Baeldung. Red-Black Trees and Their Applications. Baeldung. Retrieved July 15, 2023, from https://www.baeldung.com/cs/red-black-trees-applications  
[12] GeeksforGeeks. Applications, Advantages, and Disadvantages of Red-Black Tree. GeeksforGeeks. Retrieved July 15, 2023, from https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-red-black-tree/  
[13] Byorgey, B. Counting Inversions via Rank Queries. Brent's Blog. Retrieved July 15, 2023, from https://byorgey.wordpress.com/2019/12/18/counting-inversions-via-rank-queries/  
[14] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. 2009. Introduction to Algorithms, Third Edition (3rd. ed.). The MIT Press.  
[15] Andrew Carnegie Mellon University. RedBlackTree. JavaDocs. Carnegie Mellon University. https://www.andrew.cmu.edu/user/mm6/95-771/examples/RedBlackTreeProject/dist/javadoc/redblacktreeproject/RedBlackTree.html#inOrderTraversal(redblacktreeproject.RedBlackNode)  
[16] CodesDope. Data Structures - Red-Black Trees Deletion. CodesDope. Retrieved July 15, 2023, from https://www.codesdope.com/course/data-structures-red-black-trees-deletion/  
[17] AskPython. Red-Black Tree in Python. AskPython. Retrieved July 15, 2023, from https://www.askpython.com/python/examples/red-black-tree-in-python