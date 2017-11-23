# KANO Make Light Lightboard Animations
_Cool animations created with KANO Make Light App for the KANO Lightboard Power-Up._

Cool animations that run in the background while [KANO OS :computer:](http://developers.kano.me/downloads/) is working.

An example:

![alt text](https://github.com/scollovati/kano_make_light_lightboard_examples/blob/master/kano_labs.gif)

Here you'll find a simple recipe for creating your own looped animation.
## 1. Log-in into your KANO
You can work directly in KANO OS or you can connect remotely to it (i.e. via SSH).

## 2. Create your own animation
Now download our [test file](https://raw.githubusercontent.com/scollovati/kano_make_light_lightboard_animations/master/test01.py) and copy it to your home folder (or wherever you prefer).

Rename it.

Open it with your favorite text editor and edit the code after the row ```while True:```.

Please remember to **indent** your code :smile:

You can find some cool examples:
- on the [KANO Make Light official page](https://world.kano.me/shares/make-light/);
- in this repository.

## 3. Test it
Open a terminal, go to the home folder (or where you placed the Python code) and launch it
```
python FILENAME.py
```

## 4. Auto start-up
In order to automatically loop the animation at the OS boot, we neet to add to the file `/etc/rc.local` the following code
```
python /home/USERNAME/FILENAME.py
```
Here we assumed that the file is in the home folder: if not modify the path accordingly.

## Acknowledgments
[KANO Developers](http://developers.kano.me/downloads/) for this great and cool software and hardware :v:
