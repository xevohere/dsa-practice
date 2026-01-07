def max_odd_number_in_string(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2==1:
            return s[:i+1]
    return ""

s1="1234567"
s2="12468"
s3="13579"
print(max_odd_number_in_string(s1))
print(max_odd_number_in_string(s2))
print(max_odd_number_in_string(s3)) 