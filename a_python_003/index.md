# How to Index and Transform in Numpy Arrays?


In [previous post](https://doraemonj.github.io/a_python_002/), we learnt how to create arrays with numpy. Today we're going to talk about how to index and transform numpy arrays.

When it comes to arrays, we usually use quare brackets `[]` to index and slice:

>    arr = np.arange(6).reshape(3,2)

`.arange` method specified `arr`  array with 6 elements, and `.reshape` method specified tha array with 3 rows and 2 colonms. Print `arr`:

>   print(arr)

Feedback:

>   array([[0, 1],<br />&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [2, 3],<br />&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [4, 5]])

### How to index or select elements in array?

#### Select a column

If you want to select a column, say, the rightmost column `1,3,5`:

>    arr[:, 1]

The colon `:` here means to specify the start and end place you need from the origal array. 

Feedback:

>   array([1, 3, 5])

#### Select multiple columns

>   arr[:, [0,1]]

Feedback:

>   array([[0, 1],<br />
>   &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[2, 3],<br />
>   &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[4, 5]])

#### Select a row

>   arr[1, :]

Feedback:

>   array([2, 3])

#### Select multiple rows

>   arr[[0,1], :]

Feedback:

>   array([[0, 1],<br />
>   &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; [2, 3]])

#### Select a specific element

>   arr[1,1]

Feedback:

>   3

#### Single condition

Select a row in which the rightmost elment is greater than 2:

>   arr[arr[:, 1]>2,]

Feedback:

>   array([[2, 3],<br />
>   &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; [4, 5]])

#### Multiple conditions

Select a row that meets both conditions, which are the rightmost elment is greater than 2 and the rightmost elment is less than 4:

>   arr[(arr[:,1]>2) & (arr[:, 1]<4),]

Feedback:

>   array([[2, 3]])

### How to transform the array?

In practice, we often need to change the form of the array. There are basically four method:

#### Change array dimensions

>    arr.reshape(2,3)

Feedback:

>   array([[0, 1, 2],<br />
>   &nbsp; &nbsp; &nbsp; &nbsp;  [3, 4, 5]])

Notice: `arr` is a new array with a different set of dimensions.

####  Transposition of arrays

>   arr.T

or

>   np.transpose(arr)

`.T` method or `np.transpose()` function reversed the look of the array compeletely. We see following below:

>   array([[0, 2, 4],<br />
>   &nbsp; &nbsp; &nbsp; &nbsp;  [1, 3, 5]])

`arr` has not changed yet. When we input `print(arr)` in the python console, we'll get the feedback:

>   &nbsp; [[0 1]<br />&nbsp; [2 3]<br />
>    &nbsp; [4 5]]

#### Flatten the array

>   arr.flatten()

Feedback:

>   array([0, 1, 2, 3, 4, 5])

`.flatten()` function takes us a one-dimension array.


























