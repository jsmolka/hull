# hull
Concave hull around dataset of points.

# How to use
```python
from hull import *

h = concave_hull(dataset, k)
```
The dataset is a list of points in tuple form (x, y). The argument k is the number of nearest neighbours the algorithm is using internally. If the hull does not contain every point from the dataset the algorithm will call itself again with a higher k.

Here are some examples:
![10_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/10_points.png)
![25_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/25_points.png)
![50_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/50_points.png)
![100_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/100_points.png)
![200_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/200_points.png)

# Reference
The algorithm is based on a [paper](https://github.com/jsmolka/hull/blob/master/reference/concave_hull.pdf) by Adriano Moreira and Maribel Yasmina Santos.

# Disclaimer
I copied / ported some part from [Matotempo's](https://github.com/Mapotempo/mapotempo-web/blob/master/lib/concave_hull.rb) Ruby approach.
