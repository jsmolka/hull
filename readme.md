# hull
Concave hull around a dataset of points.

## How to use
```python
from hull import *

h = concave_hull(dataset, k)
```
The function takes two arguments. The first one is a dataset containing points in tuple form (x, y). The second one defines the number of nearest neighbours the algorithm is using interally. If there are some points outside the hull, the algorithm will call itself again with a higher k until all points are inside the concave hull.

## Examples
![10.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/10.png)
![50.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/50.png)
![200.png](https://raw.githubusercontent.com/jsmolka/hull/master/pictures/200.png)

## Requirements
- [pyprocessing](https://github.com/jsmolka/pyprocessing) if you want to run the visual examples

## Reference
The algorithm is based on a [paper](https://github.com/jsmolka/hull/blob/master/reference/concave_hull.pdf) by Adriano Moreira and Maribel Yasmina Santos.

## Disclaimer
I copied / ported some parts from [Matotempo's](https://github.com/Mapotempo/mapotempo-web/blob/master/lib/concave_hull.rb) Ruby approach.
