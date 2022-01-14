import asyncio
from tenacity import wait_exponential, retry, stop_after_attempt

from aiohttp import ClientSession

from willyard.worker.exceptions import WillyardException


def result_if_max_retry_count(retry_state):
    print("here")
    print(retry_state.outcome_timestamp)


@retry(
    wait=wait_exponential(multiplier=1, min=1, max=3),
    # stop=stop_after_attempt(10),
    before_sleep=result_if_max_retry_count,
)
async def willyard_worker(s: ClientSession):
    print("Async get")
    async with s.get("http://example.com") as resp:
        if resp.status == 200:
            raise WillyardException


async def willyard():
    async with ClientSession() as session:
        try:
            await willyard_worker(session)
        except:
            pass
        print(willyard_worker.retry.statistics)


async def main():
    await willyard()


if __name__ == "__main__":
    asyncio.run(main())
