
'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''


class Codec:

    def __init__(self):
        self.table = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if hash(longUrl) not in self.table:
            self.table[hash(longUrl)]=longUrl
            return hash(longUrl)
        else:
            self.table[hash(longUrl)+1]=longUrl
            return hash(longUrl)+1
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.table:
            return self.table[shortUrl]