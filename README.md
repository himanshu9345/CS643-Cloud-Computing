# CS643-Cloud-Computing
NJIT CS643 Cloud Computing
## Programming Assignment
### Problem Statement
Write a Hadoop/Yarn MapReduce application that takes as input the 50 Wikipedia web pages
dedicated to the US states.
### Problem 1
Computes how many times the words “education”, “politics”, “sports”, and “agriculture” appear in
each file. Then, the program outputs the number of states for which each of these words is dominant. </br>

**Expected Output**
> education	30 </br>
> politics	11 </br>
> sports	9 </br>
### Problem 2.
Identifies all states that have the same ranking of these four words. For example, NY, NJ, PA may
have the ranking 1. Politics; 2. Sports. 3. Agriculture; 4. Education

**Expected Output**
> 1.education;2.agriculture;3.politics;4.sports;	Mississippi;Iowa; </br>
> 1.education;2.agriculture;3.sports;4.politics;	Pennsylvania;</br>
> 1.education;2.politics;3.agriculture;4.sports;	Tennessee;</br>
> 1.education;2.politics;3.sports;4.agriculture;	Alabama;West_Virginia;Virginia;Vermont;Texas;South_Carolina;Oregon;Ohio;North_Carolina;New_York;Wyoming;Michigan;Kentucky;Hawaii;Delaware;California;Arkansas; </br>
> 1.education;2.sports;3.agriculture;4.politics;	Oklahoma; </br>
> 1.education;2.sports;3.politics;4.agriculture;	Louisiana;Kansas;Arizona;Florida;Washington;Missouri;Maryland;New_Mexico; </br>
> 1.politics;2.agriculture;3.education;4.sports;	North_Dakota; </br>
> 1.politics;2.education;3.agriculture;4.sports;	Alaska;</br>
> 1.politics;2.education;3.sports;4.agriculture;	Idaho;Nevada;Maine;New_Hampshire;Massachusetts;</br>
> 1.politics;2.sports;3.agriculture;4.education;	Wisconsin;</br>
> 1.politics;2.sports;3.education;	Rhode_Island;</br>
> 1.politics;2.sports;3.education;4.agriculture;	Utah;Georgia;</br>
> 1.sports;2.education;3.politics;4.agriculture;	South_Dakota;Illinois;Indiana;Connecticut;Montana;New_Jersey;</br>
> 1.sports;2.politics;3.education;4.agriculture;	Colorado;Minnesota;Nebraska;</br>
### Extra Credit
Build your own Hadoop AMI, starting from the Amazon Linux AMI
