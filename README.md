# Web Archive Template

## Welcome!
This is a template for a web archive project that automates opening urls in browser windows. To download the file, click on the green "code" button and select Download zip.

This project uses the Selenium library in Python to open and control windows.

### Installing dependencies
#### On Mac:

Please open your terminal and enter `python --version`, which will check whether you have Python installed and what version you have installed.

If it says that python is not a command, try `python3 --version`.

If `python3 --version` returned without an error, you should use `python3` to run commands instead of `python`.

You may close the terminal now.

In your file browser, navigate to the `webarchive-template` folder. Right click the folder and click "New Terminal at folder". In this terminal we are going to install selenium and numpy, two python libraries that we need in order to run this program.

if python is valid version, type and enter: \
`pip install selenium` \
(press enter. Once that install is complete, type) \
`pip install numpy`\
(enter)

if python3 is valid version, type and enter: \
`pip3 install selenium` \
(press enter. Once that install is complete, type) \
`pip3 install numpy`\
(enter)

You are all set. To run the webarchive project, type and enter `python webarchive.py` or `python3 webarchive.py` based on your version of python.

#### On Windows:
Please go to the Windows Store and download Python version 3.11 or higher.

In your file browser, go to your folder. Right click on the folder and click "copy path".

Open the Command Prompt app. Type `cd paste_your_path_here`, where paste_your_path_here is the copied path. Press enter. (This takes your command prompt to your folder so you can access those files directly.)

To install selenium, run and enter the command:\
`pip install selenium`

To install numpy, run and enter the command:\
`pip install numpy`

You should be all set. To run the webarchive project, type and enter `python webarchive.py`.

### Running the code
#### On Mac:
In your filesystem, go to location that the webarchive-template folder is in. Right click the webarchive-template folder, click "New Terminal at folder". Then, run the python script by typing and entering: `python3 webarchive.py` (or `python webarchive.py`)

#### On Windows:
In your filesystem, open the webarchive-template folder. Right click on it, select "Copy path". Open the Command Prompt app. Type and enter: `cd paste_your_path_here`. Then, run the python script by typing and entering: `python webarchive.py`


For reference, you can find Selenium documentation here: https://www.selenium.dev and https://pypi.org/project/selenium/

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
  openWindowsRandomSizeAndPosition(urls[2:4], 300, 1000, 200, 800, 1.5)
  openWindowsRandomSizeAndPosition(urls[4:6], 300, 1000, 200, 800, 1)
  openWindowsRandomSizeAndPosition(urls[6:], 300, 1000, 200, 800, .5)

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
