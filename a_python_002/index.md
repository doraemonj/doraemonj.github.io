# How to Prepare Data with Numpy in Python


NumPy is a short name for `Numerical Python` which is a high-performance package for computing and analysing.

`ndarry` is the core function of Numpy, which means n-dimensional array.

The major differece between "array" and "list" is: the elements in array is the same kind, but in the list, there are can be a variety of types.

We usually use NumPy functions to create arrays quickly, more faster than using the functions from Standard Libery.

First, let's import Numpy module as most programmers do, abbreviating `Numpy` as `np`:

>   import numpy as np

### Create arrays

An `ndarray` is made by literal data and description information. 

We use:

​	 `.shape` 	to lookup the shape of an array

​	 `.dim` 		to lookup the dimensions



#### One-demension arrays

We create a one-dimension array in Python Console with inputting this command:

>   np.array([1,2,3], dtype=float)

One dimension array is also named "vector". We get feedback immediately:

>  array([1., 2., 3.])

This is our first one dimension array, aka "vector". It's useful, but not now.



#### Two-demension arrays

Then, let's make a two dimension array with Numpy:

>   np.array([[1,2,3],[4,5,6]])

Feedback from Python:

>   array([[1, 2, 3],
>          [4, 5, 6]])

This is a two dimension array.



#### Arithmetic progression arrays

Also, we made an arithmetic progression with a step length of 0.5:

>   np.arange(0,3,0.5)

Feedback from Python:

>    array([0. , 0.5, 1. , 1.5, 2. , 2.5])

As most functions in Python, it will take the start para into account but not take the last one, so this array is not included the number `3`.

If step length equals 1, then the last param can be omitted:

>   np.arange(0,3)

Feedback from Python:

>   array([0, 1, 2])



An arithmetic progression with four elements:

>   np.linspace(0,3,4)

Feedback:

>   array([0., 1., 2., 3.])

If we omit the last para `4`, then we'll get an arithmetic progression array with 50 elements:

>   np.linspace(0,3)

Feedback:

>   array([0.        , 0.06122449, 0.12244898, 0.18367347, 0.24489796,
>          0.30612245, 0.36734694, 0.42857143, 0.48979592, 0.55102041,
>          0.6122449 , 0.67346939, 0.73469388, 0.79591837, 0.85714286,
>          0.91836735, 0.97959184, 1.04081633, 1.10204082, 1.16326531,
>          1.2244898 , 1.28571429, 1.34693878, 1.40816327, 1.46938776,
>          1.53061224, 1.59183673, 1.65306122, 1.71428571, 1.7755102 ,
>          1.83673469, 1.89795918, 1.95918367, 2.02040816, 2.08163265,
>          2.14285714, 2.20408163, 2.26530612, 2.32653061, 2.3877551 ,
>          2.44897959, 2.51020408, 2.57142857, 2.63265306, 2.69387755,
>          2.75510204, 2.81632653, 2.87755102, 2.93877551, 3.        ])



#### Repeated arrays

Repeat every elments in array for two times: 

>   np.repeat([1,2], 2)

Feedback:

>   array([1, 1, 2, 2])



Repeat the whole array for two times:

>   np.tile([1,2], 2)

Feedback:

>   array([1, 2, 1, 2])

Just like tiling on a wall.



#### Arrays of all ones

>   np.ones((2,3))

Feedback:

>   array([[1., 1., 1.],
>          [1., 1., 1.]])



#### Arrays of all zeros

>   np.zeros((3,2))

Feedback:

>   array([[0., 0.],
>          [0., 0.],
>          [0., 0.]])



#### Arrays with random elements

If we wanna create an array with 3 random decimals from 0 to 1, then we code:

>   np.random.random(3)

Feedback:

>   array([0.19756156, 0.95824079, 0.37344019])



If we wanna get specific numbers from a normal distribution, then we code:

>   np.random.randn(3)

Feedback:

>   array([ 0.74662532, -1.32921822,  0.59149021])

`randn` means `rand`om numbers for `n`ormal distributions.



If we wanna an array with specific normal distribution:

>   np.random.normal(loc = 0, scale = 1, size = 5)

It means the mean value is 0, the standard deviation is 1, and the elements in array are 5. 

Feedback:

>   array([-0.32578159,  1.68852453,  0.31375627, -0.26488277,  0.19965238])



Moreover, NumPy supports a range of data types: bool, int8, int16, int32, int 64, unit8, unit16, unit32, uint64, float16, float32, float64, etc. We can use `.astype()`function to convert the data type.



See you next posts.



















