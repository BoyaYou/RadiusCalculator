# RadiusCalculator
**_Rolling Algorithm_**
  The Rolling Algorithm (RA) was developed and applied in this study to calculate curve radius. As shown in Fig 1, a radius-changeable circle rolls through the data set ordered by geolocation at a rolling speed of 1 point/time. When this circle stops at point _i_ (Fig 2), the coordinates of point _i_, point _i_-1 and point _i_+1 are read and used to identify the perpendicular bisectors of point _i_-1 and point _i_, point _i_ and point _i_+1. The coordinates of the center point can be calculated by solving equation (1), (2), and (3). Lastly, the curve radius can be calculated by measuring the distance between the center point and point _i_. Compared to the method of manually extracting geometric features from digital maps, the RA can identify both the radius of simple curves and also spiral curves. It should be noted that the lower the speed, the higher the accuracy of this algorithm. 

**Fig 1**
![alt tag](https://github.com/Apaul0246/RadiusCalculator/blob/master/Illustration_1.png)

**Fig 2**
![alt tag](https://github.com/Apaul0246/RadiusCalculator/blob/master/illustration_2.png)

**Fig 3**
![alt tag](https://github.com/Apaul0246/RadiusCalculator/blob/master/equations.png)