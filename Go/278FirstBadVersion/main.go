package main

func main() {

}

func firstBadVersion(n int) int {
	l := 1
	r := n
	m := (r + l) / 2
	for l < r {
		if isBadVersion(m) && !isBadVersion(m-1) {
			return m
		}
		if !isBadVersion(m) {
			l = m + 1
		} else {
			r = m - 1
		}
		m = (r + l) / 2
	}
	return m
}
