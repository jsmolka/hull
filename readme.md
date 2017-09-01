# hull
Concave or convex hull around a list of points.

## How to use
```python
import hull

points = [
    (207, 184), (393, 60), (197, 158), (197, 114), (128, 261), (442, 40),
    (237, 159), (338, 75), (194, 93), (33, 159), (393, 152), (433, 267),
    (324, 141), (384, 183), (273, 165), (250, 257), (423, 198), (227, 68),
    (120, 184), (214, 49), (256, 75), (379, 93), (312, 49), (471, 187),
    (366, 122)
]

concave_hull = hull.concave(points, 3)
convex_hull = hull.convex(points)
```
The code above creates the following results:

<img src="https://raw.githubusercontent.com/jsmolka/hull/master/example/concave.png" width="400"><img src="https://raw.githubusercontent.com/jsmolka/hull/master/example/convex.png" width="400">

## Requirements
- [pyprocessing](https://github.com/jsmolka/pyprocessing) if you want to run the visual examples

## References
- The concave hull algorithm is based on a [paper](https://github.com/jsmolka/hull/blob/master/reference/concave_hull.pdf) by Adriano Moreira and Maribel Yasmina Santos.
- The convex hull algorithm is an implementation of Andrew's monotone chain algorithm.

## Disclaimer
- Some parts of the concave hull algorithm were copied from [Matotempo's](https://github.com/Mapotempo/mapotempo-web/blob/master/lib/concave_hull.rb) Ruby approach.
- The entire convex hull algorithm is copy-pasted from a [wikibook](https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain) about algorithm implementations.
