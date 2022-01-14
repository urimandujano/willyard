# How does this service add value when external services can just poll HTTP
statuses on loop?


1) Implements intelligent backoff
2) Can run in asynchronous or synchronous mode:
    - async -> callback is specified
        - "callback" should support multipl ways of notifiying
    - sync  -> request to monitor will wait until completion