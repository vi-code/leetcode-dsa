class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        str_parts = []
        for i in range(len(strs)):
            string_len = len(strs[i])
            str_parts.append(str(string_len)+"#"+strs[i])
            encoded_string = "".join(str_parts)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result: List = []
        ds = 0
        i = 0
        while i < len(s):
            j = s.index("#", i)
            # print("s[i:j]",s[i:j])
            # print(int(s[i:j]))
            decoded_str_len = int(s[i:j])
            end_str_index = j+1+decoded_str_len
            decoded_word = s[j+1:end_str_index]
            result.append(decoded_word)
            i = end_str_index
            # print("i:", i)
            # print("result:", result)
        return result