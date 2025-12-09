#!/bin/bash
set -e

# Test 1
echo -e "hello\nworld" | ./nl_upper > out1.txt
printf "   1\tHELLO\n   2\tWORLD\n" > exp1.txt
diff -u exp1.txt out1.txt

# Test 2
echo -e "abc\n\nxyz" | ./nl_upper > out2.txt
printf "   1\tABC\n   2\t\n   3\tXYZ\n" > exp2.txt
diff -u exp2.txt out2.txt

# Test 3
echo -e "\n" | ./nl_upper > out3.txt
printf "   1\t\n" > exp3.txt
diff -u exp3.txt out3.txt

echo "All tests passed!"
