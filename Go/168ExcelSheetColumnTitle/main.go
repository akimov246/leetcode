package main

import (
	"fmt"
)

func main() {
	fmt.Println(convertToTitle(1))
	fmt.Println(convertToTitle(28))
	fmt.Println(convertToTitle(701))
}

var columntTitleMap = map[int]rune{
	0:  'A',
	1:  'B',
	2:  'C',
	3:  'D',
	4:  'E',
	5:  'F',
	6:  'G',
	7:  'H',
	8:  'I',
	9:  'J',
	10: 'K',
	11: 'L',
	12: 'M',
	13: 'N',
	14: 'O',
	15: 'P',
	16: 'Q',
	17: 'R',
	18: 'S',
	19: 'T',
	20: 'U',
	21: 'V',
	22: 'W',
	23: 'X',
	24: 'Y',
	25: 'Z',
}

func convertToTitle(columnNumber int) string {
	var columnTitle string

	for columnNumber != 0 {
		columnNumber--
		columnTitle = string(columntTitleMap[columnNumber%len(columntTitleMap)]) + columnTitle
		columnNumber /= len(columntTitleMap)
	}

	return columnTitle
}
