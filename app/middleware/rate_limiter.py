import time 
from upstash_redis import Redis

from app.config import settings

_redis_client:Redis | None =None


def get_redis_client()->Redis:
    global _redis_client
    if _redis_client is None:
        _redis_client=Redis(url=settings.UPSTASH_REDIS_REST_URL,
                            token=settings.UPSTASH_REDIS_REST_TOKEN)
        
    return _redis_client

class RateLimiter:
    def __init__(self,max_requests:int,widnow_seconds:int=60):
        self.max_requests=max_requests
        self.window_seconds=widnow_seconds

    def is_allowed(self,key:str)->tuple[bool,int,int]:

        client=get_redis_client()

        now=time.time()

        window_start=now-self.window_seconds

        pipe=client.pipeline()
        pipe.zremrangebyscore(key,0,self.window_start)
        pipe.zadd(key,{str(now):now})
        pipe.zcard(key)

        pipe.expire(key,self.window_seconds)
        results=pipe.exec()

        request_count: int= results[2]
        remaining=max(0,self.max_requests-request_count)

        allowed=request_count<=self.max_requests

        return allowed,remaining,request_count


def is_allowed_ip(ip:str,route:str,limit:int,window_seconds:int)->tuple[bool,int,int]:
    limiter=RateLimiter(max_requests=limit,widnow_seconds=window_seconds)
    key=f"rate_limit:ip:{ip}:{route}"

    return limiter.is_allowed(key)


def is_allowed_user(
        user_id:str,limit:int =20, window_seconds:int=60
)->tuple[bool,int,int]:
    limiter=RateLimiter(max_requests=limit,widnow_seconds=window_seconds)
    key=f"rate_linit:user:{user_id}"

    return limiter.is_allowed(key)