import sys

a = [10, 
'\x0b', 74, 'l', 32, 't', 121, 'h', 101, 'u', 107, 'h', 33, '\x0b', 12, '\x0c', 73, '(', 111, '#', 115, 
'p', 34, 'o', 117, 'd', 109, '|', 32, 'u', 113, '#', 104, 'b', 120, 'h', 32, 'c', 103, 'h', 110, 
'!', 121, 'l', 116, 'i', 34, '|', 111, 'v', 34, 'i', 111, 's', 34, 'r', 110, 'f', 34, 'z', 104, 
'p', 110, 'h', 32, 'z', 103, 'd', 114, '!', 60, ',', 10, '\n', 91, 'r', 117, '!', 111, 'd', 107, 
'f', 34, 'p', 101, '!', 106, 'd', 112, 'q', 123, '#', 98, 'f', 123, 'r', 110, 'e', 34, 'z', 111, 
's', 102, 'v', 44, '!', 99, 'q', 100, '!', 75, '*', 109, '!', 99, 'o', 119, 'b', 123, 'v', 32, 
'e', 99, '|', 100, 's', 103, 'd', 109, 'j', 112, 'j', 32, 'b', 100, 'r', 117, 'u', 34, '|', 111, 
'v', 48, '\r', 9, 'G', 116, 'r', 109, '!', 113, 'x', 114, '!', 72, 'u', 105, 'e', 99, '|', 32, 
'u', 116, 'l', 112, 't', 34, 'd', 110, 'e', 34, 'l', 109, 'q', 116, 'r', 112, 'u', 119, '#', 100, 
'b', 112, 'f', 101, 't', 34, 'l', 110, '!', 118, 'k', 101, '!', 73, 'd', 114, 'e', 103, 'q', 105, 
'b', 34, 'v', 116, 'b', 107, 'u', 119, 'f', 110, 'o', 10, '\n', 118, 'r', 32, 'u', 106, 'h', 32, 
'n', 103, 'd', 108, 't', 34, 'z', 101, '!', 103, 'd', 116, '!', 118, 'r', 103, 'f', 118, 'k', 101, 
's', 34, 'd', 110, 'e', 34, 'w', 104, 'f', 34, 'q', 105, 'h', 106, 'w', 115, '!', 75, '#', 115, 
'q', 103, 'q', 100, '!', 107, 'q', 32, 'z', 113, 'x', 114, '!', 100, 'h', 100, '!', 121, 'l', 116, 
'i', 34, '|', 111, 'v', 116, '#', 97, 's', 111, 'v', 32, 'b', 116, 'r', 117, 'o', 102, '#', 109, 
'f', 46, '\r', 9, 'J', 34, 'j', 101, 'o', 119, '0', 119, 'j', 112, 'h', 45, 'm', 123, '#', 118, 
'b', 110, 'x', 101, '!', 103, 'y', 101, 's', 123, '#', 112, 'j', 101, 'r', 115, 'f', 101, 'r', 110, 
'e', 34, 'L', 32, 't', 114, 'h', 110, 'e', 34, 'z', 105, 'u', 106, '#', 121, 'p', 119, '$', 10, 
'\n', 91, 'r', 117, '!', 106, 'd', 118, 'f', 34, 'd', 108, 'n', 113, 'v', 116, '!', 117, 'l', 110, 
'h', 110, 'h', 45, 'i', 99, 'q', 100, 'f', 102, 'o', 121, '!', 118, 'u', 97, 'o', 117, 'i', 111, 
's', 111, 'h', 100, '!', 111, '|', 32, 'V', 69, 'O', 65, '!', 103, '{', 112, 'f', 116, 'l', 101, 
'o', 101, 'h', 44, '\x0b', 11, 'd', 110, 'e', 34, 'L', 32, 'd', 99, 'q', 39, 'u', 34, 'z', 97, 
'j', 118, '#', 116, 'p', 34, 'v', 112, 'f', 112, 'g', 32, 'u', 106, 'h', 32, 's', 103, 'v', 116, 
'!', 113, 'i', 32, 'n', 123, '#', 108, 'j', 104, 'h', 32, 'x', 107, 'w', 104, '!', 123, 'r', 117, 
'!', 62, '6', 32, '\x0b', 11, 'L', 39, 'n', 34, 'v', 111, '!', 104, 'r', 114, 'u', 119, 'q', 97, 
'u', 103, '#', 116, 'p', 34, 'e', 101, '!', 99, 'e', 108, 'f', 34, 'w', 111, '!', 105, 'u', 111, 
'x', 34, 'z', 105, 'u', 106, '#', 121, 'p', 119, '#', 97, 't', 34, 'd', 32, 'q', 103, 'u', 115, 
'p', 112, '/', 10, '\n', 116, 'd', 105, 't', 103, '#', 107, 'j', 102, 'v', 32, ')', 106, 'x', 109, 
'b', 112, '#', 97, 'o', 102, '#', 103, 'p', 99, 'w', 32, 'b', 110, 'l', 107, 'f', 43, '#', 119, 
'j', 118, 'k', 32, 'z', 113, 'x', 44, '\x0b', 11, 'd', 110, 'e', 34, 'j', 105, 'w', 103, '#', 121, 
'p', 119, '#', 116, 'i', 103, '#', 98, 'j', 105, 'j', 101, 't', 118, '#', 111, 'g', 34, 'k', 117, 
'h', 117, '#', 97, 'u', 34, 'w', 104, 'f', 34, 'h', 110, 'e', 34, 'r', 102, '!', 103, 'd', 99, 
'i', 34, 'g', 97, 'z', 48, '\r', 9, '\\', 81, 'r', 112, 't', 46, '#', 73, '!', 121, 'd', 115, 
'!', 117, 'x', 112, 'q', 113, 'v', 101, 'e', 34, 'w', 111, '!', 109, 'h', 101, 'q', 34, 'w', 104, 
'j', 117, '#', 115, 'i', 113, 'u', 116, '!', 117, 'r', 32, 'z', 113, 'x', 32, 'e', 113, 'q', 39, 
'u', 34, 'k', 97, 'w', 103, '#', 116, 'p', 34, 'w', 121, 'q', 103, '#', 116, 'p', 113, '#', 109, 
'v', 101, 'k', 32, 'i', 103, 'k', 101, '^', 12, '\x0c', 65, 'o', 123, 'z', 97, 'z', 117, '/', 32, 
'v', 112, 'i', 111, 's', 118, 'x', 110, 'b', 118, 'h', 108, 'z', 46, '#', 119, 'f', 34, 'f', 97, 
'o', 41, 'w', 32, 'c', 103, '#', 112, 'i', 123, 'v', 105, 'd', 99, 'o', 108, 'z', 34, 'w', 111, 
'h', 103, 'w', 104, 'f', 116, '#', 102, 'p', 116, '#', 111, 'v', 116, '#', 97, 'o', 112, 'l', 118, 
'f', 116, 'v', 97, 's', 123, '\r', 9, 'e', 119, 'h', 32, 'u', 113, '#', 116, 'i', 107, 'v', 32, 
'q', 99, 'q', 100, 'f', 111, 'l', 99, '!', 93, 'w', 105, 'n', 103, '#', 99, 'b', 114, 'v', 117, 
'm', 103, '#', 109, 'b', 118, 'h', 114, 'j', 99, 'o', 93, '-', 34, 'e', 117, 'u', 34, 'l', 116, 
'(', 117, '#', 111, 'l', 99, '|', 32, 'c', 103, 'f', 97, 'v', 117, 'h', 32, 'z', 113, 'x', 39, 
's', 103, '#', 97, 'm', 121, 'd', 121, 't', 34, 'l', 110, '!', 111, '|', 32, 'i', 103, 'd', 114, 
'u', 34, '=', 41, '\x0b', 11, 'K', 101, 's', 103, '*', 115, '!', 118, 'r', 32, 'j', 112, 'i', 105, 
'o', 107, 'w', 121, '!', 111, 'r', 114, 'f', 34, '|', 101, 'b', 116, 'v', 32, 'u', 113, 'j', 101, 
'u', 106, 'h', 114, '-', 34, 'p', 111, 'w', 107, 'q', 103, '!', 118, 'r', 32, 'B', 119, 'v', 116, 
's', 99, 'o', 105, 'b', 46, '#', 111, 'v', 116, '#', 102, 'b', 116, 'p', 44, '!', 118, 'k', 101, 
'!', 110, 'l', 115, 'u', 34, 'j', 111, 'f', 117, '#', 111, 'o', 48, '1', 46, '\x0b', 12, 'V', 105, 
'o', 101, 'h', 114, 'f', 110, '|', 44, '\x0b', 91, 'r', 117, 's', 34, 'i', 97, 'w', 113, 'u', 105, 
'u', 103, '#', 75, 'p', 104, 'i', 101, 'f', 34, 'N', 111, 'b', 110, 'd', 32, '=', 53, '\r', 10]

print()
print()
print()

for i in range(len(a)):
    if (i % 4) % 2 == 0:
        sys.stdout.write(str(chr(int(a[i]) - (i % 4))))
    else:
        sys.stdout.write(str(chr(ord(a[i]) - (i % 4))))

print()
print()
print()
