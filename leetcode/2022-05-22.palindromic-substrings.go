package leetcode

func PalindromicSubstrings(s string) int {
	result := 0
	length := len(s)

	for i := 0; i < length; i++ {
		x := i - 1
		y := i + 1
		result++
		for x >= 0 && y < length && s[x] == s[y] {
			result++
			x--
			y++
		}
		x = i
		y = i + 1
		for x >= 0 && y < length && s[x] == s[y] {
			result++
			x--
			y++
		}
	}
	return result
}
