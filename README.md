# Python `asyncio` in 10 minutes

**`asyncio` in 10 minutes** is the talk I gave in SITCON 2018 @ KKBOX booth. This repository contains some useful information about the talk.

## Example code

### KKBOX Open API Token

Noted that you need to have a **token** for accessing **KKBOX Open API** to run the example code.
If you don't know what this is, check out the article [Beginner's guide for Python developers](https://docs-en.kkbox.codes/docs/beginners-guide-for-python-developers).

Nevertheless, if you don't want to read the whold article, follow these steps to retrive the token:

1. Go to [My Apps](https://developer.kkbox.com/#/app), register and create an app. You should see a page that has **ID** and **Secret**.
2. use the [`get_token.py`](./get_token.py), provides your **ID** and **Secret** as the command-line arguments to fetch the token. For example if your ID is `ffc7bfde578dcf76185d6695da165512` and Secret is `99c08eff076587acee496a01c5d8a66e`:
```
$ python3 get_token.py ffc7bfde578dcf76185d6695da165512 99c08eff076587acee496a01c5d8a66e
```
3. There should be a base64 encoded string printed on the screen. That is your token.
```
$ python3 get_token.py ffc7bfde578dcf76185d6695da165512 99c08eff076587acee496a01c5d8a66e
tGm6Nizi6zRd/kmBhgCXwg==  <- This is your token
```

### pipenv

The example code requires two modules: `requests` and `aiohttp`. `Pipfile`s are provided to create a development environment with `pipenv`:

```
$ cd asyncio_in_10_minutes
$ pipenv install --three
```

### Running the code

The directory `examples` contains two example codes: [`fetch_sync.py`](./examples/fetch_sync.py) and [`fetch_asyncio.py`](./examples/fetch_asyncio.py),
which demonstrate *fetching several tracks from KKBOX Open API* in synchronous and asynchronous manner respectively.

Before you run the example code, remember to set up the `TOKEN` variable with your own token:
```python
...

TOKEN = 'Replace this string with your token'

...
```

For example, if your token is `tGm6Nizi6zRd/kmBhgCXwg==`, the code should be like:
```python
...

TOKEN = 'tGm6Nizi6zRd/kmBhgCXwg=='

...
```

There are three files that contains different number of track IDs: [`20_tracks`](./examples/20_tracks), [`40_tracks`](./examples/40_tracks) and [`60_tracks`](./examples/60_tracks).
You should change the `TRACK_FILE` variable to one of the three track IDs files listed here and see the result.

### Caveat

If you have used `asyncio` before, or you have inspected the result carefully,
you should have noticed that their is a difference between `fetch_sync.py` and `fetch_asyncio.py`: The **order** of resulting tracks information compare to the input file.

I encourage you to see why is this happening and find out a solution after you have read [this chapter](https://docs.python.org/3/library/asyncio-task.html#task-functions) from the official document of `asyncio`
(Hint: `as_completed()` vs. `gather()`).

## Slides

* [Link to the slide.](http://slides.com/johnliu55tw/python-x-kkbox-open-api-3)
