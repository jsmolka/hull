# hull
Concave hull around a dataset of points.

## How to use
```python
from hull import *

h = concave_hull(dataset, k)
```
The function takes two arguments. The first one is a dataset containing points in tuple form (x, y). The second one defines the number of nearest neighbours the algorithm is using interally. If there are some points outside the hull, the algorithm will call itself again with a higher k until all points are inside the concave hull.

Here are some examples:
![10_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/10_points.png)
![25_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/25_points.png)
![50_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/50_points.png)
![100_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/100_points.png)
![200_points.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/200_points.png)

## Requirements
- [pyprocessing](https://github.com/jsmolka/pyprocessing) if you want to run the visual example

## Reference
The algorithm is based on a [paper](https://github.com/jsmolka/hull/blob/master/reference/concave_hull.pdf) by Adriano Moreira and Maribel Yasmina Santos.

## Disclaimer
I copied / ported some parts from [Matotempo's](https://github.com/Mapotempo/mapotempo-web/blob/master/lib/concave_hull.rb) Ruby approach.
