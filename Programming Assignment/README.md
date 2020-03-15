# CS643-Cloud-Computing
NJIT CS643 Cloud Computing
## Programming Assignment
### Problem Statement
Write a Hadoop/Yarn MapReduce application that takes as input the 50 Wikipedia web pages
dedicated to the US states.
### Problem 1
Computes how many times the words “education”, “politics”, “sports”, and “agriculture” appear in
each file. Then, the program outputs the number of states for which each of these words is dominant. </br>

**My Output**
> education	30 </br>
> politics	11 </br>
> sports	9 </br>
### Problem 2.
Identifies all states that have the same ranking of these four words. For example, NY, NJ, PA may
have the ranking 1. Politics; 2. Sports. 3. Agriculture; 4. Education

**My Output**
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

## Assumptions
Please read my assumptions before grading.
1. All charcters/words are converted into lower case.
eg. Sports and sports are same

2. If the count of any two/three/four items are same then
lexicographically smallest will be considered first

e.g. sports-31 eductation-31 politics-31 agriculture-31
final order will be 1. agriculture 2. education 3. politics 4. sports

e.g. sports-30 eductation-31 politics-34 agriculture-31
final order will be 1. politics 2. agriculture 3. eductation 4. sports

3. If the important are any hyperlink or any delimiter then also its
considered in counting. Since the assignemnt question didn't mention to igrore a word with delimiter.
eg.. www.sports-sites.com,sports-play.png will be inculuded int counting
www.politicssitenew.com will be igrnored.

4. I have tried to parse the exact word so, 
education and educational are not same(though it contain education in it). 
I have igrnored word educational.


## Output
1. Output of CloudProject1.jar -> part1_part-r-00000
2. Output of CloudProject2.jar -> part2_part-r-00000


########################### </br>
Hadoop version 3.2.1 </br>
Open JDK version 1.8.0_222 </br>
########################### </br>
#### There are 4 files
1. CloudProjectPart1.java(Problem Statement 1)
2. CloudProjectPart2.java(Problem Statement 2)
3. CloudProject1.jar(packaged version of CloudProjectPart1.java)
4. CloudProject2.jar(packaged version of CloudProjectPart2.java)

#### My Testing Environment
AWS EMR.

## How to test it?
1. upload the states folder and 2 Jar files to into S3 bucket(if no bucket then create one).
2. Then create a 4 node EMR cluster on AWS in N.virgina region Latest Release emr beta 6.0.0
https://drive.google.com/file/d/18cpyXeCLHGNpv-gOX5y5L62Rf_pCU032/view?usp=sharing
3. Navigate to Steps tab and create a new step.
4. Click on Add Steps 
5. Select Custom JAR, Jar location in S3 Bucket. Pass the arguments
{input folder} {output folder}
s3://cloud-hadoop-mapreduce/states s3://cloud-hadoop-mapreduce/out3
6. Press Add.
7. Check for output in output folder specified in arguments. There 
will be miltiple parts in ouput check all of them to get the final result.

#### Test on Custom Hadoop Cluster
1. Test on your local cluster
2. To create 4 node cluster use AMI.txt

Create jar files from java files using following commands
```
mkdir classes
hadoop com.sun.tools.javac.Main -d classes/ CloudProjectPart1.java 
jar -cvf Part2.jar -C classes/ .
hadoop jar 'Part2.jar' CloudProjectPart2 HDFS/states HDFS/result5
```
*I will use
CloudProject1.jar
CloudProject2.jar
files to test*

Once Cluster is ready
1. Transfer states.tar.gz to NameNode using scp on your cluster
2. Extract it using tar -xvf states.tar.gz
Create the folder in HDFS(I  will create a HDFS folder for easy understanding) and transfer states folder into HDFS folder(a folder in hadoop filesystem)
3. hdfs dfs -mkdir -p HDFS
4. hdfs dfs -ls HDFS/
5. hdfs dfs -put 'states' HDFS </br>
6. hdfs dfs -ls HDFS/states (check if all 50 states file are there)
Run jar file using below command(you can provide any jar files provided in jar folder)
7. hadoop jar 'CloudProject1.jar' HDFS/states HDFS/result (if you get error saying output path arealy exist then try HDFS/result1 or some different path )
7. hadoop jar 'CloudProject2.jar' HDFS/states HDFS/result (if you get error saying output path arealy exist then try HDFS/result1 or some different path )
To check the output 
8. hdfs dfs -cat HDFS/result/part-r-00000 (to check the result and subsequent parts to get the final result)
