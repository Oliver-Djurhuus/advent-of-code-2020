import Data.List
import Data.List.Split (splitOn) 
import Data.List.Utils (replace)
import Data.Char

-- run: cat input.txt | ./advent4

-- Part a
requiredFields = ["byr","ecl","eyr","hcl","hgt","iyr","pid"]

isValid1 :: [[String]] -> Bool
isValid1 passport = requiredFields == sort (filter (/= "cid") (map head passport))


-- Part b
validField :: [String] -> Bool
validField ["byr", x] = 1920 <= read x && read x <= 2002
validField ["cid", _] = True
validField ["ecl", x] = 1 == length (filter (\y -> y == x) ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] )
validField ["eyr", x] = 2020 <= read x && read x <= 2030
validField ["hcl", x] = length x == 7 && head x == '#' && 0 == length (filter (==False) (map isHexDigit (tail x)))
validField ["hgt", x] = (length x == 5 && 150 <= read (drop 0 (take 3 x)) && read (drop 0 (take 3 x)) <= 193 && "cm" == drop 3 (take 5 x)) || (length x == 4 && 59 <= read (drop 0 (take 2 x)) && read (drop 0 (take 2 x)) <= 76 && "in" == drop 2 (take 4 x))
validField ["iyr", x] = 2010 <= read x && read x <= 2020
validField ["pid", x] = length x == 9 && 9 == length (filter (\y -> isDigit y) x)

isValid2 :: [[String]] -> Bool
isValid2 passport = 0 == length (filter (==False) (map validField passport))


-- Main
main = do  
    contents <- getContents  

    let passports = map (map (splitOn ":")) $ map (filter(\x -> x /= "")) $ map (splitOn " ") (map (replace "\n" " ") (splitOn "\n\n" contents))
    
    print "Answer for part (a):"
    print $ length $ filter (\passport -> isValid1 passport) passports 

    print "Answer for part (b):"
    print $ length $ filter (\passport -> isValid1 passport && isValid2 passport) passports     
     
