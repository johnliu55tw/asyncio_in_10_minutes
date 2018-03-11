import asyncio
import time

import aiohttp


TOKEN = 'Replace this string with your token'
TRACK_FILE = '20_tracks'  # Change it to `40_tracks` and `60_tracks` and see the result


async def fetch_track(track_id):
    async with aiohttp.request('GET',
            'https://api.kkbox.com/v1.1/tracks/' + track_id,
            params={'territory': 'TW'},
            headers={'Authorization': 'Bearer ' + TOKEN}) as resp:
        return await resp.json()


async def fetch_tracks_briefly(track_ids):
    results = list()
    futures = asyncio.as_completed(
            [fetch_track(track_id) for track_id in track_ids])

    for count, future in enumerate(futures, start=1):
        track_info = await future
        results.append((
            track_info['id'],
            track_info['name'],
            track_info['album']['artist']['name']))
        print('Fetched {} tracks.'.format(count))
    return results


def main():
    with open(TRACK_FILE) as f:
        track_ids = [track_id.strip() for track_id in f]

    loop = asyncio.get_event_loop()
    start = time.time()
    results = loop.run_until_complete(fetch_tracks_briefly(track_ids))
    end = time.time()

    for track_brief in results:
        print('{}    {}    {}'.format(*track_brief))
    print('Fetched {} tracks in {:.3f} seconds.'.format(
        len(results), end-start))


if __name__ == '__main__':
    main()
