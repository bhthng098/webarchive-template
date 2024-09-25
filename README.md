# Web Archive Template

## Welcome!
This is a template for a web archive project that automates opening urls in browser windows.

This project uses the Selenium library in Python to open and control windows.

If you do not have selenium downloaded, you can run `pip install selenium` in your terminal.

You can find Selenium documentation here: https://www.selenium.dev and https://pypi.org/project/selenium/

To run `webarchive.py`, open your Terminal at the folder location of your file and type `python3 webarchive.py`

## Notes on using `webarchive.py`
`webarchive.py` is broken up into 5 parts.

There are 4 functions (each of these has full descriptions in `webarchive.py`):

`openNewWindow(url, width, height, x, y)`

`openWindowsRandomPosition(urls, width, height, interval)`

`openWindowsRandomSizeAndPosition(urls, min_width, max_width, min_height, max_height, interval)`

`openWindowPlayYoutube(url, width, height, x, y)`

You should call these functions in the last section that begins with `if __name__ == "__main__":`

In `if __name__ == "__main__":` I have an examples of how to make a list of urls appear.

## Examples

Examples of how you can use these functions in `if __name__ == "__main__":`

### Open and play a YouTube video
with a window width of 720, height of 500, at the location (300, 150) on your screen.
```
  openWindowPlayYoutube("https://www.youtube.com/watch?v=uDRLW748j68", 720, 500, 300, 150)
```

### Open one window
with a window width of 720, height of 500, at the location (300, 150) on your screen
```
  openNewWindow("https://www.selenium.dev", 720, 500, 300, 150)
```

### Open a list of URLS, each in a new window, at random positions
open 3 windows, each with a width of 720, height of 500, at random locations on your screen, with a 2 second interval in between each window launch.
```
  urls = np.array([])
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")

  openWindowsRandomPosition(urls, 720, 500, 2)
```

### Open a list of URLS, each in a new window, of random sizes and at random positions
Open 3 windows. Their widths will be random numbers between 300 and 1000. Their heights will be random numbers between 200 and 800. They will appear at random locations on your screen, with a 2 second interval in between each window launch.
```
  urls = np.array([])
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")

  openWindowsRandomSizeAndPosition(urls, 300, 1000, 200, 800, 2)
```

### Open a list of URLS in a random order
Open 3 windows in a random order, at random sizes and positions
```
  urls = np.array([])
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  np.random.shuffle(urls) # this line shuffles the URLs

  openWindowsRandomSizeAndPosition(urls, 300, 1000, 200, 800, 2)
```

### Open a list of urls with variable intervals
Open 8 windows where the first 2 windows have an interval of 2 seconds, the 3rd and 4th windows have an interval of 1.5 seconds, the 5th and 6th windows have an interval of 1 second, and the 7th and 8th windows have an interval of .5 seconds.
```
  urls = np.array([])
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")
  urls = urls.append("https://www.selenium.dev")

  openWindowsRandomSizeAndPosition(urls[0:2], 300, 1000, 200, 800, 2)
  openWindowsRandomSizeAndPosition(urls[2:4], 300, 1000, 200, 800, 2)
  openWindowsRandomSizeAndPosition(urls[4:6], 300, 1000, 200, 800, 2)
  openWindowsRandomSizeAndPosition(urls[6:], 300, 1000, 200, 800, 2)

```

### Open urls one at a time
Open 2 non-youtube URLS, 1 youtube URL, 1 non-youtube URL, and 1 youtube url.
```
  openNewWindow("https://www.selenium.dev", 750, 500, 120, 400)
  sleep(4) # wait for 4 seconds before opening next window

  openNewWindow("https://www.selenium.dev", 750, 500, 120, 400)
  sleep(2)

  openWindowPlayYoutube("https://www.youtube.com/watch?v=uDRLW748j68", 720, 500, 300, 150)
  sleep(4)

  openNewWindow("https://www.selenium.dev", 750, 500, 120, 400)
  sleep(2)

  openWindowPlayYoutube("https://www.youtube.com/watch?v=uDRLW748j68", 720, 500, 300, 150)

```
