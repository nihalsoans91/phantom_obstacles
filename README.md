
Map Filter

Nihal Solomon Soans1 ,

nihalsoans91@uga.edu

Abstract

- There is an autonomous navigation robot equipped

- with numerous active sensors. Using these sensors’

- readings, your software constructs a 2D map of the

- area surrounding the robot, indicating obstacles and

- clear areas (i.e. where the robot can go). This map

- is used for planning the motion of your robot so it

- avoids collisions with obstacles. Your software rep-

- resents the map as a constant sized image, where

- each pixel represents a 5x5 square centimeter area

- in the real world. Pixel values can only be one

- of the following: 0 for clear, 127 for unexplored

- and 255 for obstacle. The map is “pinned” to the

- robot, not to the ground (i.e. the robot is always in

- the same section of the map and the area mapped

- moves along the ground as the robot moves).

- As the robot moves through its environment and

- gathers sensor data, the map is updated.

- 1 Problem

- Active sensors are susceptible to interference and noise. De-

- spite applying numerous sensor ﬁlters, you discover that as

- your robot moves through different environments, very small

- “phantom” obstacles are detected (i.e. false positives) and the

- values of the corresponding pixels on the map are changed to

- 255=OBSTACLE. These phantom obstacles cause your robot

- to incorrectly believe that its path is blocked.

- Figure 1: Map annotated with obstacle, clear, and unknown pixels

- (white, black, gray). Also shown are the map areas the robot occu-

- pies (red), and an example of a phantom obstacle: the single pixel in

- the middle of the green box with no other obstacles. (The robot and

- the box are not part of the map)

2 Solution

We solve this problem using a ﬁlter of size 41 x 41 as askedin the problem statement. As shown in Figure 2 and 3 overthe whole image. This ﬁlter slides along the image similar tohow a convolution Neural Network works. The ﬁlter checksif there is any cluster of objects near it if there is it discard thethat iteration of the ﬁlter and moves to the next one. Figure2 will help understand this problem. All cells in Figure 2colored in green are obstacles and white are empty and onescolored in grey are unexplored. In our experiment we use a41 by 41 ﬁlter size but for simplicity we use a ﬁlter of size 6by 6.

Figure 2: Filter values that are got from the image which does notsatisfy the two conditions

The ﬁlter has an area called the target area this is shown inthe red border in Figure 2 and Figure 3 this area is the wherethe detection occurs. If there is no object in this area that is ifthe value is either 0 or 127 then the current area of interest isdiscarded and the next one is taken. This is done to preventunwanted resource utilization. Doing so helps us move tonext one without wasting resources. The target area can bechanged as per the users choice. Increasing this value will getbetter accuracy but will take a hit on resources. Upon tryingmultiple sizes of target area we recommend the size of 2 by2.

Once a pixel of number 255 or an object is discovered inthis target area. we then check all the values in the surround-ing ﬁlter if there is a object or value 255 current ﬁlter is dis-carded. Figure 2 shows a good example where the ﬁlter val-ues are discarded and the next one is taken. There are 255 inthe the target area and then there are multiple 255 around itthis hows. It ﬁgures out if there is a object close to it.![Im2](images/Im2)

![Im1](images/Im1)

- Figure 3: Filter values that are got from the image which satisﬁes

- the two conditions

Figure 6: The map after the processing ﬁnishes- Once both the conditions are satisﬁed, ( Target area and

- the Surrounding area ) the values inside the Target area is

- changed into zeros. Figure 3 shows where both the target and

- surrounding area conditions are satisﬁed. Figure 4 shows the

- post-processed ﬁlter values.

- Figure 4: Filter value after the two conditions are met

This algorithm takes 500 ms on an average to get the cor-rected image or map.

- 3 Results

- We executed the algorithm on the image provided in the PDF.

- Figure 5 shows the image that is received by the algorithm

- and Figure 6 show the image after the ﬁlter has been applied.

- Figure 5: The map before the processing begins

![Im3](images/Im3)

![Im6](images/Im6)

![Im4](images/Im4)

![Im5](images/Im5)

