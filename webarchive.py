from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from time import sleep
import numpy as np

# an array to store all the drivers (windows) that we open
drivers = np.array([])

def openNewWindow(url, width, height, x, y):
    """
    openNewWindow opens the given url in a new window. Used to open 1 url.
    
    @param url
    @param width      the width of the window
    @param height     the height of the window
    @param x          the x position of the window's top left corner
    @param y          the y position of the window's top left corner
    """
    # we are going to create some options specific to the Chrome browser
    options = webdriver.ChromeOptions()
    # make sure the window stays open
    options.add_experimental_option("detach", True)
    # initialize the Chrome browser
    driver = webdriver.Chrome(options=options)
    # set the window's width and height
    driver.set_window_size(width, height)
    # set the window's top left corner position
    driver.set_window_position(x, y)
    # launch the url in chrome
    driver.get(url)

    # we want to access our "global" drivers variable that we declared on line 7
    global drivers
    # add the driver to our list of open drivers
    drivers = np.append(drivers, driver)

def openWindowsRandomPosition(urls, width, height, interval):
    """
    openWindowsRandomPosition opens the given urls in new windows at random positions.
                              Note: this will open a separate window for every url and keeps them
                              open. The number of windows open at the end will = # of urls
    
    @param urls       the array of urls to open, in order
    @param width      the width of the windows
    @param height     the height of the windows
    @param interval   the time interval in between each window launch, in seconds
    """
    for url in urls: # for each url
        # open url in new window
        openNewWindow(url, width, height, np.random.randint(1400 - width), np.random.randint(800 - height))
        # wait for [interval] seconds before opening the next window
        sleep(interval)


def openWindowsRandomSizeAndPosition(urls, min_width, max_width, min_height, max_height, interval):
    """
    openWindowsRandomPosition opens a list of urls in separate windows at random positions and with
                              random width/height. If there are more than five windows open, it will
                              start closing the oldest window.
    
    @param urls         the array of urls to open, in order
    @param min_width    the minimum width of a window
    @param max_width    the maximum width of a window
    @param min_height   the minimum width of a window
    @param max_height   the maximum width of a window
    @param interval     the time interval in between each window launch, in seconds
    """
    for url in urls: # for each url
        # set a random width between min and max
        width = np.random.randint(min_width, max_width)
        # set a random height between min and max
        height = np.random.randint(min_height, max_height)
        # open url in new window at a random position
        # btw seems like on my 13" macbook pro, the max width is 1400, height is 800 so I'm going to
        # ensure that the position keeps the window fully visible.
        openNewWindow(url, width, height, np.random.randint(0, (1400 - width)), np.random.randint(0, (800 - height)))

        # we want to access our "global" drivers variable that we declared on line 7
        global drivers
        # if there are more than 5 windows open
        if drivers.size > 5:
            # select the first window in our array
            first_driver = drivers[0]
            # close the first window
            first_driver.close()
            # remove that window from our drivers array
            drivers = drivers[1:]

        # wait for [interval] seconds before opening the next window
        sleep(interval)
  

def openWindowPlayYoutube(url, width, height, x, y):
    """
    openWindowPlayYoutube opens the youtube video url and presses the play button.

    @param url        the url
    @param width      the width of the window
    @param height     the height of the window
    @param x          the x position of the window's top left corner
    @param y          the y position of the window's top left corner
    """
    # we are going to create some options specific to the Chrome browser
    options = webdriver.ChromeOptions()
    # make sure the window stays open
    options.add_experimental_option("detach", True)
    # initialize the Chrome browser
    driver = webdriver.Chrome(options=options)    
    # set the window's width and height
    driver.set_window_size(width, height)
    # set the window's top left corner position
    driver.set_window_position(x, y) # seems like max width is 1400, height is 800
    driver.get(url)

    # find the play button
    play_button = driver.find_element(By.CLASS_NAME, "ytp-large-play-button")
    # click the play button
    play_button.click()

if __name__ == "__main__":
    # TODO: call the functions you need in here!

    # example:

    # open youtube link and play video
    openWindowPlayYoutube("https://www.youtube.com/watch?v=uDRLW748j68", 720, 720, 300, 150)
    # pause for 4 seconds before opening other urls
    sleep(4)

    # initialize urls array
    urls = np.array([])
    urls = np.append(urls, "https://www.selenium.dev")
    urls = np.append(urls, "https://www.selenium.dev")
    urls = np.append(urls, "https://www.selenium.dev")
    urls = np.append(urls, "https://www.selenium.dev")
    
    # randomize order of urls
    np.random.shuffle(urls)

    openWindowsRandomSizeAndPosition(urls, 200, 1000, 200, 800, .5)
