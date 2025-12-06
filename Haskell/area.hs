area :: Floating a => a -> a
area r = pi * r ^ 2
double :: Floating a => a -> a
double x = x * 2
quad :: Floating a => a -> a
quad x = double(double x)
add :: Num a => a -> a -> a
add x y = x + y
areaRect :: Num a => a -> a -> a
areaRect l w =  l * w
areaSquare :: Num a => a -> a
areaSquare x = areaRect x x
cylinder :: Floating a => a -> a -> a
cylinder r h = h * area r
heron :: Floating a => a -> a -> a -> a
heron a b c = sqrt (s * (s-a) * (s-b) * (s-c))
    where
    s = (a + b + c)/2
tri :: Floating a => a -> a -> a -> a
tri a b c = b * height / 2
    where
    cosa = (b^2 + c^2 - a^2) / (2 * b * c)
    sina = sqrt (1-cosa^2)
    height = c * sina