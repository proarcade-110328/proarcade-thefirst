numbers :: [Integer]
numbers = [0,3,2,8]
truths :: [Bool]
truths = [True, False]
strings :: [String]
strings = ["Junseop", "Song"]
xor :: Bool -> Bool -> Bool
xor x y = (x||y) && not (x && y)
mySignum :: (Num a, Ord a) => a -> a
mySignum x
    | x > 0 =       1
    | x < 0 =      -1
    | otherwise =     0