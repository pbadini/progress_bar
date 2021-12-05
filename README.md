# Progress Bar
Just a simple com progress bar for terminal aplications with some options for customization.


## Using the Bar
To use the progress bar you have to create a **ProgressBar** object and call the **show()** method passing the percent of bar that should be filled.
```python
bar = ProgressBar()
bar.show(50)
```
Output:
```bash
Process 0  █████████████████████████                          50.00%
```



## Customization
You can pass some paramter for customization in the constructor of the class, such as color of the bar and the character that fills the bar.
```python
class ProgressBar:
  def __init__(self, 
              num_of_bars = 1, 
              size = 50, 
              fill = '█',
              fill_color = 'reset', 
              background = '▒',
              background_color = 'reset',
              process = 'Process {}  '):
```
- You can determine the size of the bar and the character the will be the the background of the bar and the one that will fill it.

- There are 8 color for the bar and its background, they are:  ![#000000](https://via.placeholder.com/15/000000/000000?text=+) black    ![#ff0000](https://via.placeholder.com/15/ff0000/000000?text=+) red    ![#00ff00](https://via.placeholder.com/15/00ff00/000000?text=+) green    ![#ffff00](https://via.placeholder.com/15/ffff00/000000?text=+) yellow    ![#0000ff](https://via.placeholder.com/15/0000ff/000000?text=+) blue    ![#ff00ff](https://via.placeholder.com/15/ff00ff/000000?text=+) magenta    ![#00ffff](https://via.placeholder.com/15/00ffff/000000?text=+) cyan    ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) white  

- The process parameter is the message that will be printed before the bar, this paramter must have a place holder for a number

- You cran create more than one progress bar with the parameter num_of_bars, when using more than one bar you have to pass the bar you are using in the second parameter of the **show()** method

For the code: 
```python
bar = ProgressBar(num_of_bars = 2, 
                    size = 30, 
                    fill = '░', 
                    fill_color = 'green', 
                    background = '▔', 
                    background_color = 'red', 
                    process = 'Progress Bar {}  ')
bar.show(30, 0)
bar.show(65, 1)
```
The output should look something like that:

![image](https://user-images.githubusercontent.com/48367584/144766059-f4e9b8a1-32a4-4c8b-a4e7-0566d909aac7.png)




