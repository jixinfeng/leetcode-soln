"""
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no
restriction on how your encode/decode algorithm should work. You just need to
ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
to the original URL.
"""
class Codec:
    def __init__(self):
        self.chartable = {i : str(i) for i in range(10)}
        for i in range(10, 36):
            self.chartable[i] = chr(55 + i)
        for i in range(36, 62):
            self.chartable[i] = chr(61 + i)
        self.urltable= {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        #shadec = int(hashlib.sha256(longUrl.encode()).hexdigest(), 16)
        shadec = hash(longUrl)
        idx = []
        while len(idx) < 6:
            shadec, digit = divmod(shadec, 62)
            idx.append(self.chartable[digit])
        urlkey = "".join(idx[::-1])
        self.urltable[urlkey] = longUrl
        return "http://tinyurl.com/" + urlkey

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        urlkey = shortUrl.split('/')[-1]
        return self.urltable[urlkey]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
import hashlib
a = Codec()
print(a.decode(a.encode("www.google.com")))
print(a.decode(a.encode("www.facebook.com")))
print(a.decode(a.encode("www.amazon.com")))
