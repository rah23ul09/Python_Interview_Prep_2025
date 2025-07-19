def reverse_string(str):
    return str[::-1]


print(reverse_string("Rahul"))


class ReverseString:
    def reverse(self, str):
        return str[::-1]


reverse_str = ReverseString()
print(reverse_str.reverse("Rahul"))
