class Solution:
    def compress(self, chars: list[str]) -> int:
        read=0
        write=0
        n=len(chars)
        while read<n:
            curr=chars[read]
            count=0
            while read<n and chars[read]==curr:
                count+=1
                read+=1
            chars[write]=curr
            write+=1
            if count>1:
                for dig in str(count):
                    chars[write]=dig
                    write+=1
        return write