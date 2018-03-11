import time

import requests


TOKEN = 'Replace this string with your token'
TRACK_FILE = '20_tracks'  # Change it to `40_tracks` and `60_tracks` and see the result


def fetch_track(track_id):
    resp = requests.get('https://api.kkbox.com/v1.1/tracks/' + track_id,
                        params={'territory': 'TW'},
                        headers={'Authorization': 'Bearer ' + TOKEN})
    return resp.json()


def fetch_tracks_briefly(track_ids):
    results = list()
    for count, track_id in enumerate(track_ids, start=1):
        track_info = fetch_track(track_id)
        results.append((
            track_info['id'],
            track_info['name'],
            track_info['album']['artist']['name']))
        print('Fetched {} tracks.'.format(count))
    return results


def main():
    with open(TRACK_FILE) as f:
        track_ids = [track_id.strip() for track_id in f]

    start = time.time()
    results = fetch_tracks_briefly(track_ids)
    end = time.time()

    for track_brief in results:
        print('{}    {}    {}'.format(*track_brief))
    print('Fetched {} tracks in {:.3f} seconds.'.format(
        len(results), end-start))


if __name__ == '__main__':
    main()
