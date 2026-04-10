import time

class InMemoryCache:
    
    def __init__(self):
        self.store = {}

    def get(self, key: str):
        data = self.store.get(key)

        if not data:
            return None
        
        value, expiry = data

        if expiry and time.time() > expiry:
            del self.store[key]
            return None
        
        return value
    
    def set(self, key: str, value, ttl: int = None):
        expiry = time.time() + ttl if ttl else None
        self.store[key] = (value, expiry)
    
cache = InMemoryCache()