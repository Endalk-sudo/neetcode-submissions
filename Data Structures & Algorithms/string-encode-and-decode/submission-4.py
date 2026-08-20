class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            
            if j == -1: break

            length = int(s[i:j])

            start = j + 1
            end = start + length

            decoded_strs.append(s[start:end])

            i = end

        return decoded_strs